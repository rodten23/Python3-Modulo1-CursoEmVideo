# Relativo até Aula 07
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Símbolo % não funciona como Porcentagem no Python, então não pode ser usado.

preco = float(input('Qual o preço do produto? R$  '))
desconto = 5
print('Com o desconto de 5%, pelo produto que tinha o preço de {:.2f}, você pagará agora {:.2f}.'.format(preco, preco*((100-desconto)/100)))
