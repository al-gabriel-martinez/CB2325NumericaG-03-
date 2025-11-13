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

$ |Valor Real - Valor de Aproximação|\|Valor Real|$ 

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

### Aproximação

### Soma de Kahan 
A soma de Kahan é uma forma de minimizar os erros de cancelamento gerados ao somar números grandes com números pequenos.
Caso o usuário deseje utilizar essa função basta fornecer uma lista contendo os números que deseja somar. 

```python

lista = [10000, 5.29476, 2.25958]

soma = soma_de_kahan_lista(lista)
print("Soma Kahan", soma)

```

