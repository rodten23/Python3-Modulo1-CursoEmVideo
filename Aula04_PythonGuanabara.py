print('Olá, Mundo!') #pode ser aspas simples ou duplas. Maioria usa simples
print(9+6)
print('9'+'6')
#print('Olá'+9) isso dá erro
print('Olá',9) #isso dá certo (concatenação). As vezes terá ser + e as vezes terá que ser ,

nome='Rodrigo'
idade=40
peso=113.9
print(nome,idade,peso) #Não pode ser + porque só concatena strings ou faz soma de números. Então somar ou
#concatenar strings com números ele não faz.

nome=input('Qual seu nome? ') #print(significa escreva) e input(significa leia) são funções.
print('Olá',nome,'! Prazer em te conhecer!',nome,', você parece ser muito legal!!!')
print('E quando você nasceu?')
dia=input("Dia? ")
mes=input('O mês? ')
ano=input('E o ano? ')
print('Que legal. Então',nome,', você nasceu em',dia,'de',mes,'de',ano,'. Correto?')
atual=input('Em que ano nos estamos? ')
print(atual+ano)
print('Então você tem', (atual-ano), 'anos.')
