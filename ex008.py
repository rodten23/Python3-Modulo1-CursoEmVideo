# Relativo até Aula 07
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

medida = float(input('Qual a medida em metros?  '))
print('A medida em metros é {}, que é igual a {:.0f} cm e igual a {:.0f} mm.'.format(medida, medida*100, medida*1000))

print('Sua medida equivale a:\n{:.3f}km\n{:.2f}hm\n{:.1f}dam\n{}dm\n{:.0f}cm\n{:.0f}mm'.format(medida/1000, medida/100, medida/10, medida*10, medida*100, medida*1000))