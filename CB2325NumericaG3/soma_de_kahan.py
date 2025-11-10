
'''
Código para minimizar erros de cancelamento.

A soma de números grandes com números pequenos geralmente causa um erro de 
cancelamento. A soma de kahan busca minimizar esses erros de cancelamento ao 
"salvar" em comp_erro as partes "pequenas" que seriam normalmente descartadas 
'''

def soma_normal_lista(x):
    """
    Faz a soma  da maneira usual dos números da lista.
    """
    s = 0.0
    for i in x:
        s = s + i
    return s

def soma_de_kahan_lista(x):
    """
    Faz a soma com compensação de erro.
    """
    soma_acumulada = 0.0  # soma acumulada
    comp_erro = 0.0  # compensação de erro
    for numero in x:
        y = numero - comp_erro
        t = soma_acumulada+ y 
        comp_erro = (t - soma_acumulada) - y 
        soma_acumulada = t
    return soma_acumulada


