# Relativo até Aula 07
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Quer a tabuada de qual número?  '))
print('A tabuada de {} é {}, {}, {}, {}, {}, {}, {}, {}, {} e {}.'.format(numero, numero*1, numero*2, numero*3, numero*4, numero*5, numero*6, numero*7, numero*8, numero*9, numero*10))
print('*'*15)
print('A tabuada de {} é\n{} x 1 = {:>2}\n{} x 2 = {:>2}\n{} x 3 = {:>2}\n{} x 4 = {:>2}\n{} x 5 = {:>2}\n{} x 6 = {:>2}\n{} x 7 = {:>2}\n{} x 8 = {:>2}\n{} x 9 = {:>2}\n{} x 10 = {:>2}'.format(numero, numero, numero*1, numero, numero*2, numero, numero*3, numero, numero*4, numero, numero*5, numero, numero*6, numero, numero*7, numero, numero*8, numero, numero*9, numero, numero*10))
print('*'*15)