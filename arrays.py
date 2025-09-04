# quando uma variavel possui diversos valores, ou uma coleção de valores, chamamos isso de vetor, ou array.
# os vetores podem ser modificados, podendo receber ou perder valores

# São representados por valores separados por vírgula e entre colchetes
# definimos geralmente o nome dessas variaveis com seu nome no plural

# A contagem dos itens do array começa a partir do 0

frutas = ['banana','maçã','uva']

print(frutas)

# podemos adicionar novos elementos no array usando a função append. Ela inserirá o valor no final do array
frutas.append('bergamota')

print(frutas)

# podemos substituir itens em algum indice específico
frutas.insert(1,'ameixa')

print(frutas)

# podemos retirar itens do array usando a função pop e informando o indice dela

frutas.pop(2) # remove o terceiro item do array, no caso o item Uva

print(frutas)

# Podemos também remover um item especifico usando o seu valor

frutas.remove('banana')

print(frutas)

# Para eu ler o valor de um indice especifico, podemos utilizar um colchetes após o nome da variavel, e então o programa acessará essa posição do array
print('A segunda fruta do vetor é ',frutas[1])