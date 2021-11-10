# Relativo até Aula 07
# Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.

celsius = float(input('Favor, informe a temperatura em graus Celsius: '))
#cal_fahrenheit = ((9*celsius)/5)+32  Pode ser usado da forma abaixo, sem parênteses,
# pois de qualquer jeito obedecerá a ordem de precedência.
cal_fahrenheit = 9 * celsius / 5 + 32
print('A temperatura de {:.1f} ºC corresponde a {:.1f}ºF!'.format(celsius, cal_fahrenheit))
print('A temperatura de {0} ºC corresponde a {1}ºF!'.format(celsius, cal_fahrenheit))  # O zero e o um nas
# máscaras neste caso são índices para indicar a ordem de inserção das variáveis,
# pois se necessários, a ordem pode ser alterada.

fahrenheit  = float(input('Favor, informe a temperatura em graus Fahrenheit : '))
cal_celsius = (fahrenheit - 32) / (9 / 5)
print('A temperatura de {:.1f} ºF corresponde a {:.1f}ºC!'.format(fahrenheit, cal_celsius))