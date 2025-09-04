# Estrutura de decisão é usada quando precisamos seguir algum caminho com base em uma comparação

# Ex.: só podemos deixar que o usuário entre no sistema se ele for maior de 13 anos

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

# Para decidirmos, utilizamos o comando if (se)
# Os blocos de resposta precisam estar um nível para dentro na identação, para que o python entenda qual código deve ser executado
print("#### APENAS IF E ELSE ####")

if idade >= 13:     # Podemos traduzir como: Se idade é maior ou igual a 13
    print("Acesso liberado")
else:               # Else traduzimos como senão, ou seja, será executado caso o resultado do IF seja falso.
    print("Acesso bloqueado")


# E se quisermos utilizar controle parental, por exemplo?
# Não deixar entrar com menos de 13 anos, utilizar controle parental entre 13 e 18 anos, e liberar acesso total acima de 18 anos
# Para isso precisamos verificar 2x a idade, uma para verificar que é maior de 13 anos e outra verificar se é maior de 18 anos

print("#### IF ELIF ELSE ####")

if idade < 13:      # Verifica se é menor de 13 anos, para bloquear o acesso
    print("Acesso bloqueado")
elif idade < 18:    # Verifica se é menor de 18 anos (não precisamos verificar se é menor de 13 nesse caso, pois isso já foi validado no if anterior)
    print("Controle parental")
else:               # Entrará no else se não for menor de 13 nem menor de 18, conforme validado nos ifs anteriores
    print("Acesso liberado")

