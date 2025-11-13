# CB2325NumericaG3
Biblioteca de Cálculo Numérico em Python para AV2 da Disciplina de Programação 2 do IMPA Tech - Grupo 03


**Participantes:**

* Anízio Silva Correia Júnior
* Cristiane Magarinos Sampaio
* Davi Bezerra Leal Guimarães
* Felipe Lima De Sousa
* Felipe Ribeiro Medonça
* Gabriel Falcão Martinez
* Guilherme Oséias Pereira Da Silva
* Heitor Ramos Pereira
* joão Pedro Lima de Almeida
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

### Raízes
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

### Soma de Kahan 
A soma de Kahan é uma forma de minimizar os erros de cancelamento gerados ao somar números grandes com números pequenos.
Caso o usuário deseje utilizar essa função basta fornecer uma lista contendo os números que deseja somar. 

```python

lista = [10000, 5.29476, 2.25958]

soma = soma_de_kahan_lista(lista)
print("Soma Kahan", soma)

```

