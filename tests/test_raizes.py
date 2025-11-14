# tests/test_raizes.py
import sys, os, pytest, matplotlib, math
import matplotlib.pyplot as plt
from matplotlib.collections import PathCollection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from CB2325NumericaG3.raizes import bissecao, newton_raphson, secante, raiz
matplotlib.use("Agg") 
import CB2325NumericaG3.visualizacao_raizes as vg


sys.path.append(os.path.dirname(os.path.dirname(__file__)))

def test_gerar_pontos(monkeypatch):
    """Testa se gerar_pontos gera o número correto de pontos e se estão igualmente espaçados."""
    monkeypatch.setattr(plt, "show", lambda: None)

    visualizar = vg.VisualizadorRaizes(lambda x: x)
    numero_pontos = 100
    inicio = -100
    fim = 100
    lista_pontos = visualizar._gerar_pontos(a=inicio,b=fim,n=numero_pontos)
    assert len(lista_pontos)==numero_pontos
    delta1=lista_pontos[2]-lista_pontos[1]
    delta2=lista_pontos[-1]-lista_pontos[-2]
    assert abs(delta1-delta2) <=1e-6 
    assert abs(lista_pontos[-1]-fim)<=1e-6

def test_visualizar(monkeypatch):
    """Testa se vizualizar plota o gráfico com os elementos desejados."""
    monkeypatch.setattr(plt, "show", lambda: None)
    
    f = lambda x: x**2 - 4
    historico = [0, 10, 5, 6, -1]
    viz = vg.VisualizadorRaizes(f)
    
    # Visualização padrão
    viz.visualizar(historico)
    fig = plt.gcf()
    axes = fig.get_axes()
    
    ax1 = axes[0]
    xmin, xmax = ax1.get_xlim()
    assert len(ax1.lines) > 0
    
    scatters = [c for c in ax1.collections if isinstance(c, PathCollection)]
    assert len(scatters) == len(historico)
    
    assert xmin <= min(historico) - 1 + 1e-8
    assert xmax >= max(historico) + 1 - 1e-8
    
    # Visualização com limites e título personalizados
    a, b = -11, -11
    viz.visualizar(historico, a, b, titulo="testando")
    ax1 = plt.gcf().axes[0]
    xmin, xmax = ax1.get_xlim()
    assert xmin <= a - 1 + 1e-8
    assert xmax >= b + 1 - 1e-8
    
    axes = plt.gcf().get_axes()
    assert len(axes) == 2
    
    titulo = ax1.get_title()
    assert f"Raiz: {historico[-1]:.6f}" in titulo
    assert "testando" in titulo
    
    ax2 = axes[1]
    assert ax2.get_yscale() == 'log'

def test_visualizar_metodo(monkeypatch):
    """Testa se visualizar_metodo passa os parâmetros corretamente."""
    chamado = {}

    def fake_visualizar(self, historico, **kwargs):
        chamado["ok"] = (historico, kwargs)

    monkeypatch.setattr(vg.VisualizadorRaizes, "visualizar", fake_visualizar)

    f = lambda x: x**2 - 4
    historico = [1, 2, 3]

    vg.visualizar_metodo(f, historico, titulo="teste")

    assert "ok" in chamado
    assert chamado["ok"][0] == historico
    assert chamado["ok"][1]["titulo"] == "teste"

@pytest.fixture
def setup_viz(monkeypatch):
    """Configura o ambiente de teste e retorna dados para o teste."""
    monkeypatch.setattr(plt,"show",lambda:None)
    f = lambda x: x**2-4
    historico = [-2,-1,0,1,2]
    viz = vg.VisualizadorRaizes(f)

    fig=plt.gcf()
    ax1,ax2 = fig.axes
    return f, historico,ax1,ax2
    

def test_cor_pontos(setup_viz):
    """Verifica se a cor dos pontos em ax1 está correta."""
    _,_,ax1,_ =setup_viz

    scatters = [c for c in ax1.collections if isinstance(c, PathCollection)]
    for i,scat in enumerate(scatters):
        cor_ponto = scat.get_facecolor()[0]
        r, g, b, _ = cor_ponto

        if i == len(scatters)-1:
            assert r > 0.8 and g < 0.2 and b < 0.2
        else:
            assert r > 0.8 and g > 0.3 and b < 0.3

def test_linhas_tracejadas_vermelhas(setup_viz):
    """Verifica se há um número coreeto de retas vermelhas"""

    _, historico, ax1, _ = setup_viz

    linhas_vermelhas = [
        line for line in ax1.get_lines()
        if line.get_linestyle() == '--' and (line.get_color() in ['r', '#ff0000'])
    ]
    assert len(linhas_vermelhas) >= len(historico) - 1

def test_textos_pontos(setup_viz):
    """Verifica se o texto dos pontos está correto"""
    _, historico, ax1, _ = setup_viz
    textos = [t.get_text() for t in ax1.texts]
    esperados = [f"P{i+1}" for i in range(len(historico))]
    assert textos == esperados

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
