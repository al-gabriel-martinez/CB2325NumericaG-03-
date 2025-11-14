import sys, os, pytest, matplotlib
import numpy as np
from numpy.testing import assert_array_almost_equal, assert_almost_equal
matplotlib.use('Agg')  # Backend não-interativo para testes
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CB2325NumericaG3.aproximacao import (
    aproximacao_polinomial_mq,
    aproximacao_polinomial_aleatoria,
    aproximacao_exponencial,
    SSR,
    SST,
    R2,
    encontrar_grau_polinomial_bic
)


class TestValidacaoPontos:
    """Testes para validação de entrada de pontos"""
    
    def test_pontos_validos_lista(self):
        """Testa entrada válida como lista de listas"""
        pontos = [[1, 2, 3], [4, 5, 6]]
        coef = aproximacao_polinomial_mq(pontos, grau=1)
        assert coef is not None
    
    def test_pontos_validos_array(self):
        """Testa entrada válida como array numpy"""
        pontos = np.array([[1, 2, 3], [4, 5, 6]])
        coef = aproximacao_polinomial_mq(pontos, grau=1)
        assert coef is not None
    
    def test_pontos_formato_errado_1d(self):
        """Testa rejeição de array unidimensional"""
        pontos = [1, 2, 3, 4]
        with pytest.raises(ValueError, match="bidimensional"):
            aproximacao_polinomial_mq(pontos, grau=1)
    
    def test_pontos_tres_linhas(self):
        """Testa rejeição de array com três linhas"""
        pontos = [[1, 2], [3, 4], [5, 6]]
        with pytest.raises(ValueError, match="duas linhas"):
            aproximacao_polinomial_mq(pontos, grau=1)
    
    def test_pontos_tamanhos_diferentes(self):
        """Testa rejeição quando x e y têm tamanhos diferentes"""
        pontos = [[1, 2, 3], [4, 5]]
        with pytest.raises((ValueError, IndexError)):
            aproximacao_polinomial_mq(pontos, grau=1)


class TestAproximacaoPolinomialMQ:
    """Testes para aproximação polinomial por mínimos quadrados"""
    
    def test_ajuste_linear_perfeito(self):
        """Testa ajuste linear em dados perfeitamente lineares"""
        x = np.array([0, 1, 2, 3, 4])
        y = 2 * x + 3  # y = 2x + 3
        pontos = np.vstack((x, y))
        
        coef = aproximacao_polinomial_mq(pontos, grau=1)
        
        assert_almost_equal(coef[0], 2, decimal=10)
        assert_almost_equal(coef[1], 3, decimal=10)
    
    def test_ajuste_quadratico(self):
        """Testa ajuste quadrático"""
        x = np.array([0, 1, 2, 3])
        y = x**2 + 2*x + 1  # y = x² + 2x + 1
        pontos = np.vstack((x, y))
        
        coef = aproximacao_polinomial_mq(pontos, grau=2)
        
        assert_almost_equal(coef[0], 1, decimal=10)
        assert_almost_equal(coef[1], 2, decimal=10)
        assert_almost_equal(coef[2], 1, decimal=10)
    
    def test_grau_negativo(self):
        """Testa rejeição de grau negativo"""
        pontos = [[1, 2], [3, 4]]
        with pytest.raises(ValueError, match="nao negativo"):
            aproximacao_polinomial_mq(pontos, grau=-1)
    
    def test_grau_zero(self):
        """Testa ajuste de grau zero (constante)"""
        x = np.array([1, 2, 3, 4])
        y = np.array([5, 5, 5, 5])
        pontos = np.vstack((x, y))
        
        coef = aproximacao_polinomial_mq(pontos, grau=0)
        
        assert_almost_equal(coef[0], 5, decimal=10)
    
    def test_plotar_nao_causa_erro(self):
        """Testa que o parâmetro plotar=True não causa erro"""
        pontos = [[1, 2, 3], [2, 4, 6]]
        coef = aproximacao_polinomial_mq(pontos, grau=1, plotar=True)
        assert coef is not None


class TestAproximacaoPolinomialAleatoria:
    """Testes para aproximação polinomial aleatória"""
    
    def test_seed_reprodutibilidade(self):
        """Testa que a mesma seed produz os mesmos resultados"""
        pontos = [[1, 2, 3], [2, 4, 6]]
        
        coef1 = aproximacao_polinomial_aleatoria(pontos, grau=1, expoente=2, seed=42)
        coef2 = aproximacao_polinomial_aleatoria(pontos, grau=1, expoente=2, seed=42)
        
        assert_array_almost_equal(coef1, coef2)
    
    def test_expoente_afeta_tentativas(self):
        """Testa que expoente maior pode dar resultados diferentes"""
        pontos = [[1, 2, 3, 4], [1, 4, 9, 16]]
        
        coef_poucos = aproximacao_polinomial_aleatoria(
            pontos, grau=2, expoente=1, seed=42
        )
        coef_muitos = aproximacao_polinomial_aleatoria(
            pontos, grau=2, expoente=3, seed=43
        )
        
        # Apenas verifica que retorna coeficientes
        assert len(coef_poucos) == 3
        assert len(coef_muitos) == 3
    
    def test_intervalo_customizado(self):
        """Testa intervalo customizado de busca"""
        pontos = [[1, 2, 3], [2, 4, 6]]
        
        coef = aproximacao_polinomial_aleatoria(
            pontos, grau=1, expoente=2, intervalo=(-10, 10), seed=42
        )
        
        assert len(coef) == 2
    
    def test_plotar_nao_causa_erro(self):
        """Testa que plotar=True não causa erro"""
        pontos = [[1, 2, 3], [2, 4, 6]]
        coef = aproximacao_polinomial_aleatoria(
            pontos, grau=1, expoente=2, plotar=True
        )
        assert coef is not None


class TestAproximacaoExponencial:
    """Testes para aproximação exponencial"""
    
    def test_ajuste_exponencial_perfeito(self):
        """Testa ajuste exponencial em dados exponenciais perfeitos"""
        x = np.array([0, 1, 2, 3])
        c_real, b_real = 2.0, 0.5
        y = c_real * np.exp(b_real * x)
        pontos = np.vstack((x, y))
        
        coef = aproximacao_exponencial(pontos)
        
        assert_almost_equal(coef[0], c_real, decimal=5)
        assert_almost_equal(coef[1], b_real, decimal=5)
    
    def test_valores_negativos_sem_ignore(self):
        """Testa que valores negativos causam erro por padrão"""
        pontos = [[1, 2, 3], [-1, 2, 3]]
        with pytest.raises(ValueError, match="positivos"):
            aproximacao_exponencial(pontos)
    
    def test_valores_negativos_com_ignore(self):
        """Testa ignore_negativos=True remove valores inválidos"""
        x = np.array([1, 2, 3, 4])
        y = np.array([-1, 2, 4, 8])
        pontos = np.vstack((x, y))
        
        coef = aproximacao_exponencial(pontos, ignore_negativos=True)
        
        assert coef is not None
        assert len(coef) == 2
    
    def test_valores_zero(self):
        """Testa que valores zero causam erro"""
        pontos = [[1, 2, 3], [0, 2, 3]]
        with pytest.raises(ValueError):
            aproximacao_exponencial(pontos)
    
    def test_todos_valores_invalidos(self):
        """Testa erro quando todos os valores são descartados"""
        pontos = [[1, 2, 3], [-1, -2, 0]]
        with pytest.raises(ValueError, match="descartados"):
            aproximacao_exponencial(pontos, ignore_negativos=True)
    
    def test_plotar_nao_causa_erro(self):
        """Testa que plotar=True não causa erro"""
        x = np.array([0, 1, 2, 3])
        y = 2 * np.exp(0.5 * x)
        pontos = np.vstack((x, y))
        
        coef = aproximacao_exponencial(pontos, plotar=True)
        assert coef is not None


class TestSSR:
    """Testes para soma dos quadrados dos resíduos"""
    
    def test_ssr_ajuste_perfeito(self):
        """Testa SSR zero para ajuste perfeito"""
        x = np.array([1, 2, 3])
        y = 2 * x + 1
        pontos = np.vstack((x, y))
        polinomio = [2, 1]  # y = 2x + 1
        
        ssr = SSR(pontos, polinomio)
        
        assert_almost_equal(ssr, 0, decimal=10)
    
    def test_ssr_positivo(self):
        """Testa que SSR é positivo para dados com ruído"""
        x = np.array([1, 2, 3])
        y = np.array([2.1, 4.2, 5.9])  # Aproximadamente y = 2x
        pontos = np.vstack((x, y))
        polinomio = [2, 0]
        
        ssr = SSR(pontos, polinomio)
        
        assert ssr > 0


class TestSST:
    """Testes para soma total dos quadrados"""
    
    def test_sst_constante_zero(self):
        """Testa SST zero para valores constantes"""
        pontos = [[1, 2, 3], [5, 5, 5]]
        
        sst = SST(pontos)
        
        assert_almost_equal(sst, 0, decimal=10)
    
    def test_sst_positivo(self):
        """Testa que SST é positivo para dados variáveis"""
        pontos = [[1, 2, 3], [1, 2, 3]]
        
        sst = SST(pontos)
        
        assert sst > 0


class TestR2:
    """Testes para coeficiente de determinação R²"""
    
    def test_r2_ajuste_perfeito(self):
        """Testa R² = 1 para ajuste perfeito"""
        x = np.array([1, 2, 3, 4])
        y = 2 * x + 3
        pontos = np.vstack((x, y))
        polinomio = [2, 3]
        
        r2 = R2(pontos, polinomio)
        
        assert_almost_equal(r2, 1.0, decimal=10)
    
    def test_r2_intervalo_valido(self):
        """Testa que R² está no intervalo válido"""
        x = np.array([1, 2, 3, 4])
        y = np.array([2.1, 4.2, 5.9, 8.1])
        pontos = np.vstack((x, y))
        coef = aproximacao_polinomial_mq(pontos, grau=1)
        
        r2 = R2(pontos, coef)
        
        assert 0 <= r2 <= 1


class TestEncontrarGrauPolinomialBIC:
    """Testes para seleção de grau por BIC"""
    
    def test_selecao_grau_linear(self):
        """Testa que identifica corretamente dados lineares"""
        x = np.linspace(0, 10, 50)
        y = 2 * x + 3 + np.random.normal(0, 0.1, 50)
        pontos = np.vstack((x, y))
        
        d_best, coef_best, graus, bic_vals = encontrar_grau_polinomial_bic(
            pontos, d_min=0, d_max=5
        )
        
        assert d_best <= 2  # Deve escolher grau baixo para dados lineares
        assert len(graus) == 6
        assert len(bic_vals) == 6
    
    def test_selecao_grau_quadratico(self):
        """Testa seleção em dados quadráticos"""
        x = np.linspace(0, 5, 30)
        y = x**2 + 2*x + 1 + np.random.normal(0, 0.5, 30)
        pontos = np.vstack((x, y))
        
        d_best, coef_best, graus, bic_vals = encontrar_grau_polinomial_bic(
            pontos, d_min=0, d_max=5
        )
        
        assert d_best >= 1  # Deve escolher pelo menos grau 1
        assert len(coef_best) == d_best + 1
    
    def test_d_min_maior_que_d_max(self):
        """Testa erro quando d_min > d_max"""
        pontos = [[1, 2, 3], [1, 2, 3]]
        with pytest.raises(ValueError, match="maior ou igual"):
            encontrar_grau_polinomial_bic(pontos, d_min=5, d_max=2)
    
    def test_d_min_negativo(self):
        """Testa erro para d_min negativo"""
        pontos = [[1, 2, 3], [1, 2, 3]]
        with pytest.raises(ValueError, match="nao negativo"):
            encontrar_grau_polinomial_bic(pontos, d_min=-1, d_max=5)
    
    def test_pontos_vazios(self):
        """Testa erro para pontos vazios"""
        pontos = [[], []]
        with pytest.raises(ValueError, match="vazio"):
            encontrar_grau_polinomial_bic(pontos, d_min=0, d_max=5)
    
    def test_plotar_nao_causa_erro(self):
        """Testa que plotar=True não causa erro"""
        x = np.linspace(0, 5, 20)
        y = x**2 + np.random.normal(0, 0.5, 20)
        pontos = np.vstack((x, y))
        
        d_best, coef_best, graus, bic_vals = encontrar_grau_polinomial_bic(
            pontos, d_min=0, d_max=3, plotar=True
        )
        
        assert d_best is not None


class TestCasosEspeciais:
    """Testes para casos especiais e edge cases"""
    
    def test_dois_pontos_linear(self):
        """Testa ajuste linear com apenas dois pontos"""
        pontos = [[1, 2], [3, 4]]
        coef = aproximacao_polinomial_mq(pontos, grau=1)
        assert len(coef) == 2
    
    def test_grau_maior_que_pontos(self):
        """Testa grau maior que número de pontos"""
        pontos = [[1, 2, 3], [1, 2, 3]]
        # Pode causar overfitting mas não deve dar erro
        coef = aproximacao_polinomial_mq(pontos, grau=5)
        assert len(coef) == 6
    
    def test_valores_muito_grandes(self):
        """Testa com valores numericamente grandes"""
        x = np.array([1000, 2000, 3000])
        y = x * 2
        pontos = np.vstack((x, y))
        
        coef = aproximacao_polinomial_mq(pontos, grau=1)
        assert coef is not None
    
    def test_valores_muito_pequenos(self):
        """Testa com valores numericamente pequenos"""
        x = np.array([1e-6, 2e-6, 3e-6])
        y = x * 2
        pontos = np.vstack((x, y))
        
        coef = aproximacao_polinomial_mq(pontos, grau=1)
        assert coef is not None

