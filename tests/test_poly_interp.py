import sys, os, pytest
import numpy as np
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.interpolacao import poly_interp
# Testes:


"""
    Lagrange
"""

def test_lagrange_de_valores():
    pol = poly_interp([0,1,2,3], [1,2,0,4], method="lagrange", plot=False)
    assert pol(1.5) == 0.8125

    pol2 = poly_interp([200,400,600,800,1000,1200,1400],[15,9,5,3,-2,-5,-15], method="lagrange", plot=False)
    assert pol2(700) == 4.3115234375

    pol3 = poly_interp([1], [2], method="lagrange", plot=False)
    assert pol3(1.5) == 2.0



def test_lagrange_lista():
    x = [0,1,2,3]
    y = [1,2,0,4]
    pol = poly_interp(x, y, method="lagrange", plot=False)
    r = pol([1.5, 2.0])

    assert isinstance(r, np.ndarray)

    assert np.allclose(r, [0.8125, 0])

    assert len(r) == len([1.5,2.0])

@pytest.mark.parametrize("x, y, ponto, err", [
    ([], [2], 1.5, ValueError),
    ([1], [], 1.5, ValueError),
    ([], [], 1.5, ValueError),
    ([1,2], [2], 1.5, ValueError),
    ([1], [2,6], 1.5, ValueError),
    ([1,2,3,2], [2,3,0,5], 1.5, ValueError),
    ([0,1,2,3], [1,2,0,4], "oi", TypeError),
    ([0,1,2,3], [1,2,0,4], ["oi","tudo","bem?"], ValueError),
    ([0,1,2,3], [1,2,0,4],[4,5,"oi",7,"tudo",9,"bem?"], ValueError),
    ([0,1,"oi",2,3], [1,2,0,4],[4,5,6], ValueError),
    ([0,1,2,3], [1,2,"oi",0,4],[4,5,6], ValueError),
    ([0,1,2,3], [1,2,0,4], None, TypeError),
    (None, [1,2,0,4], [1,2,4,5], TypeError),
    ([0,1,2,3], None,[4,2.5,1], TypeError),
    (1, 6, 1.5, TypeError),
    ([1], 6, 1.5, TypeError),
    (1, [6], 1.5, TypeError),
    ("oi", [2,3,0,5], 1.5, TypeError),
    ([1,2,3,4], "oi", 1.5, TypeError),
    ([1], [None], 1.5, ValueError),
    ([None], [2], 1.5, ValueError)
])
def test_lagrange_entradas_incorretas(x, y, ponto, err):
    with pytest.raises(err):
        pol = poly_interp(x, y, method="lagrange", plot=False)
        pol(ponto)


"""
    Newton 
"""

def test_newton_coeficientes1():
    x = [1, 2, 4]
    y = [1, 4, 16]  # y = x^2

    # f[x0] = 1
    # f[x1] = 4
    # f[x2] = 16
    # f[x0,x1] = (4-1)/(2-1) = 3
    # f[x1,x2] = (16-4)/(4-2) = 6
    # f[x0,x1,x2] = (6-3)/(4-1) = 1
    coef_esperados = [1, 3, 1]  

    # Código.
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    coef_calc = coef[0, :]

    assert np.allclose(coef_calc, coef_esperados)
def test_newton_coeficientes2():
    x = [1, 2, 3]
    y = [2, 3, 4] # y = x+1
    # f[x0]=2
    # f[x1]=3
    # f[x2]=4
    # f[x0,x1]=(3-2)/(2-1)=1
    # f[x1,x2]=(4-3)/(3-2)=1
    # f[x0,x1,x2]=(1-1)/(3-1)=0
    coef_esperados = [2, 1, 0]

    # Código.
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    coef_calc = coef[0, :]

    assert np.allclose(coef_calc, coef_esperados)

def test_newton_coeficientes_quantidade_():
    x = [1, 2, 3,4,5,6]
    y = [2, 3, 4,5,6,8]
    # Código.
    n = len(x)
    coef = np.zeros((n, n))
    coef[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    coef_calc = coef[0, :]

    assert len(coef_calc) == len(x)

def test_newton_eval_valor():
    x = [1, 2, 4]
    y = [1, 4, 16] # y = x^2
    pol = poly_interp(x, y, method="newton", plot=False)
    
    assert pol(3) == 9.0

def test_newton_eval_valor_exemplo():
    pol = poly_interp([0,1,2,3], [1,2,0,4], method="newton", plot=False)
    assert pol(1.5) == 0.8125

def test_newton_eval_lista_de_pontos():
    x = [1, 2, 4]
    y = [1, 4, 16]# y = x^2 
    pol = poly_interp(x, y, method="newton", plot=False)
    pontos = [1.5, 3, 3.5]
    resultados = pol(pontos)

    esperados = np.array(pontos) ** 2  #  y = x^2
    assert np.allclose(resultados, esperados)

def test_newton_eval_lista_de_pontos_exemplo():
    x = [0,1,2,3]
    y = [1,2,0,4]
    pol = poly_interp(x, y, method="newton", plot=False)
    pontos = [0,1,2,3]
    resultados = pol(pontos)

    esperados = [1,2,0,4] 
    assert np.allclose(resultados, esperados)

def test_newton_eval_tipo_de_retorno():
    x = [1, 2, 4]
    y = [1, 4, 16]
    pol = poly_interp(x, y, method="newton", plot=False)

    assert isinstance(pol([1, 2, 3]), np.ndarray)

@pytest.mark.parametrize("x, y, ponto, err", [
    ([], [2], 1.5, ValueError),
    ([1], [], 1.5, ValueError),
    ([], [], 1.5, ValueError),
    ([1,2], [2], 1.5, ValueError),
    ([1], [2,6], 1.5, ValueError),
    ([1,2,3,2], [2,3,0,5], 1.5, ValueError),
    ([0,1,2,3], [1,2,0,4], "oi", TypeError),
    ([0,1,2,3], [1,2,0,4], ["oi","tudo","bem?"], ValueError),
    ([0,1,2,3], [1,2,0,4],[4,5,"oi",7,"tudo",9,"bem?"], ValueError),
    ([0,1,"oi",2,3], [1,2,0,4],[4,5,6], ValueError),
    ([0,1,2,3], [1,2,"oi",0,4],[4,5,6], ValueError),
    ([0,1,2,3], [1,2,0,4], None, TypeError),
    (None, [1,2,0,4], [1,2,4,5], TypeError),
    ([0,1,2,3], None,[4,2.5,1], TypeError),
    (1, 6, 1.5, TypeError),
    ([1], 6, 1.5, TypeError),
    (1, [6], 1.5, TypeError),
    ("oi", [2,3,0,5], 1.5, TypeError),
    ([1,2,3,4], "oi", 1.5, TypeError),
    ([1], [None], 1.5, ValueError),
    ([None], [2], 1.5, ValueError)
])
def test_newton_entradas_incorretas(x, y, ponto, err):
    with pytest.raises(err):
        pol = poly_interp(x, y, method="newton", plot=False)
        pol(ponto)

"""
    Vandermonde
"""





def test_vandermonde_coeficientes1():
    x = np.array([0, 1, 2])
    y = np.array([1, 6, 7]) # y = = -2x^2 + 7x + 1 
    
    # Código.
    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)
    
    coef_esperados = np.array([1, 7, -2])
    
    assert np.allclose(coeficientes, coef_esperados, rtol=1e-8, atol=1e-12)

def test_vandermonde_coeficientes2(): 
    x = np.array([0, 1, 2,3])
    y = np.array([0, 1, 8,27]) # y = x^3 
    
    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)
    
    coef_esperados = np.array([0, 0, 0,1])
    
    assert np.allclose(coeficientes, coef_esperados, rtol=1e-8, atol=1e-12)

def test_vandermonde_coeficientes3(): 
    x = np.array([0, 1, 2,-1,-2,3])
    y = np.array([-4, -12.5, -130,-14.5,-194,-566.5]) #y =  x^5 - 10x^4 + 0.5 x^2 -4 
    
    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)
    
    coef_esperados = np.array([-4, 0, 0.5,0,-10,1])
    
    assert np.allclose(coeficientes, coef_esperados, rtol=1e-8, atol=1e-12)

def test_vandermonde_coeficientes4(): 
    x = np.array([0, 1, 2])
    y = np.array([0, 1, 2]) # y = x
    

    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)
    

    coef_esperados = np.array([0,1,0])
    
    assert np.allclose(coeficientes, coef_esperados, rtol=1e-8, atol=1e-12)

def test_vandermonde_coeficientes5(): 
    x = np.array([0, 1])
    y = np.array([2, 2])# y = 2
    
    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)
    
    coef_esperados = np.array([2,0])
    
    assert np.allclose(coeficientes, coef_esperados, rtol=1e-8, atol=1e-12)

def test_vandemonde_quantidade_de_coeficientes():
    x = np.array([0,1,3,4,5,6,7,8,9,34])
    y = np.array([2,2,1,3,4,5,6,8,9,12])
    
    V = np.vander(x, increasing=True)
    coeficientes = np.linalg.solve(V, y)

    
    assert len(coeficientes) == len(x) 



def test_eval_vandermonde_grau_maior():
    x = [1,2,3,4]
    y = [1, 8, 27, 64]  # y = x^3
    pol = poly_interp(x, y, method="vandermonde", plot=False)

    pontos = [0.5, 1.5, 2.5]
    resultados = pol(pontos)
    esperados = np.array(pontos)**3

    assert np.allclose(resultados, esperados, rtol=1e-8, atol=1e-12)
def test_eval_vandermonde_um_ponto():
    x = [2]
    y = [5]  # Polinômio constante.
    pol = poly_interp(x, y, method="vandermonde", plot=False)

    assert pol(2) == 5
    assert pol(10) == 5

def test_eval_vandermonde_lista_de_pontos():
    x = [1, 2, 3]
    y = [1, 4, 9]  # y = x^2
    pol = poly_interp(x, y, method="vandermonde", plot=False)

    pontos = [1.5, 2.5, 3.5]
    resultados = pol(pontos)
    esperados = np.array(pontos)**2

    assert np.allclose(resultados, esperados, rtol=1e-8, atol=1e-12)

@pytest.mark.parametrize("x, y, ponto, err", [
    ([], [2], 1.5, ValueError),
    ([1], [], 1.5, ValueError),
    ([], [], 1.5, ValueError),
    ([1,2], [2], 1.5, ValueError),
    ([1], [2,6], 1.5, ValueError),
    ([1,2,3,2], [2,3,0,5], 1.5, ValueError),
    ([0,1,2,3], [1,2,0,4], "oi", TypeError),
    ([0,1,2,3], [1,2,0,4], ["oi","tudo","bem?"], ValueError),
    ([0,1,2,3], [1,2,0,4],[4,5,"oi",7,"tudo",9,"bem?"], ValueError),
    ([0,1,"oi",2,3], [1,2,0,4],[4,5,6], ValueError),
    ([0,1,2,3], [1,2,"oi",0,4],[4,5,6], ValueError),
    ([0,1,2,3], [1,2,0,4], None, TypeError),
    (None, [1,2,0,4], [1,2,4,5], TypeError),
    ([0,1,2,3], None,[4,2.5,1], TypeError),
    (1, 6, 1.5, TypeError),
    ([1], 6, 1.5, TypeError),
    (1, [6], 1.5, TypeError),
    ("oi", [2,3,0,5], 1.5, TypeError),
    ([1,2,3,4], "oi", 1.5, TypeError),
    ([1], [None], 1.5, ValueError),
    ([None], [2], 1.5, ValueError)
])
def test_vandermonde_entradas_incorretas(x, y, ponto, err):
    with pytest.raises(err):
        pol = poly_interp(x, y, method="vandermonde", plot=False)
        pol(ponto)
