import sys
sys.path.append(".")
from CB2325NumericaG3.soma_de_kahan import soma_normal_lista, soma_de_kahan_lista

if __name__ == '__main__':
    x = [1e-10] * 10000 + [1.0] # Primeiro vários pequenos depois um grande.
    print("Soma (pequenos -> grande) ")
    print(f"Soma normal: {soma_normal_lista(x)}")
    print(f"Soma Kahan : {soma_de_kahan_lista(x)}")

    x_invertido = [1.0] + [1e-10] * 10000 # Agora sim, um grade + vários pequenos, deveria dar a mesma resposta.

    print("Soma na ordem invertida (grande -> pequenos)")
    print(f"Soma normal (invertida): {soma_normal_lista(x_invertido)}")
    print(f"Soma Kahan (invertida) : {soma_de_kahan_lista(x_invertido)}")

    # exemplo 2:

    lista = [10000, 3.14159, 2.71828]
    # Essa soma deveria dar 10005.85987; observe qual dos dois métodos mais se aproxima dessa soma:
    print(f"Soma normal: {soma_normal_lista(lista)}")
    print(f"Soma Kahan : {soma_de_kahan_lista(lista)}")
