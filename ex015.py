# Relativo até Aula 07
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
# o carro custa R$60 por dia e R$0,15 por Km rodado.

corrida = float(input('Favor, informe a quantos Km percorreu no período: '))
dias = int(input('E ficou com o carro por quantos dias: '))
custo_km = 0.15
custo_d = 60
print('Se você percorreu {:.2f}km e ficou com o carro por {} dias, o valor total a pagar será de R$ {:.2f}.'.format(corrida, dias, (corrida*custo_km+dias*custo_d)))

