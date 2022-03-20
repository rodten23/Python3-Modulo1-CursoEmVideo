# Relativo até Aula 09
# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Por favor, informe seu nome: ')).strip()
print('Você faz parte da família Silva? {}'.format('SILVA' in nome.upper()))

