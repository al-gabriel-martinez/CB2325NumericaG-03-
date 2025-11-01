"""Aproximação de integrais por soma de Riemann (utilizando o ponto médio)."""

import math
import matplotlib.pyplot as plt

def integral(f, a, b, n, metodo = "trapezio"):
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

    #polígonos de 4 lados
    def poligono4(ponto, ponto2):
        x_vertices = [ponto[0],ponto2[0],ponto2[0],ponto[0]]
        y_vertices = [ponto[1],ponto2[1],0,0]                                                                                       
        plt.fill(x_vertices, y_vertices, color='skyblue', alpha=0.7)

    if metodo == 'trapezio':
        for i in range(n):
            x_esq = a + i * delta_x
            x_dir = x_esq + delta_x
            f_esq = f(x_esq)
            f_dir = f(x_dir)
            f_xm = (f_esq+f_dir)/2
            F.append(f_dir)
            X.append(x_dir)
            soma += f_xm * delta_x
            poligono4((x_esq,f_esq),(x_dir,f_dir))
    elif metodo == 'ponto_medio':
        for i in range(n):
            x_esq = a + i * delta_x
            x_dir = x_esq + delta_x
            x_med = (x_esq + x_dir) / 2.0
            f_xm = f(x_med)
            F.append(f_xm)
            X.append(x_med)
            soma += ( f(x_esq) + f_xm*4 + f(x_dir))/6 * delta_x
            poligono4((x_esq,f_xm),(x_dir,f_xm))

    elif metodo == 'simpson':
        for i in range(n):
            x_esq = a + i * delta_x
            x_dir = x_esq + delta_x
            x_med = (x_esq + x_dir) / 2.0

            f_esq = f(x_esq)
            f_dir = f(x_dir)
            f_xm = f(x_med)

            soma += (f_esq + 4.0*f_xm + f_dir) * (delta_x / 6.0)
         
            
    
    F.append(f(b))
    X.append(b)
    plt.plot(X,F)
    plt.title(f'Gráfico')
    plt.grid()
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.show()

    return soma 

if __name__ == "__main__":
    
    f = lambda x: x**2
    g = lambda x: math.sin(x)
  
    area1 = integral(f, 0, 1, 4)
    print("função f com metodo do trapezio", area1)  
    area2 = integral(g, 0, math.pi, 100)
    print("função g com metodo do trapezio", area2)  

    area3 = integral(f, 0, 1, 4, 'ponto_medio')
    print("função f com metodo do ponto medio", area3)  
    area4 = integral(g, 0, math.pi, 100, 'ponto_medio')
    print("função g com metodo do ponto medio", area4)    

    area5 = integral(f, 0, 1, 4, 'simpson')
    print("função f com metodo do simpson", area5)  
    area6 = integral(g, 0, math.pi, 100, 'simpson')
    print("função g com metodo do simpson", area6)    