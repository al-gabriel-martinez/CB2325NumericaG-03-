import sys, os, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.soma_de_kahan import soma_normal_lista, soma_de_kahan_lista


def test_soma_valores_discrepantes():
    X = [100000000] + [10**(-6) for i in range(10**6)]
    assert soma_normal_lista(X) != 100000001
    assert soma_de_kahan_lista(X) == 100000001

def test_soma_serie_harmonica():
    X = [1/(i+1) for i in range(10**6)]
    soma_ideal = 14.3927267228657236
    assert soma_normal_lista(X) != pytest.approx(soma_ideal, abs=1e-13)
    assert soma_de_kahan_lista(X) == pytest.approx(soma_ideal, abs=1e-20)