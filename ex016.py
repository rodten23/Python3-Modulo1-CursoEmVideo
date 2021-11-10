# Relativo até Aula 08
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

from math import trunc
numero = float(input('Favor, digite um número: '))
print('O valor digita foi {} e sua porção inteira é {:.0f}.'.format(numero, numero)) # Nessa versão, tomar cuidado pois faz arredondamento.
print('O valor digita foi {} e sua porção inteira é {}.'.format(numero, int(numero)))
print('O valor digita foi {} e sua porção inteira é {}.'.format(numero, trunc(numero)))
