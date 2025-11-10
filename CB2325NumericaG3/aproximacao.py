import numpy as np
import matplotlib.pyplot as plt


def _validar_pontos_2xn(pontos):
    """
    Garante que pontos tenha exatamente duas linhas.
    Aceita lista de listas ou ndarray de forma (2, N).
    """
    arr = np.asarray(pontos, dtype=float)
    if arr.ndim != 2:
        raise ValueError("pontos deve ser bidimensional no formato 2 x N")
    if arr.shape[0] != 2:
        raise ValueError("pontos deve ter exatamente duas linhas, uma para x e outra para y")
    return arr[0], arr[1]


def aproximacao_polinomial_mq(pontos, grau: int, plotar: bool = False):
    """
    Ajuste polinomial por minimos quadrados usando apenas NumPy.
    """
    x, y = _validar_pontos_2xn(pontos)
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    if x.size != y.size:
        raise ValueError("pontos deve ter duas linhas com o mesmo numero de colunas")

    if grau < 0:
        raise ValueError("grau deve ser inteiro nao negativo")

    X = np.vander(x, N=grau + 1, increasing=False)
    alpha_desc = np.linalg.lstsq(X, y, rcond=None)[0]

    if plotar:
        n_grid = max(100, int(round(max(x) - min(x)) * 100))
        x_pred = np.linspace(min(x), max(x), n_grid)
        y_pred = np.polyval(alpha_desc, x_pred)

        plt.scatter(x, y, label="dados", s=30)
        plt.plot(x_pred, y_pred, label="polinomio", linewidth=2)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

    return alpha_desc


def aproximacao_polinomial_aleatoria(
    pontos,
    grau: int,
    expoente: int = 3,
    intervalo=(0.0, 1.0),
    seed=None,
    plotar: bool = False,
):
    """
    Busca aleatoria de coeficientes polinomiais para aproximar os dados.
    Nao garante otimo global.
    """
    x, y = _validar_pontos_2xn(pontos)
    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()

    tentativas = 10 ** expoente
    low, high = float(intervalo[0]), float(intervalo[1])

    rng = np.random.default_rng(seed)

    melhor_erro = None
    melhor_alpha = None
    n_coef = grau + 1

    for _ in range(tentativas):
        alpha = rng.uniform(low, high, size=n_coef)
        erro = SSR((x, y), alpha)
        if melhor_erro is None or erro < melhor_erro:
            melhor_erro = erro
            melhor_alpha = alpha.copy()

    if plotar:
        n_grid = max(100, int(round(max(x) - min(x)) * 100))
        x_pred = np.linspace(min(x), max(x), n_grid)
        y_pred = np.polyval(melhor_alpha, x_pred)

        plt.scatter(x, y, label="dados", s=30)
        plt.plot(x_pred, y_pred, label="polinomio", linewidth=2)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

    return melhor_alpha

def aproximacao_exponencial(pontos, plotar: bool = False, ignore_negativos: bool = False):
    """
    Ajuste exponencial do tipo y = c * exp(bx).
    Se y tiver valores negativos ou nulos:
        - Lança erro por padrão
        - Ignora tais pontos se ignore_negativos=True
    """
    x, y = _validar_pontos_2xn(pontos)
    x = np.asarray(x, dtype=float).ravel()
    y = np.asarray(y, dtype=float).ravel()

    # Tratamento dos valores inválidos de y
    if np.any(y <= 0):
        if ignore_negativos:
            mask = y > 0
            x = x[mask]
            y = y[mask]
            if x.size == 0:
                raise ValueError("todos os valores de y foram descartados por serem <= 0")
        else:
            raise ValueError(
                "para ajuste exponencial todos os valores de y devem ser positivos, "
                "caso deseje ignorar valores invalidos, use ignore_negativos=True"
            )

    y_ln = np.log(y)
    dados = np.vstack((x, y_ln))
    coef_ln = aproximacao_polinomial_mq(dados, 1)

    b = coef_ln[0]
    c = np.exp(coef_ln[1])

    if plotar:
        n_grid = max(100, int(round(max(x) - min(x)) * 100))
        x_pred = np.linspace(min(x), max(x), n_grid)
        y_pred = c * np.exp(b * x_pred)

        plt.scatter(x, y, label="dados", s=30)
        plt.plot(x_pred, y_pred, label="exponencial", linewidth=2)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.show()

    return np.array([c, b])

    return np.array([c, b])


def SSR(pontos, polinomio):
    """
    Soma dos quadrados dos residuos.
    """
    x, y = _validar_pontos_2xn(pontos)
    X = np.asarray(x, dtype=float)
    Y = np.asarray(y, dtype=float)

    y_aprox = np.polyval(polinomio, X)
    A = np.power((Y - y_aprox), 2)
    ssr = np.sum(A)

    return ssr


def SST(pontos):
    """
    Soma total dos quadrados.
    """
    _, y = _validar_pontos_2xn(pontos)
    Y = np.asarray(y, dtype=float)
    med = np.mean(Y)
    A = np.power((Y - med), 2)
    sst = np.sum(A)

    return sst


def R2(pontos, polinomio):
    """
    Coeficiente de determinacao R2.
    """
    return 1 - SSR(pontos, polinomio) / SST(pontos)
