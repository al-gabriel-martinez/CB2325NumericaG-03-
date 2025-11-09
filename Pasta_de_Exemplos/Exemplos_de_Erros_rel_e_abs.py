from CB2325NumericaG3.erros import erro_absoluto, erro_relativo, epsilon_da_maquina 
# Exemplos de como usar
valor_real1 = 3.141592
valor_aprox1 = 3.14

ea = erro_absoluto(valor_real1,valor_aprox1)
er = erro_relativo(valor_real1,valor_aprox1)
print(ea, er)
##########################################################################################

# com 4 casas decimais 
valor_real = 3.141592
valor_aprox = 3.14

ea = erro_absoluto(valor_real,valor_aprox,4) # colocando com quantas casas de presição deseja arredondar
er = erro_relativo(valor_real,valor_aprox,4)

print(ea,er)

####################################################################################################

valor_real = 1.123456789012345678
valor_aprox = 1

ea = erro_absoluto(valor_real,valor_aprox,17)
er = erro_relativo(valor_real,valor_aprox,17)

print(ea,er)

##################################################################################################

valor_real = 1.123456789012345678
valor_aprox = 1

ea = erro_absoluto(valor_real,valor_aprox,6.5)
er = erro_relativo(valor_real,valor_aprox,3.4) # nesse caso, arredondaria para 3 casas decimais
# de precisão, porém como o erro relativo é 0.10989... ao arredondar para 3 casas decimais de precisão 
# obtemos o valor esperado de 0.11

print(ea,er)


################################################
valor_real = 1.123456789012345678
valor_aprox = 1

ea = erro_absoluto(valor_real,valor_aprox,"c") # testando caso não seja enviado um número ( inteiro ou float) como casas decimais
er = erro_relativo(valor_real,valor_aprox,"3") 

print(ea,er)

##################################################################################################

valor_real = "oi"
valor_aprox = 1

ea = erro_absoluto(valor_real,valor_aprox,6) # testando caso não seja enviado um número ( inteiro ou float) como valor real
er = erro_relativo(valor_real,valor_aprox,3) 

print(ea)
print(er)

########################################################################################################
valor_real = 7
valor_aprox = "2.8"

ea = erro_absoluto(valor_real,valor_aprox,6) # testando caso não seja enviado um número ( inteiro ou float) como valor aproximado
er = erro_relativo(valor_real,valor_aprox,3) 

print(ea)
print(er)

############################################################################################################
e = epsilon_da_maquina()
print(e)

###################################################################################################

valor_real = 789
valor_aprox = 569.13456896543

ea = erro_absoluto(valor_real,valor_aprox,12)
er = erro_relativo(valor_real,valor_aprox,12) 

print(ea)
print(er)
