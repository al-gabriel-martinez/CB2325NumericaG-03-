import matplotlib.pyplot as plt

class VisualizadorRaizes:
    """
    Classe para visualização gráfica de métodos de busca de raízes.
    """
    
    def __init__(self, f, intervalo=(-5, 5)):
        self.f = f
        self.a, self.b = intervalo
    
    def _gerar_pontos(self, a, b, n=200):
        """Gera n pontos no intervalo [a,b]."""
        passo = (b - a) / (n - 1)
        return [a + i * passo for i in range(n)]
    
    def visualizar(self, historico, a=None, b=None, titulo="Busca de Raiz"):
        """
        Visualização única para qualquer método.
        
        Parâmetros:
        historico: lista com as aproximações feitas em cada iteração
        a, b: limites do gráfico
        titulo: título do gráfico
        """
        # Definir limites do gráfico
        if a is None: a = min(historico) - 1
        if b is None: b = max(historico) + 1
        
        # Gerar pontos da função
        x_vals = self._gerar_pontos(a, b)
        y_vals = [self.f(x) for x in x_vals]
        
        # Criar dois gráficos, um da função e outro sobre a convergência do método
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
        
        
        # Gráfico 1: Função, iterações e intervalo
        ax1.plot(x_vals, y_vals, 'b-', linewidth=2, label='f(x)') # Função
        ax1.axhline(y=0, color='k', linestyle='--', alpha=0.5) # Eixo x
        
        # Plotar iterações
        for i, ponto in enumerate(historico):
            cor = 'red' if i == len(historico) - 1 else 'orange'
            ax1.scatter(ponto, self.f(ponto), color=cor, s=60, zorder=5)
            ax1.text(ponto, self.f(ponto), f"P{i+1}", fontsize=9, color=cor,
             ha='left', va='bottom')  # Nomeando o ponto
            if i < len(historico) - 1:
                ax1.plot([ponto, historico[i+1]], [self.f(ponto), self.f(historico[i+1])], 
                        'r--', alpha=0.5)
                
        # Plotar intervalo
        ax1.axvline(x=min(historico), color='green', linestyle='--', alpha=0.5, label='Intervalo')
        ax1.axvline(x=max(historico), color='green', linestyle='--', alpha=0.5)
        ax1.axvspan(min(historico), max(historico), alpha=0.06, color='green')
        
        # Plotar gráfico 1
        ax1.set_xlabel('x')
        ax1.set_ylabel('f(x)')
        ax1.set_title(f'{titulo}\nRaiz: {historico[-1]:.6f}')
        ax1.grid(True, alpha=0.3)
        ax1.legend()
        

        # Gráfico 2: Convergência
        erros = [abs(self.f(ponto)) for ponto in historico]
        iteracoes = list(range(1, len(erros) + 1))
        
        # Plotar gráfico 2
        ax2.semilogy(iteracoes, erros, 'ro-', linewidth=2, markersize=6) # Em escala logarítmica porque os erros diminuem exponencialmente
        ax2.set_xlabel('Iteração')
        ax2.set_ylabel('|f(x)|')
        ax2.set_title('Convergência do Método')
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        


        
        # Informações como raiz, y da raiz, iterações e erro final
        print("=" * 40)
        print(f"Raiz encontrada: {historico[-1]:.8f}")
        print(f"f(raiz) = {self.f(historico[-1]):.2e}")
        print(f"Iterações: {len(historico)}")
        print(f"Erro final: {erros[-1]:.2e}")
        print("=" * 40)

# Função de uso
def visualizar_metodo(f, historico, **kwargs):
    """Função para visualização."""
    viz = VisualizadorRaizes(f)
    viz.visualizar(historico, **kwargs)










# TESTES DE EXEMPLO:
def f(x):
    return x**3 - 9*x + 5

historico = [1.0, 0.5, 0.75, 0.625, 0.5625, 0.53125, 0.546875, 0.5546875, 0.55078125]

visualizar_metodo(f, historico, a=-4, b=5, titulo="Método da Bisseção")


historico_secante = [0, 2, 0.4, 0.6, 0.55, 0.551, 0.5508]

visualizar_metodo(f, historico_secante, a=-4, b=5, titulo="Método da Secante")


historico_newton = [2.0, 1.8333, 1.7381, 1.7001, 1.6905, 1.6899]

visualizar_metodo(f, historico_newton, a=-4, b=5, titulo="Método de Newton")