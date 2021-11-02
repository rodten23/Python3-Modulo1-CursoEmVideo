# Relativo até Aula 07
# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Qual a largura da sua parede? '))
altura = float(input('E qual a altura dela?  '))
trende = 2
print('Como sua parede tem {}m de largura e {}m de altura, sua área é de {:.2f}m².\nSendo assim, para pintá-la você precisará de {:.2f} litros de tinta.'.format(largura, altura, largura*altura, (largura*altura)/trende))
