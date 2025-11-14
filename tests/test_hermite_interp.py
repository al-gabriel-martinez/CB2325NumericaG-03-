import numpy as np
import pytest
from interpolacao import hermite_interp   # ajuste o nome do módulo
# Testa se a Hermite interpola exatamente os pontos dados
def test_interpola_os_pontos():
    xs = np.array([0, 1])
    ys = np.array([2, 4])
    dys = np.array([0, 0])  # derivadas nulas
    # A interpolação DEVE retornar os valores exatos
    assert hermite_interp(0, xs, ys, dys) == pytest.approx(2)
    assert hermite_interp(1, xs, ys, dys) == pytest.approx(4)
# Testa uma função simples cujo Hermite sabemos o resultado
#    f(x) = x^2  -> f'(x) = 2x
def test_funcao_quadratica():
    xs = np.array([0, 1])
    ys = xs**2
    dys = 2*xs
    # Teste em vários pontos intermediários
    for x in np.linspace(0, 1, 5):
        valor_esperado = x*x
        assert hermite_interp(x, xs, ys, dys) == pytest.approx(valor_esperado, rel=1e-6)
#Testa erro se arrays de tamanhos diferentes forem passados
def test_tamanho_inconsistente():
    xs = np.array([0, 1])
    ys = np.array([1])
    dys = np.array([1, 1])
    with pytest.raises(ValueError):
        hermite_interp(0.5, xs, ys, dys)
#Testa comportamento quando x está fora do intervalo (extrapolação)
def test_extrapolacao():
    xs = np.array([0, 1])
    ys = np.array([0, 1])
    dys = np.array([1, 1])
    # Extrapolação deve rodar sem erro
    resultado = hermite_interp(2, xs, ys, dys)
    assert isinstance(resultado, (float, np.floating))
# Testa se derivadas são respeitadas nos extremos
def test_derivadas_respeitadas():
    xs = np.array([0, 1])
    ys = np.array([0, 1])
    dys = np.array([2, -1])
    # Verifica derivada no ponto x = 0 usando limite numérico
    h = 1e-6
    derivada_num = (hermite_interp(h, xs, ys, dys) - hermite_interp(0, xs, ys, dys)) / h
    assert derivada_num == pytest.approx(2, rel=1e-3)
