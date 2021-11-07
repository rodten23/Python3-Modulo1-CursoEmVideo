# Relativo até Aula 08
# Faça um programa que leia o comprimento do cateto oposto e
# do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot
catoposto = float(input('Por favor, digite a medida do cateto oposto: '))
catadjacente = float(input('Agora, digite a medida do cateto adjacente: '))
hipotenusa = sqrt(catoposto**2+catadjacente**2)
hipot2 = hypot (catoposto, catadjacente)
print('Com catetos {}cm e {}cm, sua hipotenusa terá a medida de {:.2f}cm.'.format(catoposto, catadjacente, hipotenusa))
print('Com catetos {}cm e {}cm, sua hipotenusa terá a medida de {:.2f}cm.'.format(catoposto, catadjacente, ((catoposto**2+catadjacente**2)**(1/2))))
print('Com catetos {}cm e {}cm, sua hipotenusa terá a medida de {:.2f}cm.'.format(catoposto, catadjacente, hipot2))
