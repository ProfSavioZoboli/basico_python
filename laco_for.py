# Algumas vezes precisamos de um laço de repetição para redução da quantidade de código
# Isso visa diminuir a quantidade de código do programa, facilitar a manutenção e descomplicar o programa.

# Conseguimos utilizar com um contador

print("#### Com o contador ####")

contador = 1

for index in range(1,10): # Quando queremos contar com valores fixos, usamos o range
    contador += 1

print("O valor depois do laço é ",contador)

print("\n")

# Podemos também iterar em uma palavra, pois cada letra é um caractere
print("#### Escrita ####")

palavra = 'python'

for letra in palavra:
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print('A letra ',letra,' é uma vogal')
    else:
        print('A letra ',letra,' é uma consoante')

print("\n")
# Podemos também iterar entre as posições de um array ou tupla
print("#### Array ####")

frutas = ['banana','maçã','melão']

for fruta in frutas:
    print(fruta)
