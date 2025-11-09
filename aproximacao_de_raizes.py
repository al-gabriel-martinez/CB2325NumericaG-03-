"""
Módulo para cálculo de raízes de funções reais. Feito por: Anizio S. C. Júnior (aka AnZ)

Este módulo implementa métodos numéricos para encontrar raízes (zeros) de funções reais.
Implementações: Método da Bisseção e Método de Newton-Raphson.

É interessante notar que para funções com infinitas raizes em um intervalo finito, como 
a função f(x)=sen(1/x) no intervalo (0,1] é possível encontrar somente um zero dos infinitos 
com o método de bisseção, mas com o método de Newton-Raphson a aproximação é extremamente instável 
podendo divergir.
"""

def bissecao(f, a, b, tol=1e-6, max_iter=100, retornar_historico=False):
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
    
    Parâmetros
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
    
    Retorno
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
    
    for i in range(max_iter):
        # Calcula o ponto médio
        c = (a + b) / 2.0
        fc = f(c)
        historico.append(c)
        
        # Verifica convergência
        if abs(fc) < tol or (b - a) / 2.0 < tol:
            return (c, historico) if retornar_historico else c
        
        # Atualiza o intervalo
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    raise RuntimeError(f"Método da bisseção não convergiu após {max_iter} iterações.")


def newton_raphson(f, x0, df=None, tol=1e-6, max_iter=100, h=1e-8, retornar_historico=False):
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
    
    Parâmetros
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
    
    Retorno
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
        
        # Verifica convergência
        if abs(fx) < tol:
            return (x, historico) if retornar_historico else x
        
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

        # Verifica convergência da função
        if abs(fx) < tol:
            return (x, historico) if retornar_historico else x
        
        # Atualização de Newton
        x_new = x - fx / dfx
        historico.append(x_new)
        
        # Verifica convergência pela mudança em x
        if abs(x_new - x) < tol:
            return (x_new, historico) if retornar_historico else x_new
        
        x = x_new
    if retornar_historico:
        raise RuntimeError(f"Método não convergiu após {max_iter} iterações. Último x: {x:.6f}, histórico: {historico}")
    else:
        raise RuntimeError(f"Método de Newton-Raphson não convergiu após {max_iter} iterações.")

def raiz(f, a=None, b=None, x0=None, df=None, tol=1e-6, max_iter=100, method="bissecao", retornar_historico=False):
    """
    Interface unificada para encontrar raízes de funções.
    
    Esta função permite escolher entre diferentes métodos numéricos para
    encontrar raízes de funções reais.
    
    Parâmetros
    ----------
    f : callable
        Função da qual se deseja encontrar a raiz.
    a : float, optional
        Limite inferior do intervalo (necessário para bisseção).
    b : float, optional
        Limite superior do intervalo (necessário para bisseção).
    x0 : float, optional
        Aproximação inicial (necessário para Newton-Raphson).
    df : callable, optional
        Derivada da função (opcional para Newton-Raphson).
    tol : float, optional
        Tolerância para o critério de parada (padrão: 1e-6).
    max_iter : int, optional
        Número máximo de iterações (padrão: 100).
    method : str, optional
        Método a ser usado: "bissecao" ou "newton" (padrão: "bissecao").
    
    Retorno
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
        return bissecao(f, a, b, tol, max_iter, retornar_historico=retornar_historico)
    
    elif method in ["newton", "raphson", "newton-raphson", "newtonraphson", "new", "n"]:
        if x0 is None:
            # Se não forneceu x_0, tenta usar o ponto médio de [a,b] se disponível
            if a is not None and b is not None:
                x0 = (a + b) / 2.0
            else:
                raise ValueError("O método de Newton-Raphson requer o parâmetro 'x0' "
                               "ou os parâmetros 'a' e 'b' para estimativa inicial.")
        return newton_raphson(f, x0, df, tol, max_iter, retornar_historico=retornar_historico)
    
    else:
        raise ValueError(f"Método '{method}' não reconhecido. "
                        f"Use 'bissecao' ou 'newton'.")




# Retirar as aspas para ver os exemplos
"""
# Exemplo de uso sem histórico
if __name__ == "__main__":
    # Teste 1: Função do exemplo do documento
    f = lambda x: x**3 - 9*x + 5
    
    print("=" * 50)
    print("Teste 1: f(x) = x³ - 9x + 5")
    print("=" * 50)
    
    # Usando bisseção
    raiz_0 = raiz(f, a=0, b=2, tol=1e-6, method="bissecao")
    print(f"Raiz (bisseção, [0,2]): {raiz_0:.6f}")
    print(f"f({raiz_0:.6f}) = {f(raiz_0):.2e}")
    
    # Usando Newton-Raphson
    df = lambda x: 3*x**2 - 9
    raiz_1 = raiz(f, x0=1.0, df=df, tol=1e-6, method="newton")
    print(f"Raiz (Newton, x0=1.0): {raiz_1:.6f}")
    print(f"f({raiz_1:.6f}) = {f(raiz_1):.2e}")
    
    print()
    
    # Teste 2: x² - 4 = 0
    f2 = lambda x: x**2 - 4
    df2 = lambda x: 2*x
    
    print("=" * 50)
    print("Teste 2: f(x) = x² - 4")
    print("=" * 50)
    
    raiz_2 = raiz(f2, a=0, b=3, method="bissecao")
    print(f"Raiz (bisseção): {raiz_2:.6f}")
    print(f"f({raiz_2:.6f}) = {f2(raiz_2):.2e}")
    
    raiz_3 = raiz(f2, x0=1.0, df=df2, method="newton")
    print(f"Raiz (Newton): {raiz_3:.6f}")
    print(f"f({raiz_3:.6f}) = {f2(raiz_3):.2e}")
"""

'''
# Exemplo de uso com histórico
if __name__ == "__main__":
    # Teste com histórico
    f = lambda x: x**3 - 9*x + 5
    
    print("=" * 50)
    print("Teste com histórico")
    print("=" * 50)
    
    # Bisseção com histórico
    resultado_b = raiz(f, a=0, b=2, method="bissecao", retornar_historico=True)
    if isinstance(resultado_b, tuple):
        raiz_b, historico_b = resultado_b
    else:
        raiz_b, historico_b = resultado_b, [resultado_b]
    
    print(f"Raiz (bisseção): {raiz_b:.6f}")
    print(f"Histórico: {[f'{x:.6f}' for x in historico_b]}")
    print(f"Número de iterações: {len(historico_b)}")
    
    print()
    
    # Newton com histórico
    df = lambda x: 3*x**2 - 9
    resultado_n = raiz(f, x0=1.0, df=df, method="newton", retornar_historico=True)
    if isinstance(resultado_n, tuple):
        raiz_n, historico_n = resultado_n
    else:
        raiz_n, historico_n = resultado_n, [resultado_n]
    
    print(f"Raiz (Newton): {raiz_n:.6f}")
    print(f"Histórico: {[f'{x:.6f}' for x in historico_n]}")
    print(f"Número de iterações: {len(historico_n)}")
'''
