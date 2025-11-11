import sys, os, math, pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.integracao import integral

class TestIntegral:
    """Testes para o módulo de integração numérica."""

    # Descreve entradas de função, limite sup, limite inf, particoes.
    @pytest.mark.parametrize(
            "funcao, a, b, n",
            [
                (lambda x: f'x{x}', 0, 1, 10000),
                (lambda x: (x, 0), 3, 12.5, 10000),
                (lambda x: [x**2, 3], 0, 1, 10000),
            ]
    )
    def test_input_invalido(self, funcao, a, b, n):
        with pytest.raises(TypeError):
            integral(funcao, a, b, n, plotar=False) # type: ignore

    # Descreve entradas de função, limite sup, limite inf, particoes.
    @pytest.mark.parametrize(
            "funcao, a, b, n",
             [
                 (lambda x: x, 'a', 1, 10000),
                 (lambda x: x, ('num', 'num'), 12.5, 10000),
                 (lambda x: x, [0, 0], 1, 10000), 
                 (lambda x: x, 1, 'b', 10000),
                 (lambda x: x, 1, ('num', 'num'), 10000),
                 (lambda x: x, 1, [0, 0], 10000),
                 (lambda x: x,lambda x: 2*x, lambda x: 5*x, 10000),
             ]
     )
    
    def test_intervalo_invalido(self, funcao, a, b, n):
        with pytest.raises(TypeError):
            integral(funcao, a, b, n, plotar=False) # type: ignore

    # Descreve entradas de função, limite sup, limite inf, particoes.
    @pytest.mark.parametrize(
            "funcao, a, b, n",
             [
                 (lambda x: x, 0, 1, 'particoes'),
                 (lambda x: x, 0, 1, (1000, 909)),
                 (lambda x: x, 0, 1, [900]),
             ]
    )

    def test_particoes_invalido(self, funcao, a, b, n):
        with pytest.raises(TypeError):
            integral(funcao, a, b, n, plotar=False) # type: ignore

    # Descreve entradas de função, limite sup, limite inf, particoes e valor esperado.
    @pytest.mark.parametrize(
            "funcao, a, b, n, valor_esp",
             [
                 (lambda x: x, 1, 0, 10000, -0.5),
                 (lambda x: -2*x**3 + 4*x**2 + 3*x, 5, 2, 10000, 117),
                 (lambda x: math.cos(x), math.pi/4, -3*math.pi/4, 10000, -1.4142),
             ]
    )

    def test_intervalo_invertido(self, funcao, a, b, n, valor_esp):
        area = integral(funcao, a, b, n, plotar=False, metodo='simpson')
        assert math.isclose(area, valor_esp, abs_tol=0.01)
    
    def test_polinomio(self):
        pytest.skip("Testar resultado da integral de uma função polinomial")
        
    def test_constante(self):
        pytest.skip("Testar validação de número de partições inválido (n <= 0, n não inteiro)")

    def test_precisao(self):
        pytest.skip("Testar convergência do método com aumento de n")

    def test_limites_nao_usuais(self):
        pytest.skip("Testar comportamento em limites e casos de borda")
    
    def test_nan(self):
        pytest.skip("Testar comportamento com math.nan")  

    def test_inf(self):  
        pytest.skip("Testar comportamento com math.inf")