"""
Este módulo implementa interpolação de Hermite com base em diferenças divididas.
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def hermite_interp(x: list, deriv: list):
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
    
    Retorno
    -------
    H : callable
        Função que avalia polinômio interpolador em valores escalares ou arrays.

    
    Exemplos
    --------

    
    Notas
    -----
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
            if Z[i] != Z[i - j]:
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

"""
if __name__ == "__main__":
    pass
"""
