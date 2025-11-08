'''
código que calcula o erro relativo e absoluto entre o valor real e uma 
aproximação, sendo o erro absoluto = | valor real - valor aproximado| 
e o erro relativo = | valor real - valor aproximado| / | valor real| 

Para os códigos, foi definido como padrão arredondar até 7 casas decimais de precisão para
a representação do erro relativo e absoluto, ou seja, se não for passado um parâmetro
de quantas casas decimais os erros apresentarão, então vai retornar com 7 casas decimais 
de precisão. Além disso, foi determinado que caso uma quantidade de casas decimais inválida seja
passado ( exemplo: número negativo, float, ou que seja maior ou igual a 16), a precisão que o python
vai retornar é com o número de casas decimais mais próximo do valor inválido originalmente
fornecido. O intervalo de números inteiros válidos é de entre 0 e 15 uma vez que o padrão IEEE754
tem precisão exata em apenas cerca de no máximo 15 ou 16 dígitos decimais (inclui a parte inteira 
e parte decimal))

Também fará uma verificação para saber se o valor passado pelo usuário como número de casas decimais de precisão 
era um número ( int ou float).Se não for, como uma string, é retornado o erro com 7 casas decimais de precisão. 
Além disso, em ambos os erros, é verificado se o valor e o valor aproximado são inteiros ou floats. Se não forem,
é retornado uma mensagem de que o tipo das variáveis são inválidas


O epsilon da máquina é, por definição, o menor número que somado a 1 produza um resultado diferente de 1

'''
def erro_absoluto(valor,aprox,casas_decimais_de_precisao =7):
    ''' define o erro absoluto conforme a explicação anterior. casas_decimais_de_precisao 
    começa com 7 caso nenhum valor tenha sito passado'''
    if (not isinstance(valor,int) and not isinstance(valor,float)) or (not isinstance(aprox,int) and not isinstance(aprox,float)):
        return("valor e/ou valor aproximado não está com tipo válido( inteiro ou float)")
    # faz uma verificação se os valores passados para calcular o erro são inteiros ou floats. Se não forem, é retornado uma mensagem dizendo que os valores não eram válidos
    if isinstance(casas_decimais_de_precisao,int) and 0 <= casas_decimais_de_precisao < 16:
        '''verifica se o numero de casas de precisão é inteiro e se está dentro do intervalo'''
        return(round(abs(valor-aprox),casas_decimais_de_precisao))
    elif not isinstance(casas_decimais_de_precisao,int) and not isinstance(casas_decimais_de_precisao,float):
        return (round(abs(valor-aprox),7))
    else:
        p = 0 # começa com o numero de casas decimais de precisão sendo igual a 0
        k = erro_absoluto(casas_decimais_de_precisao,0,2) # guarda " quao distante está" do 0 
        for i in range(16): # faz essa verificação para todos os inteiros válidos para representação decimal
            g = erro_absoluto(casas_decimais_de_precisao,i,2)
            if g < k: # e vai utilizar aquele que mais se aproxima
                k = g
                p = i # valor de casas decimais é atualizado quando está mais proximo   
        return(round(abs(valor-aprox),p))
def erro_relativo(valor,aprox, casas_decimais_de_precisao = 7):
    
    ''' define o erro relativo conforme a explicação anterior. casas_decimais_de_precisao 
    começa com 7 caso nenhum valor tenha sito passado. As outras verificações são similares
    às verificações do erro relativo'''
    if (not isinstance(valor,int) and not isinstance(valor,float)) or (not isinstance(aprox,int) and not isinstance(aprox,float)):
        return("valor e/ou valor aproximado não está com tipo válido( inteiro ou float)")
    resposta = abs(valor-aprox)/abs(valor)
    if  isinstance(casas_decimais_de_precisao,int) and 0 <= casas_decimais_de_precisao < 16:
        return(round(resposta,casas_decimais_de_precisao))
    elif not isinstance(casas_decimais_de_precisao,int) and not isinstance(casas_decimais_de_precisao,float):
        return (round(resposta,7))
    else:
        p = 0
        k = erro_absoluto(casas_decimais_de_precisao,0,2)
        for i in range(16):
            g = erro_absoluto(casas_decimais_de_precisao,i,2)
            if g < k:
                k = g
                p = i   
        return(round(resposta,p))
def epsilon_da_maquina():
    '''retorna o epsilon de maquina, caso o usuário queira'''
    epsilon = 1
    while 1+ epsilon != 1:
        epsilon = epsilon/2
    return( 2*epsilon )
		

	
