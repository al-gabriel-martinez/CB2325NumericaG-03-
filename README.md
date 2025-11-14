# CB2325NumericaG3
Biblioteca de Cálculo Numérico em Python para AV2 da Disciplina de Programação 2 do IMPA Tech - Grupo 03


**Participantes:**

* Anízio Silva Correia Júnior
* Cristiane Magarinos Sampaio
* Davi Bezerra Leal Guimarães
* Felipe Lima De Sousa
* Felipe Ribeiro Mendonça
* Gabriel Falcão Martinez
* Guilherme Oséias Pereira Da Silva
* Heitor Ramos Pereira
* João Pedro Lima de Almeida
* Natália Brandão De Sousa
* Theo Veiga Drumond Ambrósio

**Funcionalidades:**

* Erros Numéricos
    * Erro Absoluto
    * Erro Relativo
    * Calculo de Epslon
* Interpolação
    * Linear
    * Hermite
    * Polinomiais
        * Lagrange
        * Newton
        * Vandermonde
* Integração
    * Trapézio
    * Ponto Médio
    * Simpson
* Raízes
    * Bisseção
    * Newton - Raphson
    * Secante
* Aproximação
    * Polinomial
    * Exponencial
* Soma de Kahan

## Instalação da Biblioteca 



## Visão Geral Das Funções Com Exemplos 

### Erros Numéricos 


#### Erro Absoluto 

Erro absoluto é definido como: 

$|Valor Real - Valor de Aproximação|$ 

Para a função retornar qual o erro absoluto de uma dada aproximação, o usuário deve:

- Fornecer o valor original.
- Fornecer a sua aproximação.
- Fornecer, opcionalmente, a quantidade desejada de casas decimais de precisão do erro absoluto.
  
Caso o usuário não indique quantas casas decimais de precisão deseja, ou insira um valor inválido, a função retornará automaticamente o erro com precisão de 7 casas decimais.A maior precisão permitida pela função é de 15 casas decimais, e caso seja enviado um valor fora do intervalo, ou um número não inteiro, será retornado o erro absoluto com o inteiro mais próximo da precisão originalmente desejada. 

Exemplo de uso:

```python

valor_real1 = 3.141592
valor_aprox1 = 3.14

ea = erro_absoluto(valor_real1, valor_aprox1)
print(ea)

```

E para o caso onde é especificado a quantidade de casas decimais desejadas:

```python

valor_real1 = 3.141592
valor_aprox1 = 3.14

ea = erro_absoluto(valor_real1, valor_aprox1, 4)
print(ea)

```
Onde 4 é o número de casas decimais de aproximação desejada.

#### Erro Relativo  

Erro absoluto é definido como: 

$|Valor Real - Valor de Aproximação|/|Valor Real|$ 
$$ \frac{|\text{Valor Real} - \text{Valor de Aproximação}|}{|\text{Valor Real}|} $$

Para a função retornar qual o erro relativo de uma dada aproximação, o usuário deve:

- Fornecer o valor original.
- Fornecer a sua aproximação.
- Fornecer, opcionalmente, a quantidade desejada de casas decimais de precisão do erro absoluto.
  
Caso o usuário não indique quantas casas decimais de precisão deseja, ou insira um valor inválido, a função retornará automaticamente o erro com precisão de 7 casas decimais.A maior precisão permitida pela função é de 15 casas decimais, e caso seja enviado um valor fora do intervalo, ou um número não inteiro, será retornado o erro absoluto com o inteiro mais próximo da precisão originalmente desejada. 

Exemplo de uso:

```python

valor_real1 = 3.141592
valor_aprox1 = 3.14

er = erro_relativo(valor_real1, valor_aprox1)
print(er)

```

E para o caso onde é especificado a quantidade de casas decimais desejadas:

```python

valor_real1 = 3.141592
valor_aprox1 = 3.14

er = erro_relativo(valor_real1, valor_aprox1,4)
print(er)

```
Onde 4 é o número de casas decimais de aproximação desejada.

#### Epslon de Máquina 

O epslon da máquina é definido como o menor número que, somado a 1, produz um resultado diferente de 1. Logo, caso o usuário deseje o epslon de máquina basta:

```python

e = epsilon_da_maquina()
print(e)

```
### Interpolação

A interpolação é utilizada para estimar valores desconhecidos de uma função a partir de pontos conhecidos. A biblioteca implementa diferentes métodos de interpolação, que permitem ajustar curvas contínuas aos dados de entrada e avaliar novos valores intermediários.

---

#### Interpolação Linear por Partes

Na interpolação linear por partes, cada par de pontos consecutivos é conectado por uma reta. Esse método fornece uma aproximação simples e contínua da função original, sendo muito eficiente quando os dados apresentam variação quase linear.

Exemplo de uso:

```python
X = [0, 1, 2, 3]
Y = [0, 2, 4, 6]

f = linear_interp(X, Y, plot=True, title="Interpolação Linear por Partes")

print(f(1.5))
```

---

#### Interpolação Polinomial

A interpolação polinomial busca um polinômio que passe exatamente pelos pontos fornecidos. O grau do polinômio depende da quantidade de pontos usados. A biblioteca permite construir esse polinômio por diferentes métodos equivalentes: Lagrange, Newton ou Vandermonde.

Exemplo com o método de Lagrange:

```python
X = [1, 2, 3]
Y = [2, 3, 5]

p = poly_interp(X, Y, method="lagrange", plot=True, title="Interpolação Polinomial - Lagrange")
print(p(2.5))
```

Exemplo com o método de Newton:

```python
p = poly_interp(X, Y, method="newton", plot=True, title="Interpolação Polinomial - Newton")
print(p(2.5))
```

Exemplo com o método de Vandermonde:

```python
p = poly_interp(X, Y, method="vandermonde", plot=True, title="Interpolação Polinomial - Vandermonde")
print(p(2.5))
```

---

#### Interpolação de Hermite

A interpolação de Hermite leva em conta não apenas os valores da função, mas também as derivadas conhecidas nos pontos dados, proporcionando uma curva mais suave que reflete o comportamento local da função.

Exemplo de uso:

```python
x = [0, 1]
deriv = [
    [1, 1],  # f(0) = 1, f'(0) = 1
    [2, 3]   # f(1) = 2, f'(1) = 3
]

H = hermite_interp(x, deriv, plot=True, title="Interpolação de Hermite")
print(H(0.5))
```

### Integração

A função `integral` aproxima o valor da integral definida de uma função real em um intervalo \[a, b\]:

Ela permite escolher entre três métodos numéricos:

- Trapézio  
- Ponto Médio  
- Simpson  

Para usar a função, o usuário deve:

- Fornecer a função `f(x)` a ser integrada ;
- Fornecer o limite inferior `a`;
- Fornecer o limite superior `b`;
- Fornecer o número de subintervalos `n` (inteiro positivo).

Opcionalmente, o usuário pode:

- Escolher o método numérico (`metodo="trapezio"`, `"ponto_medio"` ou `"simpson"`);
- Decidir se quer ou não o gráfico (`plotar=True/False`);
- Ajustar parâmetros visuais do gráfico: `suavidade`, `cor_grafico`, `opacidade_grafico`,
  `cor_area`, `opacidade_area` e `grade`.
---

#### Trapézio

No **método do trapézio**, o intervalo $[a, b]$ é dividido em $n$ subintervalos de largura

$$
\Delta x = \frac{b - a}{n}.
$$

Em cada subintervalo $[x_i, x_{i+1}]$, a função é aproximada por um **segmento de reta**
ligando os pontos $(x_i, f(x_i))$ e $(x_{i+1}, f(x_{i+1}))$.

A área sob a curva nesse pedaço é aproximada pela área de um **trapézio**:

$$
\text{área}_i \approx \frac{f(x_i) + f(x_{i+1})}{2}\. \Delta x.
$$

A integral aproximada é a soma de todas essas áreas.  
Quando `plotar=True`, o gráfico mostra vários trapézios inclinados preenchidos sob a curva.

Exemplo com o método do Trapézio

```python

g = lambda x: math.sin(x)

area = integral(g, 0, math.pi, 100, metodo = "trapezio", cor_grafico="black")
ou
area = integral(g, 0, math.pi, 100, cor_grafico="black")

print("função g com método do trapézio:", area)
```
---

#### Ponto Médio

No **método do ponto médio**, o intervalo $[a, b]$ também é dividido em  $n$ subintervalos de largura $\Delta x = \dfrac{b - a}{n}$.

Em cada subintervalo $[x_i, x_{i+1}]$, calcula-se o **ponto médio**:

$$
x_m = \frac{x_i + x_{i+1}}{2}.
$$

A função é aproximada por um **retângulo** de base $\Delta x$ e altura $f(x_m)$.

A área em cada subintervalo é:

$$
\text{área}_i \approx f(x_m)\.\Delta x.
$$


A integral aproximada é a soma das áreas desses retângulos.  
No gráfico, aparecem retângulos centrados no ponto médio de cada subintervalo.

Exemplo com o método do Ponto Médio

```python
g = lambda x: math.sin(x)

area = integral(g, 0, math.pi, 100, metodo="ponto_medio")
print("função g com método do ponto médio:", area)
```


---

#### Simpson

No **método de Simpson**, cada subintervalo $[x_i, x_{i+1}]$ é tratado junto com seu ponto médio:

$$
x_m = \frac{x_i + x_{i+1}}{2}.
$$

Em vez de usar uma reta ou um retângulo, o método ajusta uma **parábola** que passa pelos três pontos:

$$
(x_i, f(x_i)),\ (x_m, f(x_m)),\ (x_{i+1}, f(x_{i+1})).
$$

A área em cada subintervalo é aproximada por:

$$
\text{área}_i \approx \frac{\Delta x}{6}\cdot\big(f(x_i) + 4f(x_m) + f(x_{i+1})\big).
$$

Somando todas essas áreas, obtém-se a aproximação da integral.  
Quando `plotar=True`, o código desenha a parábola ajustada em cada subintervalo e preenche a área sob essa curva.

---

Exemplo com o método do Simpson

```python
g = lambda x: math.sin(x)

area = integral(g, 0, math.pi, 100, metodo="simpson", opacidade_area=1)
print("função g com método de Simpson:", area)
```


### Raízes

#### Bisseção 
#### Newton - Raphson
#### Secante
#### 1. Método da Bisseção

O **método da bisseção** é o mais simples e estável entre os métodos.  
Ele **reduz progressivamente o intervalo [a, b]** onde há uma mudança de sinal (ou seja, `f(a)` e `f(b)` têm sinais opostos).  
A cada passo, o intervalo é dividido ao meio até encontrar uma aproximação da raiz dentro da **tolerância (`tol`)** definida.

##### Como funciona:
1. Escolha um intervalo `[a, b]` tal que `f(a)` e `f(b)` tenham sinais opostos.  
2. Calcule o ponto médio `c = (a + b)/2`.  
3. Substitua o intervalo por `[a, c]` ou `[c, b]` dependendo do sinal de `f(c)`.  
4. Repita até que a diferença entre os limites seja pequena (ou `f(c)` ≈ 0).

##### Exemplo:
```python
from raizes import bissecao

f = lambda x: x**2 - 4
raiz = bissecao(f, 0, 3)
print(f"Raiz encontrada: {raiz:.6f}")
# Saída: Raiz encontrada: 2.000000
````

##### Vantagens:

* Sempre converge se `f(a)` e `f(b)` têm sinais opostos.
* Muito estável, embora mais lento que Newton.

---

#### 2. Método de Newton-Raphson

O **método de Newton-Raphson** utiliza a **reta tangente** à função para aproximar rapidamente a raiz.
É um método **rápido e eficiente**, mas pode **falhar se a derivada for muito pequena** ou se o ponto inicial for ruim.

##### Como funciona:

1. Comece com uma estimativa inicial `x0`.
2. Atualize o valor com a fórmula:
   [
   x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
   ]
3. Repita até que a diferença entre `x_{n+1}` e `x_n` seja menor que `tol`.

##### Exemplo com derivada:

```python
from raizes import newton_raphson

f = lambda x: x**2 - 4
df = lambda x: 2*x
raiz = newton_raphson(f, 1.0, df)
print(f"Raiz: {raiz:.6f}")
# Saída: Raiz: 2.000000
```

##### Exemplo sem derivada (aproximação numérica):

```python
raiz = newton_raphson(f, 1.0)
print(f"Raiz: {raiz:.6f}")
# Saída: Raiz: 2.000000
```

##### Observações:

* Pode divergir se o ponto inicial for mal escolhido.
* Requer (ou aproxima) a derivada de `f`.

---

#### 3. Método da Secante

O **método da secante** é uma alternativa ao de Newton-Raphson, **dispensando o cálculo da derivada**.
Ele utiliza **duas estimativas iniciais (`a` e `b`)** e traça uma reta entre os pontos `(a, f(a))` e `(b, f(b))`.

##### Como funciona:

1. Escolha dois valores iniciais `a` e `b`.
2. Calcule:
   [
   x_2 = b - f(b) \cdot \frac{b - a}{f(b) - f(a)}
   ]
3. Atualize `a ← b`, `b ← x2` e repita.

##### Exemplo:

```python
from raizes import secante

f = lambda x: x**3 - 9*x + 5
raiz = secante(f, 0, 1)
print(f"Raiz encontrada: {raiz:.6f}")
# Saída: Raiz encontrada: 0.586
```

##### Observações:

* Converge mais rápido que a bisseção, mas pode falhar se `f(a)` e `f(b)` forem iguais.
* Boa escolha quando a derivada é difícil de calcular.

---

#### 4. Bisseção para Múltiplas Raízes

Versão modificada do método da bisseção que **procura várias raízes** em um intervalo, dividindo o intervalo em partes menores e procurando onde há **mudança de sinal**.

##### Exemplo:

```python
from raizes import bissecao_multiraizes

f = lambda x: x**3 - 6*x**2 + 11*x - 6  # Raízes: 1, 2 e 3
raizes = bissecao_multiraizes(f, 0, 4)
print("Raízes encontradas:", raizes)
# Saída: Raízes encontradas: [1.0, 2.0, 3.0]
```

---

#### Função Unificada: `raiz()`

A função `raiz()` serve como uma **interface unificada** para todos os métodos.
Você pode escolher o método desejado por meio do parâmetro `method`.

##### Parâmetros principais:

* `f`: função alvo (`lambda` ou função definida).
* `a`, `b`: intervalo inicial (para bisseção e secante).
* `x0`: aproximação inicial (para Newton-Raphson).
* `df`: derivada de `f` (opcional para Newton-Raphson).
* `method`: `"bissecao"`, `"multbissecao"`, `"secante"` ou `"newton"`.

##### Exemplo de uso:

```python
from raizes import raiz
import math

f = lambda x: x**3 - 9*x + 5
g = lambda x: math.sen(1/x) if x != 0 else 0

# Usando o método da bisseção
r1 = raiz(f, a=0, b=2, method="bissecao")
print(f"Raiz (bisseção): {r1:.6f}")

# Usando o método de múltiplas raízes 
r2 = raiz(g, a=0, b=1, method="multbissecao" )

# Usando Newton-Raphson
r3 = raiz(f, x0=3, method="newton")
print(f"Raiz (Newton-Raphson): {r2:.6f}")

# Usando Secante
r4 = raiz(f, a=0, b=1, method="secante")
print(f"Raiz (Secante): {r3:.6f}")
```

---

##### Visualização Gráfica

Todos os métodos possuem o parâmetro `graf=True`, que exibe **um gráfico interativo** com a função e os pontos aproximados até a convergência (usando `VisualizadorRaizes`).

---

##### Dicas Gerais

* Sempre comece com um **intervalo ou ponto inicial próximo da raiz**.
* Métodos mais rápidos (Newton, Secante) são menos estáveis.
* O método da bisseção **nunca falha se houver mudança de sinal no intervalo**.
* A precisão depende da **tolerância (`tol`)** e do **número máximo de iterações (`max_iter`)**.

---

 **Resumo rápido dos métodos:**

| Método               | Precisa de intervalo? | Precisa de derivada? | Velocidade | Confiabilidade |
| -------------------- | --------------------- | -------------------- | ---------- | -------------- |
| Bisseção             | ✅ Sim                | ❌ Não               | 🐢 Lento   | 💪 Alta        |
| Newton-Raphson       | ❌ (usa x₀)           | ✅ Sim / aproxima    | ⚡ Rápido  | ⚠️ Média       |
| Secante              | ✅ Sim (a, b)         | ❌ Não               | ⚡ Rápido  | ⚠️ Média       |
| Bisseção Multiraízes | ✅ Sim                | ❌ Não               | 🐢 Lento   | 💪 Alta        |
### Aproximação

A aproximação tem como objetivo ajustar funções que não precisam passar exatamente pelos pontos, mas que representem bem o comportamento geral dos dados. A biblioteca implementa métodos para ajustar polinômios, funções exponenciais e também calcular métricas estatísticas de qualidade do ajuste.

#### Polinomial

A aproximação polinomial consiste em encontrar um polinômio que minimize o erro entre os valores observados e os valores previstos. Esta biblioteca oferece dois métodos principais:

Mínimos Quadrados (MQ) — encontra de forma determinística o polinômio que minimiza a soma dos quadrados dos resíduos.

Busca Aleatória — testa coeficientes aleatórios para encontrar um polinômio razoável, útil para explorações iniciais ou validação.

##### Mínimos 

Este método usa álgebra linear para calcular diretamente os coeficientes do polinômio que melhor se ajusta aos dados.

```python
pontos = [
    [0, 1, 2, 3, 4],   # x
    [1, 2, 0, 6, 10]   # y
]

coef = aproximacao_polinomial_mq(pontos, grau=2, plotar=True)
print("Coeficientes:", coef)
```

##### Busca Aleatória

Neste método, coeficientes aleatórios são testados em um intervalo definido, e o polinômio com menor erro é retornado.
Não garante o ótimo global, mas funciona como abordagem heurística.

```python
pontos = [
    [0, 1, 2, 3], 
    [1, 2, 0, 5]
]

melhor = aproximacao_polinomial_aleatoria(
    pontos,
    grau=2,
    expoente=2,
    intervalo=(-2, 2),
    plotar=True
)

print("Melhores coeficientes encontrados:", melhor)
```

#### Exponencial 

A aproximação exponencial busca ajustar uma função do tipo:

$$
y = c \, e^{bx}
$$

Esse tipo de ajuste é útil quando os dados apresentam crescimento ou decaimento exponencial.
A função automaticamente converte o problema para uma regressão linear no logaritmo de 
$y$

Se valores de $y \leq 0$ estiverem presentes, a função poderá:

- lançar erro (comportamento padrão), ou
- descartar pontos inválidos (```ignore_negativos=True```).

```python
pontos = [
    [0, 1, 2, 3],   # x
    [2, 4, 9, 20]   # y
]

c, b = aproximacao_exponencial(pontos, plotar=True)
print("c =", c, "b =", b)
```

#### Cálculo de Resíduos
A qualidade de um ajuste pode ser medida pela diferença entre os valores reais e os valores previstos.
A biblioteca implementa funções clássicas da análise de regressão:

##### SSR - Soma dos Quadrados dos Resíduos

$$
SSR = \sum (y_i - \hat{y}_i)^2
$$

Medida de erro total do ajuste.

```python
ssr = SSR(pontos, coef)
print("SSR:", ssr)
```

##### SST - Soma Total dos Quadrados

$$
SST = \sum (y_i - \bar{y})^2
$$

Representa a variação total dos dados — usada como referência para normalizar o erro.

```python
sst = SST(pontos, coef)
print("SST:", sst)
```

##### R² - Coeficiente de Determinação

$$
R^2 = 1 - \frac{SSR}{SST}
$$

Valores próximos de 1 indicam bom ajuste.

```python
r2 = R2(pontos, coef)
print("R²:", r2)
```

#### Seleção Automática do Grau Polinomial (BIC)
Método para escolher automaticamente o grau ótimo do polinômio usando o Critério de Informação Bayesiano (BIC).

A função testa graus dentro de um intervalo e retorna:
- grau selecionado
- coeficientes
- lista de graus testados
- valores de BIC correspondentes

```python
d_best, coef_best, graus, bics = encontrar_grau_polinomial_bic(
    pontos,
    d_min=0,
    d_max=6,
    plotar=True
)

print("Melhor grau:", d_best)
print("Coeficientes:", coef_best)
```


### Soma de Kahan 
A soma de Kahan é uma forma de minimizar os erros de cancelamento gerados ao somar números grandes com números pequenos.
Caso o usuário deseje utilizar essa função basta fornecer uma lista contendo os números que deseja somar. 
Existem duas funções no arquivo:

- soma_normal_lista(x)
- soma_de_kahan_lista(x)

Onde a segunda função é a que de fato faz e retorna a soma de Kahan e a primeira função serve apenas de comparação, pois é um somatório normal dos elementos da lista.

Segue um exemplo de como implementar:

```python

lista = [10000, 5.29476, 2.25958]

soma = soma_de_kahan_lista(lista)
print("Soma Kahan", soma)

```

