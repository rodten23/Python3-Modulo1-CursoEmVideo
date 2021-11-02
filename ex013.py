# Relativo até Aula 07
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Favor, qual seu salário? R$ '))
aumento = 15
print('Seu salário, com aumento de 15%, ficará em R$ {:.2f}.'.format(salario+(salario*(aumento/100))))
print('Seu salário, com aumento de 15%, ficará em R$ {:.2f}.'.format(salario+(salario*aumento/100)))