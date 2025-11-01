import matplotlib.pyplot as plt

def linear_interp(X_coord: list, Y_coord: list):
  '''
  A função recebe duas listas com as coordenadas x e y
  de alguns pontos e retorna uma função definida para
  todos os reais formada pelos segmentos de reta entre
  os pontos fornecidos.
  '''

  '''Ordenando as coordenadas dos pontos.'''
  pontos = [(X_coord[i],Y_coord[i]) for i in range(len(X_coord))]
  pontos.sort()

  def f(t, xi=0, xf=1, n=100, title=""):
    '''
    Essa função plota o seu gráfico se t=="graf" e retorna
    o valor esperado da função caso contrário. No caso em
    que t != "graf", apenas o primeiro parametro da função
    é utilizado.
    '''

    '''Plotando o gráfico da função.'''

    if t=="graf":
      '''Intervalo do eixo X no gráfico.'''
      x = [x / n for x in range(int(n*xi) -1, int(n*xf) + 1)]
      y = [f(x) for x in x]

      plt.plot(x, y)

      '''Plotando os pontos de interpolação.'''
      for p in pontos:
        plt.plot(p[0], p[1], marker='o', color='blue')

      plt.title(title)
      plt.xlabel("Eixo X")
      plt.ylabel("Eixo Y")
      plt.grid(True)

      plt.show()
      return


    '''Busca binária para descobrir em qual intervalo do eixo X o ponto t está.'''
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

    '''Retornando o valor da função.'''
    return pontos[pos][1] + (t-pontos[pos][0])*(pontos[pos+1][1]-pontos[pos][1])/(pontos[pos+1][0]-pontos[pos][0])

  '''Retornando a função.'''
  return f
