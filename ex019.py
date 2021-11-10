# Relativo até Aula 08
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

alunos = ['Rodrigo', 'Sara', 'Melissa', 'Miguel']
print('{} ajudará o professor hoje.'.format(random.choice(alunos)))

n1 = input('Primeiro(a) aluno(a): ')
n2 = input('Segundo(a) aluno(a): ')
n3 = input('Terceiro(a) aluno(a): ')
n4 = input('Quarto(a) aluno(a): ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) # As vezes, é melhor criar a variável, pois assim poderá usá-la em várias partes do programa.
print('{} ajudará o professor hoje.'.format(escolhido))

