# Atribuição de variáveis e tipos primitivos

# Para atribuir o valor a uma variável, informamos o nome dela, o sinal de atribuição (=) e o valor que queremos armazenar

# Quando informamos texto, colocamos esses dados entre aspas simples. Algumas linguagens diferenciam tipos de dados entre aspas simples e aspas duplas
# Python não é uma delas.

# Algumas linguagens de programação são fortemente tipadas, o que indica que as variáveis precisam ter um tipo informado que não pode ser alterado
# Python também não é uma delas.
# Exemplo dessas linguagens
# Java          ->      String nome = "Alberto"
# Typescript    ->      nome:string = "Alberto"

# Escrita é do tipo String (str) que é basicamente uma cadeia de caracteres
nome = 'Alberto'
sobrenome = "Malvadives"

# valores sem casa decimal são do tipo inteiro (int)
idade = 25

# Valores com casa decimal são do tipo float (ponto flutuante)
# Não deve-se colocar separador de milhar. O separador decimal deve ser ponto (.)
altura = 1.75

# Para dados que são verdadeiro e falso, deve-se utilizar as palavras reservadas True (Verdadeiro) e False (Falso).
is_casado = False

print("Nome é do tipo: ",type(nome))
print("Sobrenome é do tipo: ",type(sobrenome))
print("Idade é do tipo: ",type(idade))
print("Altura é do tipo: ",type(altura))
print("Casado é do tipo:",type(is_casado))