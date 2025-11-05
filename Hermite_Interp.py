"""
Este módulo implementa interpolação de Hermite com base em diferenças divididas.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def hermite_interp(x: list, deriv: list, plot=True):
    """
    Cria e faz o plot do polinômio interpolador de Hermite.

    Parâmetros
    ----------
    x : list
        Lista com as coordenadas dos pontos no eixo X.

    deriv : list of lists 
        Lista cujos elementos são listas contendo os valores da função
        e uma quantia indeterminada de derivadas sucessivas no ponto
        correspondente em 'x'.

    plot : bool, optional (default=True)
        Se True, exibe um gráfico do polinômio interpolador junto aos pontos.
        Caso False, apenas retorna a função interpoladora.
    
    Retorno
    -------
    H : callable
        Função que avalia polinômio interpolador em valores escalares ou arrays.

    Notas
    -----
    - O polinômio tem grau menor ou igual ao número total
      de derivadas fornecidas menos um.

    - Repetimos os nós conforme o número de derivadas associadas a ele.

    - Para cada derivada conhecida de ordem k, usamos f^(k)(xi) / k! 
      como entrada na tabela de diferenças divididas.

    - Demais entradas da tabela são calculadas usando 
      diferenças divididas convencionais.
    """

    n = sum(len(d) for d in deriv)

    # Vetor de pontos repetidos
    Z = np.zeros(n)

    # Tabela de diferenças divididas
    D = np.zeros((n, n))

    """
    Preenche Z e a primeira coluna de D
    """
    row = 0
    for x_i, d_i in zip(x, deriv):
        m = len(d_i)    # Quantidade de derivadas nesse ponto
        for j in range(m):
            Z[row] = x_i
            D[row, 0] = d_i[0]  # Valor da função em x_i

            # Preenche derivadas conhecidas
            for k in range(1, j + 1):
                D[row, k] = d_i[k] / math.factorial(k)
            row += 1

    # Diferenças divididas normais
    for j in range(1, n):
        for i in range(j, n):
            if Z[i] != Z[i - j]:    # Pontos repetidos já foram preenchidos
                D[i][j] = (D[i][j-1] - D[i-1][j-1]) / (Z[i] - Z[i-j])

    # Coeficientes do polinômio (diagonal principal da tabela)
    coeff = [D[i][i] for i in range(n)] 

    def H(t):
        """
        Avalia o polinômio de Hermite em t.

        Parâmetros
        ----------
        t : float ou list
        
        Retorno
        -------
        float ou np.array
            Valor do polinômio em t.
        
        Exemplos
        --------

        
        Notas
        -----
        """
        if isinstance(t, (int, float)):
            result = 0
            for k in range(len(coeff)-1, -1, -1):
                result = result * (t - Z[k]) + coeff[k]
            return result
        else:
            return np.array([H(x_i) for x_i in t])

    # Plot do dos pontos e o polinômio interpolador
    if plot:
        if min(x) == max(x):    # Caso onde só é dado um ponto
            x_plot = np.linspace(x[0] - 1, x[0] + 1, 200)
        else:
            x_plot = np.linspace(min(x), max(x), 200)
        y_plot = H(x_plot)

        plt.figure(figsize=(7,5))
        plt.plot(x_plot, y_plot, label="Polinômio de Hermite", color='blue')
        plt.scatter(x, [d[0] for d in deriv], color='red', zorder=5, label="Pontos")
        plt.title("Interpolação de Hermite")
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        plt.grid(True)
        plt.legend()
        plt.show()
    
    return H

# Retirar as aspas para ver os exemplos
'''
if __name__ == "__main__":
    print("\n Exemplo 1: Apenas valores (caso Lagrange), f(x)=x²")

    x = [0, 1, 2]
    deriv = [
        [0],   # f(0) = 0
        [1],   # f(1) = 1
        [4]    # f(2) = 4
    ]

    H = hermite_interp(x, deriv, plot=False)

    # Testando um ponto intermediário
    print("H(1.5) =", H(1.5), "| esperado =", 1.5**2)
    input()

    print("\n Exemplo 2: Com derivada, f(x)=e^x")
    """ 
    Interpola f(x)=e^x em x=0 sabendo f(0) e f'(0)
    """

    x2 = [0]
    deriv2 = [
        [1, 1],   # f(0) = 1, f'(0) = 1
    ]

    H2 = hermite_interp(x2, deriv2, plot=True)
    print("H2(0.5) ≈", H2(0.5), "| esperado =", f'{np.exp(0.5):.2f}')
    input()

    print("\n Exemplo 3: múltiplas derivadas")
    print("f(0)=1, f(0)=0, f(0)=-2"+'\n'+"f(1)=-1, f(1)=3, f(1)=1"+'\n'+"f(2)=0, f'(2)=2")
    x3 = [0, 1, 2]
    deriv3 = [
        [1, 0, -2],       # f(0)=1, f(0)=0, f(0)=-2
        [-1, 3, 1],       # f(1)=-1, f(1)=3, f(1)=1
        [0, 2]            # f(2)=0, f'(2)=2
    ]
    H3 = hermite_interp(x3, deriv3, plot=True)
    input()

    print("\n Exemplo 4: f(x)=cos(2x)")
    """ 
    Interpola f(x) = cos(2x)
    """
    x4 = [0, np.pi/3, np.pi/2]
    deriv4 = [
        [1, 0],                     # cos(2*0)=1, -2sin(2*0)=0
        [-0.5, -1*np.sqrt(3)],      # cos(2π/3)=-0.5, -2sin(2π/3)≈-1,73
        [-1, 0],                    # cos(π)=-1, -2sin(π)=0
    ]
    H4 = hermite_interp(x4, deriv4, plot=True)
    print("Cos(π/2) ≈", f'{H4(np.pi/4):.5f}') # cos(π/2) = 0
'''
