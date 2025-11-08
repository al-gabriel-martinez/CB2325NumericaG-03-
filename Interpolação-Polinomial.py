import numpy as np
import matplotlib.pyplot as plt
class InterpolacaoPolinomial:
    def __init__(self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.n = len(x)
        self.coeficientes = None   # a_i do polinômio interpolador
    def lagrange(self, ponto):
        ponto = np.array(ponto, dtype=float)   # transforma os pontos onde queremos avaliar o polinômio em array NumPy
        n = self.n                               # número de pontos conhecidos
        x, y = self.x, self.y                    # pega os vetores x e y originais
        p = np.zeros_like(ponto)             # cria vetor de zeros p, que vai guardar P(x_eval)
        for i in range(n):                       # para cada ponto i conhecido
            L = np.ones_like(ponto)             # começa L_i(x) = 1 (vai multiplicar fatores)
            for j in range(n):                   # para cada outro ponto j
                if j != i:                       # mas pula o caso j = i
                    L *= (ponto - x[j]) / (x[i] - x[j])  # multiplica pelos termos do produto
            p += y[i] * L                                   # soma y_i * L_i(x) ao resultado final
        return p
    def newton_coef(self):
        n = self.n #número de pontos conhecidos
        x, y = self.x.copy(), self.y.copy() #copia os vetores x e y originais
        coef = np.zeros((n, n))
        coef[:,0] = y
        for j in range(1, n):
            for i in range(n - j):
                coef[i][j] = (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j] - x[i])
        self.coeficientes = coef[0, :]
        return self.coeficientes
    def newton_eval(self, ponto):
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
        V = np.vander(self.x, increasing=True)
        self.coeficientes = np.linalg.solve(V, self.y)
        return self.coeficientes
    def eval_vandermonde(self, ponto):
        if self.coeficientes is None:
            self.vandermonde()
        ponto = np.array(ponto, dtype=float)
        p = np.zeros_like(ponto)
        for i, a in enumerate(self.coeficientes):
            p += a * ponto**i
        return p
    def plot(self, metodo='lagrange', num_pontos=200):
        x_plot = np.linspace(min(self.x), max(self.x), num_pontos)
        if metodo == 'lagrange':
            y_plot = self.lagrange(x_plot)
        elif metodo == 'newton':
            y_plot = self.newton_eval(x_plot)
        else:
            y_plot = self.eval_vandermonde(x_plot)
        plt.scatter(self.x, self.y, color='red', label='Pontos dados')
        plt.plot(x_plot, y_plot, label=f'Interpolação ({metodo})')
        plt.legend()
        plt.grid()
        plt.show()

