"""
Módulo para cálculo de erros absoluto e relativo e do epsilon da máquina.

Funções fornecidas:
- erro_absoluto(valor, aprox, casas_decimais=7)
- erro_relativo(valor, aprox, casas_decimais=7)
- epsilon_da_maquina()

Detalhes:
- O padrão é arredondar os erros para 7 casas decimais.
- Se o número de casas decimais informado for inválido (negativo, float ou >= 16),
  será usado o valor inteiro mais próximo no intervalo [0, 15].
- Se o valor de quantidade de casas decimais passada não for um inteiro, nem um float,
  como uma string, será arredondado automaticamente para 7 casas decimais
- Verifica se os valores passados para "valor" e "aprox" são inteiros ou floats; caso contrário, retorna uma mensagem de erro.
- O epsilon da máquina é definido como o menor número que, somado a 1, produz um resultado diferente de 1.
"""
def erro_absoluto(valor, aprox, casas_decimais=7):
    """
    Calcula o erro absoluto entre um valor real e uma aproximação.

    Fórmula dada por: |valor real - valor aproximado| 
	
	Parâmetros:
    valor (int ou float): Valor real.
    aprox (int ou float): Valor aproximado.
    casas_decimais (int, opcional): Número de casas decimais para arredondamento (padrão = 7).

    Retorna:
    float ou str: Erro absoluto arredondado ou mensagem de erro se os tipos forem inválidos.
    """
    if (not isinstance(valor, int) and not isinstance(valor, float)) or (not isinstance(aprox, int) and not isinstance(aprox, float)):
        return("valor e/ou valor aproximado não está com tipo válido( inteiro ou float)")
    if isinstance(casas_decimais, int) and 0 <= casas_decimais < 16:
        """Verifica se o numero de casas de precisão é inteiro e se está dentro do intervalo."""
        return(round(abs(valor - aprox),casas_decimais))
    elif not isinstance(casas_decimais, int) and not isinstance(casas_decimais, float):
        return (round(abs(valor - aprox), 7))
    else: # Procura qual o inteiro mais próximo.
        p = 0 # Salva o inteiro mais próximo.
        k = erro_absoluto(casas_decimais, 0, 2) # Guarda a menor distância entre o valor inválido e o inteiro desejado.
        for i in range(16): # # Procura qual o inteiro mais próximo.
            g = erro_absoluto(casas_decimais, i, 2)
            if g < k: # Vai utilizar a menor distância.
                k = g
                p = i # Valor de casas decimais é atualizado.  
        return(round(abs(valor - aprox),p))
def erro_relativo(valor, aprox, casas_decimais=7):
    """
    Calcula o erro relativo entre um valor real e uma aproximação.

    Fórmula: |valor real - valor aproximado| / | valor real| 
	
	Parâmetros:
    valor (int ou float): Valor real.
    aprox (int ou float): Valor aproximado.
    casas_decimais (int, opcional): Número de casas decimais para arredondamento (padrão = 7).

    Retorna:
    float ou str: Erro absoluto arredondado ou mensagem de erro se os tipos forem inválidos.
    """    
    if (not isinstance(valor, int) and not isinstance(valor, float)) or (not isinstance(aprox, int) and not isinstance(aprox, float)):
        return("valor e/ou valor aproximado não está com tipo válido( inteiro ou float)")
    if valor == 0:
        raise ZeroDivisionError("Erro relativo não definido: Valor real é zero.")
    resposta = abs(valor - aprox)/abs(valor)
    if  isinstance(casas_decimais, int) and 0 <= casas_decimais < 16:
        return(round(resposta,casas_decimais))
    elif not isinstance(casas_decimais, int) and not isinstance(casas_decimais, float):
        return (round(resposta,7))
    else:
        p = 0
        k = erro_absoluto(casas_decimais, 0, 2)
        for i in range(16):
            g = erro_absoluto(casas_decimais, i, 2)
            if g < k:
                k = g
                p = i   
        return(round(resposta, p))
def epsilon_da_maquina():
    """
	Retorna o epsilon de máquina.

	Retorna:
	float
	"""
    epsilon = 1
    while 1 + epsilon != 1:
        epsilon = epsilon/2
    return( 2*epsilon )
		
