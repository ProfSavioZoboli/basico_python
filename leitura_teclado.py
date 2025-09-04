# Na maioria dos casos, o programa precisa interagir com o usuário para fazer o que deve ser feito
# Para isso, utilizamos o comando input, e passamos a pergunta que deve aparecer ao usuário como parâmetro.
# O valor recebido deve ser armazenado em uma variável

nome = input("Digite o seu nome: ")

# O valor padrão é sempre string, portanto quando solicitamos que o usuário digite algum número, esse valor precisa ser convertido

idade = int(input("Digite a sua idade"))

print("Olá",nome,"!",type(nome))
print("Você tem ",idade," anos",type(idade))
