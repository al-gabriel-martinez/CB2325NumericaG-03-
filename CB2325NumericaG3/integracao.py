"""Métodos numéricos de integração: trapézio, ponto médio e Simpson, com visualização."""

import math
import matplotlib.pyplot as plt
import numpy as np

def poligono4(ponto, ponto2, *, cor='skyblue', alpha=0.7):
    
    """
    Preenche um quadrilátero com base em y=0 entre duas abscissas.

    Desenha um polígono de 4 lados cuja base está em y=0, com vértices
    x = ponto[0] e x = ponto2[0], e topos em y = ponto[1] e y = ponto2[1].

    Parametres:
      ponto : tuple 
        (x_esq, y_esq).

      ponto2 : tuple
        (x_dir, y_dir).

      cor : string
        Cor do preenchimento.

      alpha : float 
        Opacidade do preenchimento.
    """

    x_vertices = [ponto[0], ponto2[0], ponto2[0], ponto[0]]
    y_vertices = [ponto[1], ponto2[1], 0,        0       ]
    plt.fill(x_vertices, y_vertices, color=cor, alpha=alpha)


def integral(f, a, b, n, plotar = True, metodo = "trapezio", suavidade = 500, cor_grafico = '#1f77b4', opacidade_grafico = 1, cor_area = 'skyblue', opacidade_area = 0.7, grade =True):
    
    """
    Aproxima ∫_a^b f(x) dx por trapézio, ponto_medio ou simpson.

    A partição é uniforme: delta_x = (b - a) / n. Para 'plotar=True',
    a função é amostrada com 'suavidade' pontos por unidade de comprimento.

    Parametres:
      f : callable
        Função escalar (f(x) -> float).

      a : float
        Extremo esquerdo do intervalo.

      b : float
        Extremo direito do intervalo.

      n : int
        Número de subintervalos.

      plotar : bool, optional 
        Se True, desenha função e áreas aproximadas.

      metodo : string, optional
        'trapezio', 'ponto_medio' ou 'simpson'.

      suavidade : int, optional
        Densidade de pontos p/ desenhar a curva (plot).

      cor_grafico : string, optional
        Cor da curva f(x).

      opacidade_grafico : float, optional
        Opacidade da curva f(x).

      cor_area : string, optional
        Cor do preenchimento das áreas.

      opacidade_area : float, optional
        Opacidade do preenchimento das áreas.

      grade : bool, optional
        Se True, exibe grade no gráfico.

    Returns:
      soma : float 
        Aproximação numérica de ∫_a^b f(x) dx.
    """
    if not callable(f):
      raise TypeError("O argumento 'funcao' deve ser uma função chamável (callable).")
    
    try:
        # Testa se a função pode ser avaliada
        teste = f((a + b) / 2)
    except Exception:
        raise TypeError("A função fornecida não pôde ser avaliada.")

    # Checa se o retorno é válido
    if isinstance(teste, complex):
        raise TypeError("A função retornou valor complexo, o que não é suportado.")

    if math.isnan(teste):
        raise TypeError("A função retornou NaN, o que não é permitido.")

    if math.isinf(teste):
        raise OverflowError("A função retornou infinito, o que não é permitido.")
        # Conversão e validação dos limites
    try:
      a = float(a)
      b = float(b)
    except Exception:
      raise TypeError("Os limites de integração devem ser números reais.")
    
    # Casos de borda: NaN e infinito
    if any(math.isnan(x) for x in [a, b]):
      raise TypeError("Limites de integração não podem ser NaN.")
    
    if any(math.isinf(x) for x in [a, b]):
      raise OverflowError("Limites infinitos não são suportados.")
    
    # Validação de partições
    if not isinstance(n, (int, np.integer)) or n <= 0:
      raise TypeError("O número de partições deve ser um inteiro positivo.")
    
    if a == b:
      return 0

    if metodo not in ['trapezio', 'simpson', 'ponto_medio']:
      raise NameError('O método deve ser trapezio, simpson ou ponto_medio')
    
    delta_x = (b - a) / n
    soma = 0.0
    tamanho_intervalo = abs(b-a)
    n_pontos_f = max(1, round(tamanho_intervalo*suavidade))
    delta_x_funçao = (b-a)/n_pontos_f

    F = []
    X = []

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
        plt.plot(X,F,color = cor_grafico, alpha=opacidade_grafico)
        plt.title(f'Gráfico da função abaixo')
        if grade:
            plt.grid()
        plt.xlabel('Eixo X')
        plt.ylabel('Eixo Y')
        plt.show()

    return soma 