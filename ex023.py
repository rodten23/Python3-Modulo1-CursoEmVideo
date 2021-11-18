# Relativo até Aula 09
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = input('Por favor, digite um número: ').strip()
u = int(num) % 10
d = int(num) // 10 % 10
c = int(num) // 100 % 10
m = int(num) // 1000 % 10
print('O número digitado foi: {}'.format(num))
print('Ele é composto de\n{} unidade(s)\n{} dezena(s)\n{} centena(s)\n{} milhar(es)'.format(u, d, c, m))
#print('Ele é composto de\n{} unidade(s)\n{} dezena(s)\n{} centena(s)\n{} milhar(es)'.format(num[-1], num[-2], num[-3:1], num[-4:0]))