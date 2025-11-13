import math
import pytest

from raizes import bissecao, newton_raphson, secante, raiz


class TestBissecao:
    def test_mudanca_de_sinal(self):
        with pytest.raises(ValueError):
            bissecao(lambda x: x**2 + 1, 0, 1, graf=False)

    def test_extremos_raizes(self):
        r = bissecao(lambda x: x - 3, 3, 6, graf=False)
        assert math.isclose(r, 3.0, abs_tol=1e-12)
        r = bissecao(lambda x: x + 2, -4, -2, graf=False)
        assert math.isclose(r, -2.0, abs_tol=1e-12)

    def test_convergencia(self):
        r = bissecao(lambda x: x**2 - 2, 1, 2, tol=1e-10, graf=False)
        assert math.isclose(r, math.sqrt(2), abs_tol=1e-9)

    def test_historico(self):
        r, hist = bissecao(lambda x: x - 1, 0, 2, tol=1e-8, graf=False, retornar_historico=True)
        assert math.isclose(r, 1.0, abs_tol=1e-6)
        assert isinstance(hist, list)

    def test_falha_convergencia(self):
        with pytest.raises(RuntimeError):
            bissecao(lambda x: x, 0, 1e-16, tol=1e-20, max_iter=1, graf=False)


class TestNewtonRaphson:
    def test_convergencia_com_derivada(self):
        f = lambda x: x**2 - 4
        df = lambda x: 2*x
        r = newton_raphson(f, x0=3.0, df=df, tol=1e-12, graf=False)
        assert math.isclose(r, 2.0, abs_tol=1e-10)

    def test_convergencia_sem_derivada(self):
        f = lambda x: math.cos(x) - x
        r = newton_raphson(f, x0=0.5, tol=1e-10, graf=False)
        assert math.isclose(r, 0.7390851332151607, abs_tol=1e-8)

    def test_derivada_zero(self):
        f = lambda x: x**3
        with pytest.raises(RuntimeError):
            newton_raphson(f, x0=0.0, tol=1e-12, graf=False)

    def test_nao_converge(self):
        f = lambda x: x**2 - 2
        with pytest.raises(RuntimeError):
            newton_raphson(f, x0=10.0, max_iter=1, graf=False)

    def test_retorno_historico(self):
        f = lambda x: x - 3
        r, hist = newton_raphson(f, x0=0.0, tol=1e-12, graf=False, retornar_historico=True)
        assert math.isclose(r, 3.0, abs_tol=1e-10)
        assert isinstance(hist, list)


class TestSecante:
    def test_divisao_zero(self):
        with pytest.raises(ZeroDivisionError):
            secante(lambda x: 5, 0, 1, graf=False)

    def test_nao_converge(self):
        with pytest.raises(RuntimeError):
            secante(lambda x: math.sin(1/x) if x != 0 else 0, 0.1, 0.2, max_iter=5, graf=False)

    def test_funcao_linear(self):
        r = secante(lambda x: x - 2, 0, 3, graf=False)
        assert math.isclose(r, 2.0, abs_tol=1e-6)

    def test_funcao_quadratica(self):
        r = secante(lambda x: x**2 - 4, 0, 3, graf=False)
        assert math.isclose(r, 2.0, abs_tol=1e-6)

    def test_funcao_cubica(self):
        r = secante(lambda x: x**3 - 8, 0, 3, graf=False)
        assert math.isclose(r, 2.0, abs_tol=1e-6)

    def test_trigonometrica(self):
        r = secante(lambda x: math.sin(x), 2, 4, graf=False)
        assert math.isclose(r, math.pi, abs_tol=1e-6)

    def test_exponencial(self):
        r = secante(lambda x: math.exp(x) - 1, -1, 1, graf=False)
        assert math.isclose(r, 0.0, abs_tol=1e-6)

    def test_raiz_negativa(self):
        r = secante(lambda x: 2*x + 1, -1, 0, graf=False)
        assert math.isclose(r, -0.5, abs_tol=1e-6)

    def test_precisao(self):
        f = lambda x: x**3 - 2*x - 5
        r1 = secante(f, 2, 3, tol=1e-4, graf=False)
        r2 = secante(f, 2, 3, tol=1e-8, graf=False)
        assert abs(r1 - 2.094551) < 1e-3
        assert abs(r2 - 2.094551) < 1e-6

    def test_historico(self):
        r, h = secante(lambda x: x - 2, 0, 3, graf=False, retornar_historico=True)
        assert math.isclose(r, 2.0, abs_tol=1e-6)
        assert isinstance(h, list)
        assert math.isclose(h[-1], 2.0, abs_tol=1e-6)

    def test_casos_limites(self):
        r = secante(lambda x: x - 1e-10, 0, 1, tol=1e-12, graf=False)
        assert abs(r - 1e-10) < 1e-8
        r = secante(lambda x: x - 0.5, 0.499, 0.501, graf=False)
        assert abs(r - 0.5) < 1e-6

    def test_sem_grafico(self):
        r = secante(lambda x: x - 2, 0, 3, graf=False)
        assert math.isclose(r, 2.0, abs_tol=1e-6)


class TestInterfaceRaiz:
    def test_bissecao_padrao(self):
        f = lambda x: x**2 - 2
        r = raiz(f, a=1, b=2, tol=1e-10, graf=False)
        assert math.isclose(r, math.sqrt(2), abs_tol=1e-9)

    def test_alias_bissecao(self):
        f = lambda x: x - 3
        r = raiz(f, a=0, b=5, method="b", graf=False)
        assert math.isclose(r, 3.0, abs_tol=1e-6)

    def test_secante(self):
        f = lambda x: x**3 - 8
        r = raiz(f, a=0, b=3, method="secante", graf=False)
        assert math.isclose(r, 2.0, abs_tol=1e-6)

    def test_newton_com_x0(self):
        f = lambda x: x**2 - 9
        r = raiz(f, x0=10.0, method="newton", graf=False)
        assert math.isclose(r, 3.0, abs_tol=1e-8)

    def test_newton_sem_x0(self):
        f = lambda x: math.cos(x) - x
        r = raiz(f, a=0, b=1, method="newton", graf=False)
        assert math.isclose(r, 0.7390851332151607, abs_tol=1e-6)

    def test_parametros_faltando(self):
        with pytest.raises(ValueError):
            raiz(lambda x: x, method="bissecao", graf=False)
        with pytest.raises(ValueError):
            raiz(lambda x: x, method="secante", graf=False)
        with pytest.raises(ValueError):
            raiz(lambda x: x, method="newton", graf=False)

    def test_metodo_invalido(self):
        with pytest.raises(ValueError):
            raiz(lambda x: x, a=0, b=1, method="invalido", graf=False)
