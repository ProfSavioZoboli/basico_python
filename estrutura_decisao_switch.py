# Em alguns casos precisamos analisar o valor de uma variável e decidir sobre vários valores
# Para isso, usamos a estrutura Match, onde informamos a variável para verificação e cada resposta dependendo do valor
# Só consegue ser utilizada quando as comparações são de escopo IGUAL

# Erros, principalmente HTTP possuem numerações que nos ajudam a descobrir o motivo do erro. Mas isso é papo para mais tarde.
codigo_erro = 401

match codigo_erro:
    case 0:
        print("Erro desconhecido")
    case 200:
        print("Ok")
    case 201:
        print("Criado")
    case 400:
        print("Faltando informações")
    case 401:
        print("Não autorizado")
    case 500:
        print("Erro geral do servidor")
    case _: # Usar o _ significa que se não houver nenhuma correspondência aos casos anteriores, o código abaixo será executado
        print("Erro não capturado")

# Em outras linguágens de programação, essa estrutura é conhecida como switch, e o caso padrão (_) é escrito como default:
# Exemplo do padrão dessa estrutura em outras linguagens de programação

#switch (codigo_erro){
#    case 0:
#        print("Erro desconhecido")
#    case 200:
#        print("Ok")
#    case 201:
#        print("Criado")
#    case 400:
#        print("Faltando informações")
#    case 401:
#        print("Não autorizado")
#    case 500:
#        print("Erro geral do servidor")
#    default:
#        print("Erro não capturado")
#}