# Usando exemplo de comidas do Guanabara:
# Basicamente, são duas formas de importar módulos no Python.

# import bebida  trará todos os itens do módulo bebida
# from doce import pudim  trará apenas a funcionalidade pudim do módulo doce, sem as outras funcionalidades, que no momento não são
# necessárias e aumentariam o tamanho do programa a toa.


import math  #  Assim vem tudo do módulo math

# from math import sqrt, ceil, floor  Trará apenas a funcionalidade sqrt, ceil e floor e direto para a página do códido, então no código eu
# colocarei direto sqrt(Num), sem precisar "chamar" (referenciar) antes o math

Num = int(input('Digite um número: '))  # Posso criar variáveis com letras maísculas, mas não é recomendado pelas Boas Práticas.
raiz = math.sqrt(Num)
print('A raiz quadrada de {} é igual a {}.'.format(Num, math.ceil(raiz)))  # Arredondado pra cima
print('A raiz quadrada de {} é igual a {}.'.format(Num, raiz))  # Sem arredondamento
print('A raiz quadrada de {} é igual a {}.\n'.format(Num, math.floor(raiz)))  # Arredondado pra baixo


import random # biblioteca para criar números aleatórios
num = random.random()
num_int = random.randint(3, 30)
print(num)
print(num_int)

# Se der import e Ctrl+espaço eu consigo ver o que posso importar por padrão no Python

import emoji  # Consigo importar uma biblioteca direto no Pycharm pela lampadinha vermelha.
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases=True))
