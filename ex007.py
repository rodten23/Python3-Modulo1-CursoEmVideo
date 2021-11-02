# Relativo até Aula 07
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Em Python, as variáveis podem ter acento, mas não podem começar com números.

nota1 = float(input('Sua primeira nota foi: '))
nota2 = float(input('Sua segunda nota foi: '))
print('Com suas notas a média foi de {:.2f}.'.format((nota1+nota2)/2))