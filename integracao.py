"""Aproximação de integrais por soma de Riemann (utilizando o ponto médio)."""

import math
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

def poligono4(ponto, ponto2, *, cor='skyblue', alpha=0.7):
    x_vertices = [ponto[0], ponto2[0], ponto2[0], ponto[0]]
    y_vertices = [ponto[1], ponto2[1], 0,        0       ]
    plt.fill(x_vertices, y_vertices, color=cor, alpha=alpha)


def integral(f, a, b, n, plotar = True,metodo = "trapezio",suavidade = 500,cor_grafico = '#1f77b4',opacidade_grafico = 1,cor_area = 'skyblue',opacidade_area = 0.7,grade =True):
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

    F = []
    X = []

    tamanho_intervalo = abs(b-a)
    n_pontos_f = math.floor(tamanho_intervalo*suavidade)
    delta_x_funçao = (b-a)/n_pontos_f

    for i in range(n_pontos_f+1):
        x_i = a+i*delta_x_funçao
        X.append(x_i)
        F.append(f(x_i))

    if metodo == 'trapezio':
        for i in range(n):
            x_esq = a + i * delta_x
            x_dir = x_esq + delta_x
            f_esq = f(x_esq)
            f_dir = f(x_dir)
            f_xm = (f_esq+f_dir)/2
            soma += f_xm * delta_x
            if plotar:
                poligono4((x_esq, f_esq), (x_dir, f_dir),cor=cor_area, alpha=opacidade_area)
    elif metodo == 'ponto_medio':
        for i in range(n):
            x_esq = a + i * delta_x
            x_dir = x_esq + delta_x
            x_med = (x_esq + x_dir) / 2.0
            f_xm = f(x_med)
            soma += f_xm * delta_x
            if plotar:
                poligono4((x_esq, f_xm), (x_dir, f_xm),cor=cor_area, alpha=opacidade_area)

    elif metodo == 'simpson':
        for i in range(n):
            x_esq = a + i * delta_x
            x_dir = x_esq + delta_x
            x_med = (x_esq + x_dir) / 2.0

            f_esq = f(x_esq)
            f_dir = f(x_dir)
            f_xm = f(x_med)
            
            if plotar:
                x_pontos = np.array([x_esq,x_med,x_dir])
                y_pontos = np.array([f_esq,f_xm,f_dir])

                a_p,b_p,c_p = np.polyfit(x_pontos,y_pontos,2)
                g = lambda t: a_p*t**2+b_p*t+c_p 
                n_pontos_g = math.floor(delta_x*suavidade)

                X_G = np.linspace(x_esq, x_dir, n_pontos_g)
                G = g(X_G)

                plt.fill_between(X_G, G, color=cor_area, alpha=opacidade_area)

            soma += (f_esq + 4.0*f_xm + f_dir) * (delta_x / 6.0)
         
            
    if plotar:
        plt.plot(X,F,color = cor_grafico,alpha=opacidade_grafico)
        plt.title(f'Gráfico da função')
        if grade:
            plt.grid()
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.show()

    return soma 

if __name__ == "__main__":
    
    f = lambda x: x**2
    g = lambda x: math.sin(x)
  
    area1 = integral(g, 0, 1, 4,metodo='simpson',cor_area="purple",grade=False,opacidade_area=0.3)
    print("função f com metodo do trapezio", area1)  
    area2 = integral(g, 0, math.pi, 100,plotar=False)
    print("função g com metodo do trapezio", area2)  

    area3 = integral(f, 0, 1, 4, 'ponto_medio')
    print("função f com metodo do ponto medio", area3)  
    area4 = integral(g, 0, math.pi, 100, 'ponto_medio')
    print("função g com metodo do ponto medio", area4)  

    area5 = integral(f, 0, 1, 4, 'simpson',cor_grafico='black',cor_area='red',opacidade_area=0.3)
    print("função f com metodo do simpson", area5)  
    area6 = integral(g, 0, math.pi, 100)
    print("função g com metodo do simpson", area6)  