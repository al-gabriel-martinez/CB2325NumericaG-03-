import numpy as np
import matplotlib.pyplot as plt
import math

def linear_interp(X_coord: list, Y_coord: list, plot: bool = True, title: str = ""):

  """
  Retorna uma função que interpola linearmente pontos definidos por coordenadas.

  A função gerada realiza interpolação linear entre pontos sucessivos
  de ``(X_coord, Y_coord)``.

  Parameters
  ----------
  X_coord : list of float
      Lista com as coordenadas dos pontos no eixo X.

  Y_coord : list of float
      Lista com as coordenadas dos pontos no eixo Y.
      Deve ter o mesmo comprimento de ``X_coord``.

  plot : bool, optional (default=True)
      Se True, exibe um gráfico do polinômio interpolador junto aos pontos.
      Caso False, apenas retorna a função interpoladora.

  title : str, optional (default='')
      Título do gráfico.

  Returns
  -------
  f : callable
      Função interpoladora ``f(t)` que retorna o
      valor interpolado em ``t`` (float ou np.array).

  Notes
  -----
  - Os pontos são automaticamente ordenados por suas coordenadas x.
  - Fora do intervalo definido pelos pontos, o comportamento é de extrapolação
    linear com base nos dois primeiros ou dois últimos pontos.
  - Utiliza ``matplotlib`` para plotar.
  """

  pontos = [(X_coord[i],Y_coord[i]) for i in range(len(X_coord))]
  pontos.sort()

  def f(t: float):
    """
    Avalia a interpolação linear definida por ``linear_interp()``.

    Parameters
    ----------
    t : float, array_like or str
        Valor(es) em que o polinômio será avaliado.
        Se ``t == "graf"``, o gráfico da função interpoladora será exibido.

    Returns
    -------
    float: Valor interpolado em ``t``.

    Notes
    -----
    Função interna de ``linear_interp()`` e utiliza a
    lista de pontos de interpolação fornecida a ela. 
    Fora do intervalo dos pontos, a interpolação é linearmente extrapolada.
    """

    # Calculando a imagem de t

    # Busca binária para descobrir em qual intervalo do eixo X o ponto t está.
    if t <= pontos[1][0]:
      pos = 0

    elif t >= pontos[-2][0]:
      pos = len(pontos)-2

    else:
      a = 0
      b = len(pontos)-2
      pos = (a+b)//2

      while a != b:
        if t < pontos[pos][0]:
          b = pos-1

        elif t <= pontos[pos+1][0]:
          break

        else:
          a = pos + 1
        pos = (a+b)//2

    # Retornando o valor da função.
    return pontos[pos][1] + (t-pontos[pos][0])*(pontos[pos+1][1]-pontos[pos][1])/(pontos[pos+1][0]-pontos[pos][0])

  # Plotagem da interpolação.

  if plot:
    # Intervalo do eixo X no gráfico.
    x = [x / 200 for x in range(int(200*pontos[0][0]) -1, int(200*pontos[-1][0]) + 1)]
    y = [f(x) for x in x]

    # Plotando a função
    plt.plot(x, y)

    # Plotando os pontos de interpolação.
    for p in pontos:
      plt.plot(p[0], p[1], marker='o', color='blue')

    plt.title(title)
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)

    plt.show()

  # Retornando a função.
  return f

def poly_interp(X, Y, method = "lagrange", plot = True, title = "" ):

  """
  Implementa métodos clássicos de interpolação polinomial.

  Esta função permite construir e avaliar polinômios interpoladores
  pelos métodos de Lagrange, Newton e Vandermonde, além de fornecer
  ferramentas gráficas para visualização dos resultados.

  Parameters
  ----------
  X : array_like
      Coordenadas dos pontos no eixo X.

  Y : array_like
      Coordenadas correspondentes no eixo Y.

  method : str, optional (default='lagrange')
      Determina qual método será utilizado para a
      construção do polinômio interpolador.

  plot : bool, optional (default=True)
      Se True, exibe um gráfico do polinômio interpolador junto aos pontos.
      Caso False, apenas retorna a função interpoladora.

  title : str, optional (default='')
      Título do gráfico.

  Returns
  ----------
  pol : callable
        Função que avalia polinômio interpolador em valores escalares ou arrays.

  Notas
  -----
  - Todos os métodos de interpolação produzem o mesmo polinômio teórico,
    embora possam diferir numericamente em estabilidade.
  - Requer `numpy` e `matplotlib`.
  """
  if not isinstance(X, (list, np.ndarray)) or not isinstance(Y, (list, np.ndarray)):
    raise TypeError
  if len(X) == 0 or len(Y) == 0:
    raise ValueError
  if len(X) != len(Y):
    raise ValueError
  if len(set(X)) < len(X):
    raise ValueError
  def verificar_valores(vetor):
    for valor in vetor:
        if not isinstance(valor, (int, float)):
            raise ValueError
  verificar_valores(X)
  verificar_valores(Y)

  # Converte listas em arrays NumPy (para operações vetorizadas)
  x = np.array(X, dtype=float)
  y = np.array(Y, dtype=float)
  n = len(x)

  # Método de Lagrange
  if method == "lagrange":
    def lagrange(ponto):

      """
        Avalia o polinômio interpolador pelo método de Lagrange.

        Parameters
        ----------
        ponto : array_like
            Ponto ou sequência de pontos nos quais o polinômio será avaliado.
            Pode ser um escalar ou um array/lista de valores.

        Returns
        -------
        p : ndarray
            Valores do polinômio interpolador avaliados em ``ponto``.

        Notes
        -----
        - O método constrói o polinômio de Lagrange explicitamente a partir dos pontos
        fornecidos em ``x`` e ``y``.
        - Este método é numericamente instável para conjuntos grandes de pontos.
        """

      if not isinstance(ponto, (list, np.ndarray,int, float)):
        raise TypeError
      if isinstance(ponto,(list,np.ndarray)):
        verificar_valores(ponto)
        
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
    pol = lagrange

  # Método de Newton
  if method == "newton":
    # Cálculo dos coeficientes do polinômio de Newton
    # (Diferenças divididas)
    coef = np.zeros((n, n))
    coef[:,0] = y  # primeira coluna recebe os valores y_i
    # Calcula as diferenças divididas
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
    # Retorna apenas a primeira linha (coeficientes do polinômio)
    coeficientes = coef[0, :]

    # Avaliação do polinômio de Newton em um ponto (ou vetor)
    def newton_eval(ponto):

      """
        Calcula os coeficientes do polinômio interpolador pelo método de Newton.

        Parameters
        ----------
        ponto : array_like
            Ponto ou sequência de pontos nos quais o polinômio será avaliado.
            Pode ser um escalar ou um array/lista de valores.

        Returns
        -------
        p : ndarray
            Valores do polinômio interpolador avaliados em ``ponto``.

        Notes
        -----
        - O método utiliza os coeficientes do polinômio calculados
        anteriormente com base na tabela de diferenças divididas,
        construída a partir dos pontos ``x`` e ``y``.
        - O polinômio resultante tem grau ``n - 1``.
        - A avaliação é feita usando o esquema de Horner modificado 
        para a forma de Newton, garantindo eficiência numérica.
        """

      if not isinstance(ponto, (list, np.ndarray,int, float)):
        raise TypeError
      if isinstance(ponto,(list,np.ndarray)):
        verificar_valores(ponto)
        
      ponto = np.array(ponto, dtype=float)
      k = len(coeficientes)
      p = np.zeros_like(ponto)
      # Avaliação pelo método de Horner generalizado
      for i in range(k-1, -1, -1):
          p = coeficientes[i] + (ponto - x[i]) * p
      return p
    pol = newton_eval

  # Método de Vandermonde
  if method == "vandermonde":
    # Resolve o sistema V * a = y, onde V é a matriz de Vandermonde
    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)

    # Avalia o polinômio definido pelos coeficientes de Vandermonde
    def eval_vandermonde(ponto):

      """
        Avalia o polinômio interpolador obtido pelo método de Vandermonde em um ou mais pontos.

        Parameters
        ----------
        ponto : array_like
            Valor ou sequência de valores nos quais o polinômio será avaliado.

        Returns
        -------
        p : ndarray
            Valores do polinômio interpolador avaliados em ``ponto``.

        Notes
        -----
        - O polinômio obtido é equivalente ao de Lagrange e Newton, mas o método 
        pode ser numericamente instável para alto número de pontos.
        - O cálculo é feito pela soma direta dos termos do polinômio.
        - A avaliação é feita usando o esquema de Horner modificado 
        para a forma de Vandermonde, garantindo eficiência numérica.
        """

      if not isinstance(ponto, (list, np.ndarray,int, float)):
        raise TypeError
      if isinstance(ponto,(list,np.ndarray)):
        verificar_valores(ponto)
      ponto = np.array(ponto, dtype=float)
      p = np.zeros_like(ponto)
      # Avalia o polinômio somando a_i * x^i
      for i, a in enumerate(coeficientes):
          p += a * ponto**i
      return p
    pol = eval_vandermonde

  # Plotando o Gráfico
  if plot:
    # Gera pontos igualmente espaçados para desenhar a curva
    x_plot = np.linspace(min(x), max(x), 200)
    y_plot = pol(x_plot)
    # Exibe os pontos conhecidos e o polinômio interpolador
    plt.scatter(x, y, color='blue', label='Pontos dados')
    plt.plot(x_plot, y_plot, label=f'Interpolação ({method})')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

  # Retornando o polinômio
  return pol

def hermite_interp(x: list, deriv: list, plot=True, title=""):
    """
    Cria e faz o plot do polinômio interpolador de Hermite.

    Parameters
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

    title : str, optional (default='')
        Título do gráfico.
        
    Returns
    -------
    H : callable
        Função que avalia polinômio interpolador em valores escalares ou arrays.

    Notes
    -----
    - O polinômio tem grau menor ou igual ao número total
      de derivadas fornecidas menos um.

    - Repetimos os nós conforme o número de derivadas associadas a ele.

    - Para cada derivada conhecida de ordem k, usamos f^(k)(xi) / k! 
      como entrada na tabela de diferenças divididas.

    - Demais entradas da tabela são calculadas usando 
      diferenças divididas convencionais.
    """
    deriv = [
    d if isinstance(d, (list, tuple, np.ndarray)) else [d]
    for d in deriv
    ]
    n = sum(len(d) for d in deriv)

    if len(x) != len(deriv):
       raise ValueError('O tamanho de x e das derivadas deve ser o mesmo!')
       

    # Vetor de pontos repetidos
    Z = np.zeros(n)

    # Tabela de diferenças divididas
    D = np.zeros((n, n))

    
    # Preenche Z e a primeira coluna de D
    
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

      Parameters
      ----------
      t : float or array_like
          Ponto ou conjunto de pontos onde o polinômio será avaliado.

      Returns
      -------
      float or ndarray
          Valor do polinômio em ``t``.
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
        plt.scatter(x, [d[0] for d in deriv], color='blue', zorder=5, label="Pontos")
        plt.title(title)
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        plt.grid(True)
        plt.legend()
        plt.show()
    
    return H


