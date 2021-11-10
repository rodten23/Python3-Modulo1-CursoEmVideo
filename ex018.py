# Relativo até Aula 08
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math # Lembrar que não precisa importar o módulo completo.
angulo = float(input('Favor, digite o valor do ângulo: '))
print('Para o ângulo {}º temos o seno de {:.2f}, o cosseno de {:.2f} e a tangente de {:.2f}.'.format(angulo, math.sin(math.radians(angulo)), math.cos(math.radians(angulo)), math.tan(math.radians(angulo))))
