# Relativo até Aula 07
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

seud = float(input('Quanto dinheiro você tem na carteira?  R$  '))
dolar = 5.67
print('Com a cotação do dólar em {}, hoje seu dinheiro vale {:.2f} dólares.'.format(dolar, seud/dolar))