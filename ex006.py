# Relativo até Aula 07
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

alvo = int(input('Favor, digite um número:  '))

# Não criei outras variáveis porque bastava fazer os cálculos direto no .format, mas se precisar usar em outras partes, precisará das variáveis.

print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(alvo, alvo*2, alvo*3, alvo**(1/2)))
print('O dobro de {} é {} e seu triplo é {}.\nAlém diso, sua raiz quadrada é {:.2f}.'.format(alvo, alvo*2, alvo*3, alvo**(1/2)))

# Perceber que o :.2f fez um arredondamento.
