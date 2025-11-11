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

    def test_precisao(self):
        area1 = integral(lambda x: x**3 + 4 * x**2, -2, 3, 100, plotar=False, metodo="simpson")
        area2 = integral(lambda x: x**3 + 4 * x**2, -2, 3, 1000, plotar=False, metodo="simpson")
        # Resultado esperado = 62.916666...

        assert math.isclose(area1, 62.917, abs_tol=0.01)
        assert math.isclose(area2, 62.917, abs_tol=0.001)
        assert abs(area2 - 62.917) < abs(area1 - 62.917)  # convergência

    @pytest.mark.parametrize(
        "funcao, a, b, n, metodo, condicao",
        [
            # a == b, então resultado 0
            (lambda x: x**2, 5, 5, 1000, 'simpson', lambda area: math.isclose(area, 0.0, abs_tol=1e-12)),  
            # Intervalo muito pequeno
            (lambda x: x, 0, 1e-6, 1000, 'simpson', lambda area: area < 1e-6),
            # Intervalo grande
            (lambda x: 1 / (x + 1), 0, 1e3, 1000, 'simpson', lambda area: (not math.isnan(area)) and area > 0),
        ],
    )
    def test_limites_nao_usuais(self, funcao, a, b, n, metodo, condicao):
        area = integral(funcao, a, b, n, plotar=False, metodo=metodo)
        assert condicao(area)
