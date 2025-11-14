import sys, os, pytest
import matplotlib 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.interpolacao import linear_interp
matplotlib.use('Agg')  # evita abrir janelas de gráfico nos testes


 # altere o nome conforme seu arquivo
def test_interpolacao_simples():
    # Pontos de uma função linear simples: y = 2x
    X = [0, 1, 2]
    Y = [0, 2, 4]
    f = linear_interp(X, Y, plot=False)
    assert f(0) == pytest.approx(0)
    assert f(0.5) == pytest.approx(1)
    assert f(1.5) == pytest.approx(3)
    assert f(2) == pytest.approx(4)
def test_interpolacao_nao_linear():
    # Pontos que formam uma função não linear
    X = [0, 1, 2]
    Y = [1, 3, 2]
    f = linear_interp(X, Y, plot=False)
    # Verifica interpolação entre 0 e 1 (reta entre (0,1) e (1,3))
    assert f(0.5) == pytest.approx(2)
    # Entre 1 e 2 (reta entre (1,3) e (2,2))
    assert f(1.5) == pytest.approx(2.5)
def test_extrapolacao_para_esquerda():
    X = [1, 2, 3]
    Y = [2, 4, 6]
    f = linear_interp(X, Y, plot=False)
    # Extrapolação para t < X[0]
    # Regressão linear dos dois primeiros pontos: y = 2x
    assert f(0) == pytest.approx(0)
    assert f(0.5) == pytest.approx(1)
def test_extrapolacao_para_direita():
    X = [1, 2, 3]
    Y = [2, 4, 6]
    f = linear_interp(X, Y, plot=False)
    # Extrapolação para t > X[-1]
    assert f(4) == pytest.approx(8)
    assert f(3.5) == pytest.approx(7)
def test_funcao_retorna_callable():
    X = [0, 1, 2]
    Y = [0, 1, 0]
    f = linear_interp(X, Y, plot=False)
    assert callable(f)
def test_plot_nao_gatilha_erro():
    X = [0, 1, 2]
    Y = [0, 1, 0]
    # Apenas verifica se o plot funciona sem erro
    f = linear_interp(X, Y, plot=True, title="Teste Plot")
    assert callable(f)
def test_ordem_automatica_dos_pontos():
    # Testa se a função ordena automaticamente os pontos
    X = [2, 0, 1]
    Y = [4, 0, 2]
    f = linear_interp(X, Y, plot=False)
    assert f(1.5) == pytest.approx(3)


