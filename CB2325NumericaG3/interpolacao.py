import numpy as np
import matplotlib.pyplot as plt
import math

def hermite_interp(x: list, deriv: list, plot=True):

  """
  Cria e faz o plot do polinômio interpolador de Hermite.

  Parameters
  ----------
  x : list
      Lista com as coordenadas dos pontos no eixo X.

  deriv : list of lists 
      Lista cujos elementos são listas contendo os valores da função
      e uma quantia indeterminada de derivadas sucessivas no ponto
      correspondente em ``x``.

  plot : bool, optional (default=True)
      Se True, exibe um gráfico do polinômio interpolador junto aos pontos.
      Caso False, apenas retorna a função interpoladora.
  
  Returns
  -------
  H : callable
      Função que avalia o polinômio interpolador em valores escalares ou arrays.

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

  n = sum(len(d) for d in deriv)

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
    plt.scatter(x, [d[0] for d in deriv], color='red', zorder=5, label="Pontos")
    plt.title("Interpolação de Hermite")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.legend()
    plt.show()
  
  return H


def linear_interp(X_coord: list, Y_coord: list):

  """
  Retorna uma função que interpola linearmente pontos definidos por coordenadas.

  A função gerada realiza interpolação linear entre pontos sucessivos
  de ``(X_coord, Y_coord)``. Também pode plotar o gráfico da função interpoladora
  quando chamada com o argumento ``t="graf"``.

  Parameters
  ----------
  X_coord : list of float
      Lista com as coordenadas dos pontos no eixo X.

  Y_coord : list of float
      Lista com as coordenadas dos pontos no eixo Y.
      Deve ter o mesmo comprimento de ``X_coord``.

  Returns
  -------
  f : callable
      Função interpoladora tal que:
      - ``f(t)`` retorna o valor interpolado em ``t`` (float ou np.array).
      - ``f("graf")`` plota o gráfico da função no intervalo definido.

  Notes
  -----
  - Os pontos são automaticamente ordenados por suas coordenadas x.
  - Fora do intervalo definido pelos pontos, o comportamento é de extrapolação
    linear com base nos dois primeiros ou dois últimos pontos.
  - Utiliza ``matplotlib`` para plotar.
  """

  pontos = [(X_coord[i],Y_coord[i]) for i in range(len(X_coord))]
  pontos.sort()

  def f(t, xi=0, xf=1, n=100, title=""):

    """
    Avalia ou plota a interpolação linear definida por ``linear_interp()``.

    Parameters
    ----------
    t : float, array_like or str
        Valor(es) em que o polinômio será avaliado.
        Se ``t == "graf"``, o gráfico da função interpoladora será exibido.

    xi : float, optional
        Limite inferior do intervalo do gráfico. O padrão é 0.

    xf : float, optional
        Limite superior do intervalo do gráfico. O padrão é 1.

    n : int, optional
        Número de subdivisões no eixo X ao plotar. O padrão é 100.

    title : str, optional
        Título do gráfico exibido. O padrão é string vazia.

    Returns
    -------
    float or None
        Valor interpolado em ``t`` quando ``t`` for numérico.
        Retorna ``None`` se ``t == "graf"``.

    Notes
    -----
    Função interna de ``linear_interp()`` e utiliza a
    lista de pontos de interpolação fornecida a ela. 
    Fora do intervalo dos pontos, a interpolação é linearmente extrapolada.
    """

    # Plotando o gráfico da função.

    if t=="graf":
      # Intervalo do eixo X no gráfico.
      x = [x / n for x in range(int(n*xi) -1, int(n*xf) + 1)]
      y = [f(x) for x in x]

      plt.plot(x, y)

      # Plotando os pontos de interpolação.
      for p in pontos:
        plt.plot(p[0], p[1], marker='o', color='blue')

      plt.title(title)
      plt.xlabel("Eixo X")
      plt.ylabel("Eixo Y")
      plt.grid(True)

      plt.show()
      return

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

  # Retornando a função.
  return f


class InterpolacaoPolinomial:

    """
    Implementa métodos clássicos de interpolação polinomial.

    Esta classe permite construir e avaliar polinômios interpoladores
    pelos métodos de Lagrange, Newton e Vandermonde, além de fornecer
    ferramentas gráficas para visualização dos resultados.

    Parameters
    ----------
    x : array_like
        Coordenadas dos pontos no eixo X.
    y : array_like
        Coordenadas correspondentes no eixo Y.

    Attributes
    ----------
    x : ndarray
        Coordenadas dos pontos no eixo X convertidas para `numpy.ndarray`.
    y : ndarray
        Coordenadas dos pontos no eixo Y convertidas para `numpy.ndarray`.
    n : int
        Número de pontos fornecidos.
    coeficientes : ndarray or None
        Coeficientes do polinômio interpolador. Inicialmente `None`.

    Notas
    -----
    - Todos os métodos de interpolação produzem o mesmo polinômio teórico,
      embora possam diferir numericamente em estabilidade.
    - Requer `numpy` e `matplotlib`.
    """

    def __init__(self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.n = len(x)
        self.coeficientes = None                        # a_i do polinômio interpolador
    

    def lagrange(self, ponto):
    
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
        fornecidos em ``self.x`` e ``self.y``.
        - Este método é numericamente instável para conjuntos grandes de pontos.
        """

        ponto = np.array(ponto, dtype=float)            # Transforma os pontos onde queremos avaliar o polinômio em ndarray
        n = self.n                                      # Número de pontos conhecidos
        x, y = self.x, self.y                           # Pega os vetores x e y originais
        p = np.zeros_like(ponto)                        # Cria vetor de zeros p, que vai guardar P(x_eval)
    
        for i in range(n):                       
            L = np.ones_like(ponto)                     # Inicia L_i(x) = 1 (vai multiplicar fatores)
        for j in range(n):                              # Para cada outro ponto j
            if j != i:                                  # Pula o caso j = i
                L *= (ponto - x[j]) / (x[i] - x[j])     # Multiplica pelos termos do produto
        p += y[i] * L                                   # Soma y_i * L_i(x) ao resultado final
        return p
    

    def newton_coef(self):
        """
        Calcula os coeficientes do polinômio interpolador pelo método de Newton.

        Returns
        -------
        self.coeficientes : ndarray
            Array contendo os coeficientes do polinômio de Newton obtidos por 
            diferenças divididas. Os coeficientes serão armazenados em ``self.coeficientes``.

        Notes
        -----
        - O cálculo é baseado na tabela de diferenças divididas, construída a partir
        dos pontos ``self.x`` e ``self.y``.
        - O polinômio resultante tem grau ``self.n - 1``.
        - Esse método deve ser executado antes de ``newton_eval()``, pois ela depende
        dos coeficientes aqui gerados.
        """

        n = self.n                                      
        x, y = self.x.copy(), self.y.copy()             
        coef = np.zeros((n, n))
        coef[:,0] = y
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i+1][j-1] - 
                              coef[i][j-1]) / (x[i+j] - x[i])
        self.coeficientes = coef[0, :]
        return self.coeficientes
    
    
    def newton_eval(self, ponto):
        """
        Avalia o polinômio interpolador pelo método de Newton.

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
        - O método utiliza os coeficientes calculados por ``newton_coef()`` 
        e os nós armazenados em ``self.x``.
        - Caso os coeficientes ainda não tenham sido gerados, 
        ``newton_coef()`` é chamado automaticamente.
        - A avaliação é feita usando o esquema de Horner modificado 
        para a forma de Newton, garantindo eficiência numérica.
        """
                  
        if self.coeficientes is None:
            self.newton_coef()
        ponto = np.array(ponto, dtype=float)
        x = self.x
        a = self.coeficientes
        n = len(a)
        p = np.zeros_like(ponto)
        for k in range(n-1, -1, -1):
            p = a[k] + (ponto - x[k]) * p
        return p

    
    def vandermonde(self):
        """
        Calcula os coeficientes do polinômio interpolador usando o sistema de Vandermonde.

        Returns
        -------
        self.coeficientes : ndarray
            Array contendo os coeficientes do polinômio interpolador obtidos
            a partir da resolução do sistema linear de Vandermonde. Os coeficientes
            serão armazenados em ``self.coeficientes``

        Notes
        -----
        - O método constrói a matriz de Vandermonde com os pontos ``self.x`` 
        e resolve o sistema linear ``V * a = y`` para determinar os coeficientes.
        - O polinômio obtido é equivalente ao de Lagrange e Newton, mas o método 
        pode ser numericamente instável para alto número de pontos.
        """

        V = np.vander(self.x, increasing=True)
        self.coeficientes = np.linalg.solve(V, self.y)
        return self.coeficientes

    
    
    def vandermonde_eval(self, ponto):

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
        - Caso os coeficientes não tenham sido previamente calculados, o método
        ``vandermonde()`` é chamado automaticamente.
        - O cálculo é feito pela soma direta dos termos do polinômio.
        - A avaliação é feita usando o esquema de Horner modificado 
        para a forma de Vandermonde, garantindo eficiência numérica.
        """

        if self.coeficientes is None:
            self.vandermonde()
        ponto = np.array(ponto, dtype=float)
        p = np.zeros_like(ponto)
        for a in self.coeficientes[::-1]:
            p = a + ponto * p

        return p

    
    
    def plot(self, metodo='lagrange', num_pontos=200):

        """
        Plota o polinômio interpolador junto com os pontos originais.

        Parameters
        ----------
        metodo : {'lagrange', 'newton', 'vandermonde'}, default='lagrange'
            Método de interpolação a ser utilizado para gerar o polinômio.
        num_pontos : int, default=200
            Número de pontos usados para gerar a curva suave do gráfico.

        Notes
        -----
        - Os pontos originais ``(self.x, self.y)`` são mostrados em vermelho.
        - A curva do polinômio interpolador é desenhada conforme o método escolhido.
        - Requer ``matplotlib`` para plotar.
        """

        x_plot = np.linspace(min(self.x), max(self.x), num_pontos)
        if metodo == 'lagrange':
            y_plot = self.lagrange(x_plot)
        elif metodo == 'newton':
            y_plot = self.newton_eval(x_plot)
        else:
            y_plot = self.vandermonde_eval(x_plot)
        plt.scatter(self.x, self.y, color='red', label='Pontos dados')
        plt.plot(x_plot, y_plot, label=f'Interpolação ({metodo})')
        plt.legend()
        plt.grid()
        plt.show()