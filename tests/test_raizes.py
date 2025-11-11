import sys
import os
import math
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.raizes import secante

class TestSecante:
    """Testes para o método da secante."""
    
    def test_entradas_invalidas(self):
        """Testa entradas inválidas."""
    with pytest.raises((TypeError, ValueError)):
        secante(lambda x: 'texto', 0, 1, graf=False)

    def test_limites_invalidos(self):
        """Testa limites inválidos."""
        with pytest.raises(TypeError):
            secante(lambda x: x, 'a', 1, graf=False)

    def test_tolerancia_invalida(self):
        """Testa tolerância inválida."""
        with pytest.raises(TypeError):
            secante(lambda x: x, 0, 1, tol='erro', graf=False)

    def test_max_iter_invalido(self):
        """Testa max_iter inválido."""
        with pytest.raises(TypeError):
            secante(lambda x: x, 0, 1, max_iter='100', graf=False)
        
    def test_divisao_por_zero(self):
        """Testa quando f(a) = f(b)."""
        with pytest.raises(ZeroDivisionError):
            secante(lambda x: 5, 0, 1, graf=False)

    def test_nao_converge(self):
        """Testa quando o método não converge."""
        with pytest.raises(RuntimeError):
            secante(lambda x: math.sin(1/x) if x != 0 else 0, 0.1, 0.2, max_iter=5, graf=False)

    def test_funcao_linear(self):
        """Testa função linear simples."""
        raiz = secante(lambda x: x - 2, 0, 3, graf=False)
        assert math.isclose(raiz, 2.0, abs_tol=1e-6)

    def test_funcao_quadratica(self):
        """Testa função quadrática."""
        raiz = secante(lambda x: x**2 - 4, 0, 3, graf=False)
        assert math.isclose(raiz, 2.0, abs_tol=1e-6)

    def test_funcao_cubica(self):
        """Testa função cúbica."""
        raiz = secante(lambda x: x**3 - 8, 0, 3, graf=False)
        assert math.isclose(raiz, 2.0, abs_tol=1e-6)

    def test_funcao_trigonometrica(self):
        """Testa função trigonométrica."""
        raiz = secante(lambda x: math.sin(x), 2, 4, graf=False)
        assert math.isclose(raiz, math.pi, abs_tol=1e-6)

    def test_funcao_exponencial(self):
        """Testa função exponencial."""
        raiz = secante(lambda x: math.exp(x) - 1, -1, 1, graf=False)
        assert math.isclose(raiz, 0.0, abs_tol=1e-6)

    def test_raiz_negativa(self):
        """Testa raiz negativa."""
        raiz = secante(lambda x: 2*x + 1, -1, 0, graf=False)
        assert math.isclose(raiz, -0.5, abs_tol=1e-6)

    def test_precisao(self):
        """Testa diferentes níveis de precisão."""
        funcao = lambda x: x**3 - 2*x - 5
        
        raiz1 = secante(funcao, 2, 3, tol=1e-4, graf=False)
        raiz2 = secante(funcao, 2, 3, tol=1e-8, graf=False)
        
        assert abs(raiz1 - 2.094551) < 1e-3
        assert abs(raiz2 - 2.094551) < 1e-6

    def test_retorno_historico(self):
        """Testa o retorno do histórico."""
        raiz, historico = secante(
            lambda x: x - 2, 0, 3, graf=False, retornar_historico=True
        )
        
        assert math.isclose(raiz, 2.0, abs_tol=1e-6)
        assert isinstance(historico, list)
        assert len(historico) >= 3
        assert math.isclose(historico[-1], 2.0, abs_tol=1e-6)

    def test_casos_limites(self):
        """Testa casos especiais."""
        # Raiz próxima de zero
        raiz = secante(lambda x: x - 1e-10, 0, 1, tol=1e-12, graf=False)
        assert abs(raiz - 1e-10) < 1e-8
        
        # Intervalo pequeno
        raiz = secante(lambda x: x - 0.5, 0.499, 0.501, graf=False)
        assert abs(raiz - 0.5) < 1e-6

    def test_sem_grafico(self):
        """Testa execução sem gráfico."""
        raiz = secante(lambda x: x - 2, 0, 3, graf=False)
        assert math.isclose(raiz, 2.0, abs_tol=1e-6)