import numpy as np
import matplotlib.pyplot as plt
# Método de Lagrange
def lagrange(x, y, ponto):
    n = len(x)
    # Converte listas em arrays NumPy (para operações vetorizadas)
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    ponto = np.array(ponto, dtype=float)
    # Vetor de zeros onde serão armazenados os valores do polinômio P(x)
    p = np.zeros_like(ponto)
    # Loop principal — percorre cada ponto conhecido
    for i in range(n):
        # Inicializa o polinômio básico de Lagrange L_i(x)
        L = np.ones_like(ponto)
        for j in range(n):
            if j != i:  # evita divisão por zero no termo (x_i - x_j)
                L *= (ponto - x[j]) / (x[i] - x[j])
        # Soma o termo y_i * L_i(x) ao resultado final
        p += y[i] * L
    return p
# Cálculo dos coeficientes do polinômio de Newton
# (Diferenças divididas)
def newton_coef(x, y):
    n = len(x)
    coef = np.zeros((n, n))
    coef[:,0] = y  # primeira coluna recebe os valores y_i
    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    # Retorna apenas a primeira linha (coeficientes do polinômio)
    coeficientes = coef[0, :]
    return coeficientes
# Avaliação do polinômio de Newton em um ponto (ou vetor)
def newton_eval(x, y, ponto, coeficientes=None):
    n = len(x)
    # Se os coeficientes não foram fornecidos, calcula
    if coeficientes is None:
        coeficientes = newton_coef(x, y)
    ponto = np.array(ponto, dtype=float)
    a = coeficientes
    k = len(a)
    p = np.zeros_like(ponto)
    # Avaliação pelo método de Horner generalizado
    for i in range(k-1, -1, -1):
        p = a[i] + (ponto - x[i]) * p
    return p
# Método de Vandermonde
# Resolve o sistema V * a = y, onde V é a matriz de Vandermonde
def vandermonde(x, y):
    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)
    return coeficientes
# Avalia o polinômio definido pelos coeficientes de Vandermonde
def eval_vandermonde(x, y, ponto, coeficientes=None):
    if coeficientes is None:
        coeficientes = vandermonde(x, y)
    ponto = np.array(ponto, dtype=float)
    p = np.zeros_like(ponto)
    # Avalia o polinômio somando a_i * x^i
    for i, a in enumerate(coeficientes):
        p += a * ponto**i
    return p
# Função genérica para plotar o polinômio interpolador
def plot(x, y, x_plot, metodo:str, num_pontos=200):
    # Gera pontos igualmente espaçados para desenhar a curva
    x_plot = np.linspace(min(x), max(x), num_pontos)
    # Escolhe o método de interpolação
    if metodo == 'lagrange':
        y_plot = lagrange(x, y, x_plot)
    elif metodo == 'newton':
        y_plot = newton_eval(x, y, x_plot, coeficientes=None)
    else:
        y_plot = eval_vandermonde(x, y, x_plot, coeficientes=None)
    # Exibe os pontos conhecidos e o polinômio interpolador
    plt.scatter(x, y, color='red', label='Pontos dados')
    plt.plot(x_plot, y_plot, label=f'Interpolação ({metodo})')
    plt.legend()
    plt.grid()
    plt.show()



