"""
Módulo para cálculo de raízes de funções reais. Feito por: Anizio S. C. Júnior

Este módulo implementa métodos numéricos para encontrar raízes (zeros) de funções reais.
Implementações: Método da Bisseção e Método de Newton-Raphson.

É interessante notar que para funções com infinitas raizes em um intervalo finito, como 
a função f(x)=sen(1/x) é possível encontrar somente um zero dos infinitos com o método de 
bisseção, mas com o método de Newton-Raphson a aproximação é extremamente instável podendo 
divergir.
"""

def raiz(f, a=None, b=None, x0=None, df=None, tol=1e-6, max_iter=100, method="bissecao"):
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
        return bissecao(f, a, b, tol, max_iter)
    
    elif method in ["newton", "raphson", "newton-raphson", "newtonraphson", "new", "n"]:
        if x0 is None:
            # Se não forneceu x0, tenta usar o ponto médio de [a,b] se disponível
            if a is not None and b is not None:
                x0 = (a + b) / 2.0
            else:
                raise ValueError("O método de Newton-Raphson requer o parâmetro 'x0' "
                               "ou os parâmetros 'a' e 'b' para estimativa inicial.")
        return newton_raphson(f, x0, df, tol, max_iter)
    
    else:
        raise ValueError(f"Método '{method}' não reconhecido. "
                        f"Use 'bissecao' ou 'newton'.")

# Retirar aspas caso queira ver os exemplos
"""
# Exemplo de uso
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
