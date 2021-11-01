nome = input('Qual seu nome? ')  # print(significa escreva) e input(significa leia) são funções.
# O input, por padrão, sempre recebe o valor digitado pelo usuário como string, então as vezes tem que converter para outro tipo de dado.
print('Olá', nome, '! Prazer em te conhecer!', nome, ', você parece ser muito legal!')
print('Olá, {}! Prazer em te conhecer! {}, você parece ser muito legal!'.format(nome, nome))
# tive que colocar dois argumentos para método  .format. Será que precisa mesmo?
print('E quando você nasceu?')
dia = int(input("Dia? "))
mes = input('O mês? ')
ano = int(input('E o ano? '))
print('Que legal. Então', nome, ', você nasceu em', dia, 'de', mes, 'de', ano, '. Correto?')
atual = int(input('Em que ano nos estamos? '))
print(atual + ano)  # Aqui estou usando as variáveis, então pra variável não se usa aspas, senão vira uma string.
print(atual - ano)
print('Então você tem', (atual - ano), 'anos.')
print('Então, se estamos em {} e você nasceu em {}, hoje você tem'.format(atual, ano), (atual - ano), 'anos.')
# O .format tem que estar "colado" junto a parte da frase onde irão as variáveis e não no final do texto.

print(type(mes))
print(type(atual))
print(float(atual)) # Converteu o int em ponto flutuante.
print(bool(atual)) # Converteu o int em boleano, e como tem um valor dentro, considerou como verdadeiro.
print(bool(0)) # Zero para boleano é falso.
print(bool()) # Vazio também é falso para boleano.
print(mes.isalpha(),mes.islower(),mes.isnumeric(),mes.isspace(),mes.isprintable(),mes.isupper())

# tipos primitivos em Python são int (9, -3, 1981), float (0.6, 3.69, -23145.35, 9.0, sendo que no Python usamos  .  ), bool (True e False, apenas),
# string (texto diverso com tudo que é possível, sempre entre " ou  ' , inclusive tendo string vazia com "" ou '').
# Método .isnumeric confere se o valor é numérico e .isalpha confere se são letras. E .isalnum confere se é alfanumérico. E temos outros métodos.
