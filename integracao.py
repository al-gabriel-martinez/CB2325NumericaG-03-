"""Aproximação de integrais por soma de Riemann (utilizando o ponto médio)."""

import math
import matplotlib.pyplot as plt

def integral(f, a, b, n):
    """Aproxima a integral definida ∫_a^b f(x) dx pela regra do ponto médio.

    A partição é uniforme em n subintervalos de largura delta_x = (b - a) / n.
    Em cada subintervalo [x_esq, x_dir], avalia-se a função no ponto médio
    x_med = (x_esq + x_dir) / 2.

    Parâmetros:
        f (callable): função escalar f(x) avaliável em float.
        a (float): extremidade esquerda do intervalo.
        b (float): extremidade direita do intervalo.
        n (int): número de subintervalos (inteiro positivo).

    Retorna:
        float: aproximação numérica de ∫_a^b f(x) dx.
    """
    a = float(a)
    b = float(b)
    delta_x = (b - a) / n
    soma = 0.0
    F = [f(a)]
    X = [a]

    def poligono(ponto, ponto2):
        x_vertices = [ponto[0],ponto2[0],ponto2[0],ponto[0]]
        y_vertices = [ponto[1],ponto2[1],0,0]
        plt.fill(x_vertices, y_vertices, color='skyblue', alpha=0.7)

    for i in range(n):
            x_esq = a + i * delta_x
            x_dir = x_esq + delta_x
            x_med = (x_esq + x_dir) / 2.0
            f_xm = f(x_med)
            F.append(f_xm)
            X.append(x_med)
            soma += f_xm
            poligono((x_esq,f_xm),(x_dir,f_xm))
    
    F.append(f(b))
    X.append(b)
    plt.plot(X,F)
    plt.title('Polígono Preenchido com fill()')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()

    return soma * delta_x


if __name__ == "__main__":
    
    f = lambda x: x**2
    g = lambda x: math.sin(x)
  
    area1 = integral(f, 0, 1, 4)
    print(area1)  
    area2 = integral(g, 0, math.pi, 100)
    print(area2)   