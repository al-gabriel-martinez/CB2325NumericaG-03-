import sys, os, pytest
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.interpolacao import hermite_interp


import pytest
import numpy as np
from CB2325NumericaG3.interpolacao import hermite_interp

# 1️⃣ Testa se a Hermite interpola exatamente os pontos dados
def test_interpola_os_pontos():
    xs = [0, 1]
    ys = [2, 4]
    dys = [0, 0]  # derivadas nulas

    deriv_list = [[y, dy] for y, dy in zip(ys, dys)]
    H = hermite_interp(xs, deriv_list, plot=False)

    assert H(0) == pytest.approx(2)
    assert H(1) == pytest.approx(4)

# 2️⃣ Testa uma função quadrática f(x) = x^2 -> f'(x) = 2x
def test_funcao_quadratica():
    xs = [0, 1]
    ys = [x**2 for x in xs]
    dys = [2*x for x in xs]

    deriv_list = [[y, dy] for y, dy in zip(ys, dys)]
    H = hermite_interp(xs, deriv_list, plot=False)

    for x in np.linspace(0, 1, 5):
        valor_esperado = x**2
        assert H(x) == pytest.approx(valor_esperado, rel=1e-6)

# 3️⃣ Testa erro se arrays de tamanhos diferentes forem passados
def test_tamanho_inconsistente():
    xs = [0, 1]
    ys = [1]       # tamanho diferente de xs
    dys = [1, 1]

    deriv_list = [[y, dy] for y, dy in zip(ys, dys)]
    # A função pode lançar ValueError ou outro erro de tamanho
    with pytest.raises(ValueError):
        hermite_interp(xs, deriv_list, plot=False)

# 4️⃣ Testa extrapolação (x fora do intervalo dos nós)
def test_extrapolacao():
    xs = [0, 1]
    ys = [0, 1]
    dys = [1, 1]

    deriv_list = [[y, dy] for y, dy in zip(ys, dys)]
    H = hermite_interp(xs, deriv_list, plot=False)

    resultado = H(2)  # ponto fora do intervalo
    assert isinstance(resultado, (float, np.floating))

# 5️⃣ Testa se derivadas são respeitadas nos extremos
def test_derivadas_respeitadas():
    xs = [0, 1]
    ys = [0, 1]
    dys = [2, -1]

    deriv_list = [[y, dy] for y, dy in zip(ys, dys)]
    H = hermite_interp(xs, deriv_list, plot=False)

    # Verifica derivada no ponto x=0 usando limite numérico
    h = 1e-6
    derivada_num = (H(h) - H(0)) / h
    assert derivada_num == pytest.approx(2, rel=1e-3)

