# Relativo até Aula 08
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
n1 = input('Nome do(a) primeiro(a) aluno(a): ')
n2 = input('Nome do(a) segundo(a) aluno(a): ')
n3 = input('Nome do(a) terceiro(a) aluno(a): ')
n4 = input('Nome do(a) quarto(a) aluno(a): ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: {}.'.format(lista))

