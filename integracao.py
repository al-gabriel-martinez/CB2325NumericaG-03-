"""Aproximação de integrais por soma de Riemann (utilizando o ponto médio)."""

import math

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

    for i in range(n):
        x_esq = a + i * delta_x
        x_dir = x_esq + delta_x
        x_med = (x_esq + x_dir) / 2.0
        soma += f(x_med)

    return soma * delta_x


if __name__ == "__main__":
    
    f = lambda x: x**2
    g = lambda x: math.sin(x)
  
    area1 = integral(f, 0, 1, 4)
    print(area1)  
    area2 = integral(g, 0, math.pi, 100)
    print(area2)   