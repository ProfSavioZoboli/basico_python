# para fazer os cálculos, utilizamos variáveis e atribuições, além dos sinais matemáticos

# + adição
# - subtração
# * multiplicação
# / divisão
# // divisão com resultado inteiro
# % Módulo, pegará o resto da divisão (divide o valor até não ser mais possível um resultado inteiro, retorna o valor que sobra) 5/2 = 4, sobrando 1. Nesse caso o resultado é 1
# ** Exponenciação, também conhecido como Potenciação

val_a = 5
val_b = 2

res_adicao = val_a + val_b
res_subtracao = val_a - val_b
res_multiplicacao = val_a * val_b
res_divisao = val_a / val_b
res_divisao_inteira = val_a // val_b
res_modulo = val_a % val_b
res_exponenciacao = val_a ** val_b

print("Resultados:")
print(val_a,"+",val_b,"=",res_adicao)
print(val_a,"-",val_b,"=",res_subtracao)
print(val_a,"*",val_b,"=",res_multiplicacao)
print(val_a,"/",val_b,"=",res_divisao)
print(val_a,"//",val_b,"=",res_divisao_inteira)
print(val_a,"%",val_b,"=",res_modulo)
print(val_a,"**",val_b,"=",res_exponenciacao)

# Também é possível realizar cálculos e reatibuir ao valor da variavel

contador = 1
contador += 1

print("O valor de contador é ",contador)