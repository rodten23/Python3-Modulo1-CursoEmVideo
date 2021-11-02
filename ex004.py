#Relativo até Aula 06
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

palavra = input('Favor, digite algo:  ')
print('O tipo primitivo desse valor é', type(palavra))
print('Só tem espaços?', palavra.isspace()) # Os () indicam que é um método (isspace) daquele objeto (palavra).
print('É um número?', palavra.isnumeric())
print('É alfabético?', palavra.isalpha())
print('É alfanumérico?', palavra.isalnum())
print('Está em maiúsculas?', palavra.isupper())
print('Está em minúsculas?', palavra.islower())
print('Está capitalizada?', palavra.istitle())

print('O tipo primitivo desse valor é', type(palavra), '. Só tem espaços?  {}.  É um número?  {}.  É alfabético?  {}.  É alfanumérico?  {}.  Está em maiúsculas?  {}.  Está em minúsculas?  {}.  Está capitalizada?  {}.'.format(palavra.isspace(), palavra.isnumeric(), palavra.isalpha(), palavra.isalnum(), palavra.isupper(), palavra.islower(), palavra.istitle()))
