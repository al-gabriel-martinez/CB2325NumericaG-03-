"""
Módulo para cálculo de raízes de funções reais. Feito por: Anizio S. C. Júnior (aka AnZ)

Este módulo implementa métodos numéricos para encontrar raízes (zeros) de funções reais.
Implementações: Método da Bisseção, Método de Bisseção para múltiplas raízes, Método de Secante e Método de Newton-Raphson.
"""

from CB2325NumericaG3.visualizacao_raizes import VisualizadorRaizes

def bissecao(f, a, b, tol=1e-6, max_iter=100, graf=True, retornar_historico=False):
    """
    Encontra uma raiz da função f no intervalo [a, b] usando o Método da Bisseção.
    
    O método da bisseção é um algoritmo robusto que sempre converge quando
    f(a) e f(b) têm sinais opostos.

    Este método é muito semelhante ao conceito de intervalos encaixantes, repare
    que quando definimos um intervalo em que buscamos um zero nos vamos encaixando
    intervalo de metade do tamanho do anterior, entao cada vez mais vamos nos 
    aproximando do valor do zero da função, apesar de ser mais lento que o método
    de Newton ele é bem mais preciso e também mais consistente, assim como foi
    explicito na observação feito antes.
    
    Parameters
    ----------
    f : callable
        Função da qual se deseja encontrar a raiz.
    a : float
        Limite inferior do intervalo.
    b : float
        Limite superior do intervalo.
    tol : float, optional
        Tolerância para o critério de parada (padrão: 1e-6).
    max_iter : int, optional
        Número máximo de iterações (padrão: 100).
    graf : bool, optional
        Se mostra o gráfico da função ou não.
    retornar_historico : bool, optional
        Se retorna o historico de intervalos ou não.
    
    Returns
    -------
    float
        Aproximação da raiz da função.
    
    Raises
    ------
    ValueError
        Se f(a) e f(b) não têm sinais opostos.
    RuntimeError
        Se o método não convergir dentro do número máximo de iterações.
    
    Exemplos
    --------
    >>> f = lambda x: x**2 - 4
    >>> raiz = bissecao(f, 0, 3)
    >>> print(f"{raiz:.6f}")
    2.000000
    """
    fa = f(a)
    fb = f(b)
    
    # Verifica se há mudança de sinal
    if fa * fb > 0:
        raise ValueError(f"A função deve ter sinais opostos em a={a} e b={b}. "
                        f"f(a)={fa:.6f}, f(b)={fb:.6f}")
    
    # Verifica se os extremos já são raízes
    if abs(fa) < tol:
        return (a, [a]) if retornar_historico else a
    if abs(fb) < tol:
        return (b, [b]) if retornar_historico else b
    
    historico = []
    ultimo_c = None
    
    for i in range(max_iter):
        # Calcula o ponto médio
        c = (a + b) / 2.0
        fc = f(c)
        historico.append(c)
        
        # Verifica convergência
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            if graf:
                viz = VisualizadorRaizes(f)
                viz.visualizar(historico, a=a, b=b, titulo="Método da Bisseção")
            return (c, historico) if retornar_historico else c

        if ultimo_c is not None:
            if abs(c-ultimo_c) < 1e-15:
                raise RuntimeError(
                    f"Método da bisseção estagnou na iteração {i}"
                    f"Último c: {c:.12e}, f(c)={fc:.6e}, historico_size={len(historico)}"
            )

        ultimo_c = c 
        
        # Atualiza o intervalo
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    raise RuntimeError(f"Método da bisseção não convergiu após {max_iter} iterações.")

def bissecao_multiraizes(f, a, b, tol=1e-6, max_iter=100, max_raizes=10, subdivisoes=1000, graf=False):
    """
    Encontra até 'max_raizes' raízes de f(x) no intervalo [a, b] usando o método da bisseção.
    Se o número de raízes ultrapassar 'max_raizes', lança um aviso e interrompe.

    Parameters
    ----------
    f : callable
        Função cujo zero será procurado.
    a, b : float
        Limites do intervalo.
    tol : float
        Tolerância da bisseção.
    max_iter : int
        Iterações máximas da bisseção.
    max_raizes : int
        Número máximo de raízes a encontrar antes de interromper.
    subdivisoes : int
        Número de divisões do intervalo para detectar mudanças de sinal.
    graf : bool
        Se True, plota cada raiz encontrada.

    Returns
    -------
    list of float
        Lista com as raízes encontradas.
    """

    raizes = []
    x_vals = [a + i*(b-a)/subdivisoes for i in range(subdivisoes+1)]

    for i in range(subdivisoes):
        x0, x1 = x_vals[i], x_vals[i+1]
        f0, f1 = f(x0), f(x1)

        # Detecta mudança de sinal
        if f0 * f1 < 0:
            try:
                raiz = bissecao(f, x0, x1, tol=tol, max_iter=max_iter, graf=graf, retornar_historico=False)
                raizes.append(raiz)
            except Exception:
                continue  # Se der erro numérico, ignora o subintervalo

            # Se atingir o limite de raízes, interrompe
            if len(raizes) >= max_raizes:
                print( f"Atenção: limite de {max_raizes} raízes atingido. Interrompendo busca em [{a}, {b}].\n"
                       f"{len(raizes)} Raízes encontradas antes do limite:\n"
                       f"{raizes}")
                break

    return raizes

def newton_raphson(f, x0, df=None, tol=1e-6, max_iter=100, h=1e-8, graf=True, retornar_historico=False):
    """
    Encontra uma raiz da função f usando o Método de Newton-Raphson.
    
    O método de Newton-Raphson converge rapidamente quando próximo da raiz,
    mas requer o cálculo ou aproximação da derivada.

    Esse metodo utiliza de retas tangentes, definimos um ponto x_0 para começarmos
    e extraimos a reta tangente df(x_0)/dx daquele ponto utilizando de derivadas,
    após pergarmos a reta tangente desse ponto nos observamos onde ela intersecta
    o eixo x e pegamos aquele valor intersectado x_1 e fazemos o mesmo processo
    que fizemos com x_0, perceba que quanto mais iterações fizermos se aproxima,
    esse método também é mais rápido que o de bisseção, apesar de não ter tanta
    estabilidade em algumas funções, como o exemplo dado antes, f(x) = sex(1/x).
    
    Parameters
    ----------
    f : callable
        Função da qual se deseja encontrar a raiz.
    x0 : float
        Aproximação inicial da raiz.
    df : callable, optional
        Derivada da função f. Se não fornecida, será aproximada numericamente.
    tol : float, optional
        Tolerância para o critério de parada (padrão: 1e-6).
    max_iter : int, optional
        Número máximo de iterações (padrão: 100).
    h : float, optional
        Passo para aproximação numérica da derivada (padrão: 1e-8).
    graf : bool, optional
        Se mostra o gráfico da função ou não.
    retornar_historico : bool, optional
        Se retorna o historico de pontos ou não.
    
    Returns
    -------
    float
        Aproximação da raiz da função.
    
    Raises
    ------
    RuntimeError
        Se o método não convergir ou se a derivada for zero.
    
    Examples
    --------
    >>> f = lambda x: x**2 - 4
    >>> df = lambda x: 2*x
    >>> raiz = newton_raphson(f, 1.0, df)
    >>> print(f"{raiz:.6f}")
    2.000000
    
    >>> # Sem fornecer a derivada (aproximação numérica)
    >>> raiz = newton_raphson(f, 1.0)
    >>> print(f"{raiz:.6f}")
    2.000000
    """
    x = x0
    historico = [x0]
    
    for i in range(max_iter):
        fx = f(x)
        
        # Calcula a derivada
        if df is not None:
            dfx = df(x)
        else:
            # Aproximação numérica da derivada (diferenças finitas)
            dfx = (f(x + h) - f(x - h)) / (2 * h)
        
        # Verifica se a derivada é muito pequena
        if abs(dfx) < 1e-12:
            if retornar_historico:
                raise RuntimeError(f"Derivada zero. Último x: {x:.6f}, histórico: {historico}")
            else:
                raise RuntimeError(f"Derivada muito próxima de zero na iteração {i}. "
                             f"x={x:.6f}, f'(x)={dfx:.2e}")
        
        # Verifica convergência
        if abs(fx) < tol * 1e-2:
            if graf:
                viz = VisualizadorRaizes(f)
                viz.visualizar(historico, titulo="Método de Newton-Raphson")
            return (x, historico) if retornar_historico else x

        # Atualização de Newton
        x_new = x - fx / dfx
        historico.append(x_new)
        
        # Verifica convergência pela mudança em x
        if abs(x_new - x) < tol:
            if graf:
                viz = VisualizadorRaizes(f)
                viz.visualizar(historico, titulo="Método de Newton-Raphson")
            return (x_new, historico) if retornar_historico else x_new
        
        x = x_new
    if retornar_historico:
        raise RuntimeError(f"Método não convergiu após {max_iter} iterações. Último x: {x:.6f}, histórico: {historico}")
    else:
        raise RuntimeError(f"Método de Newton-Raphson não convergiu após {max_iter} iterações.")


def secante(f, a, b, tol=1e-6, max_iter=100, graf=True, retornar_historico=False):
    """
    Encontra uma raiz da função f(x) = 0 usando o Método da Secante.
    
    O método da secante é uma variação do método de Newton-Raphson que
    não requer o cálculo explícito da derivada da função. Ele utiliza
    uma aproximação baseada em duas estimativas iniciais e é útil quando
    df(x) é difícil de obter ou muito custosa de calcular.

    Parameters
    ----------
    f : callable
        Função cujo zero será encontrado.
    a, b : float
        Estimativas iniciais da raiz.
    tol : float, optional
        Tolerância para o critério de parada (padrão: 1e-6).
    max_iter : int, optional
        Número máximo de iterações (padrão: 100).
    graf : bool, optional
        Se mostra o gráfico da função e das aproximações (padrão: True).
    retornar_historico : bool, optional
        Se retorna o histórico de pontos (padrão: False).

    Returns
    -------
    float ou (float, list)
        Aproximação da raiz da função. Caso retornar_historico=True,
        retorna também a lista dos valores aproximados.

    Raises
    ------
    ZeroDivisionError
        Se f(b) e f(a) forem iguais.
    RuntimeError
        Se o método não convergir dentro do número máximo de iterações.

    Exemplos
    --------
    >>> f = lambda x: x**3 - 9*x + 5
    >>> raiz = secante(f, 0, 1)
    >>> print(f"{raiz:.6f}")
    0.586
    """

    historico = [a, b]

    for i in range(max_iter):
        f0 = f(a)
        f1 = f(b)

        if f1 == f0:
            raise ZeroDivisionError(
                f"Divisão por zero: f(b) = f(a) = {f1:.6f} na iteração {i}."
            )

        # Fórmula da secante
        x2 = b - f1 * (b - a) / (f1 - f0)
        historico.append(x2)

        # Verifica convergência
        if abs(x2 - b) < tol or abs(f(x2)) < tol:
            if graf:
                viz = VisualizadorRaizes(f)
                viz.visualizar(historico, titulo="Método da Secante")
            return (x2, historico) if retornar_historico else x2

        # Atualiza pontos
        a, b = b, x2

    raise RuntimeError(f"Método da secante não convergiu após {max_iter} iterações.")


def raiz(f, a=None, b=None, x0=None, df=None, tol=1e-6, max_iter=100, max_raizes=10, subdivisoes=1000, method="bissecao", graf=True, retornar_historico=False):
    """
    Interface unificada para encontrar raízes de funções.
    
    Esta função permite escolher entre diferentes métodos numéricos para
    encontrar raízes de funções reais.
    
    Parameters
    ----------
    f : callable
        Função da qual se deseja encontrar a raiz.
    a : float, optional
        Limite inferior do intervalo (necessário para bisseção e secante).
    b : float, optional
        Limite superior do intervalo (necessário para bisseção e secante).
    x0 : float, optional
        Aproximação inicial (necessário para Newton-Raphson).
    df : callable, optional
        Derivada da função (opcional para Newton-Raphson).
    tol : float, optional
        Tolerância para o critério de parada (padrão: 1e-6).
    max_iter : int, optional
        Número máximo de iterações (padrão: 100).
    max_raizes : int
        Número máximo de raízes a encontrar antes de interromper. (necessário para mult-bisseção)
    subdivisoes : int
        Número de divisões do intervalo para detectar mudanças de sinal. (necessário para mult-bisseção)
    method : str, optional
        Método a ser usado: "secante", "bissecao" ou "newton" (padrão: "bissecao").
    graf : bool, optional
        Se mostra o gráfico da função ou não.
    retornar_historico : bool, optional
        Se retorna o historico de pontos ou não.
    
    Returns
    -------
    float
        Aproximação da raiz da função.
    
    Raises
    ------
    ValueError
        Se os parâmetros necessários não forem fornecidos ou se o método for inválido.
    
    Exemplos
    --------
    >>> f = lambda x: x**3 - 9*x + 5
    >>> raiz_0 = raiz(f, a=0, b=2, tol=1e-6, method="bissecao")
    >>> print(f"{raiz_0:.3f}")
    0.586
    
    >>> # Usando Newton-Raphson
    >>> raiz_1 = raiz(f, x0=3, tol=1e-6, method="newton")
    >>> print(f"{raiz_1:.3f}")
    2.730
    """

    method = method.lower()
    
    if method in ["bissecao", "bisseção", "bisseccao", "bissecção", "bissec", "bisec", "bi", "b"]:
        if a is None or b is None:
            raise ValueError("O método da bisseção requer os parâmetros 'a' e 'b'.")
        return bissecao(f, a, b, tol, max_iter, graf=graf, retornar_historico=retornar_historico)
    
    elif method in ["secante", "sec", "s"]:
        if a is None or b is None:
            raise ValueError("O método da secante requer os parâmetros 'x0' e 'x1'.")
        return secante(f, a, b, tol, max_iter, graf=graf, retornar_historico=retornar_historico)

    elif method in ["newton", "raphson", "newton-raphson", "newtonraphson", "new", "n"]:
        if x0 is None:
            # Se não forneceu x_0, tenta usar o ponto médio de [a,b] se disponível
            if a is not None and b is not None:
                x0 = (a + b) / 2.0
            else:
                raise ValueError("O método de Newton-Raphson requer o parâmetro 'x0' "
                               "ou os parâmetros 'a' e 'b' para estimativa inicial.")
        return newton_raphson(f, x0, df, tol, max_iter, graf=graf, retornar_historico=retornar_historico)

    elif method in ["bisseção-multiraizes", "multbissecao", "mult-bissecao", "multbissec", "multbis", "multraizes", "mb"]:
        if a is None or b is None:
            raise ValueError("O método da bisseção de múltiplas raízes requer os parâmetros 'a' e 'b'.")
        return bissecao_multiraizes(f, a, b, tol, max_iter, max_raizes=max_raizes, subdivisoes=subdivisoes, graf=graf)
    
    else:
        raise ValueError(f"Método '{method}' não reconhecido. "
                        f"Use 'bissecao', 'multbissecao' 'secante' ou 'newton'.")
