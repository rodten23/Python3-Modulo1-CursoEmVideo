# Desafios da aula
salario = float(input('Favor, qual seu salário? '))
aumento = 15
print('Seu salário, com aumento de 15%, ficará em R$ {:.2f}.'.format(salario+(salario*(aumento/100))))

print('---------')
preco = float(input('Qual o preço do produto?  '))
desconto = 5
print('Com o desconto de 5%, pelo produto que tinha o preço de {:.2f}, você pagará agora {:.2f}.'.format(preco, preco*((100-desconto)/100)))

print('---------')
largura = int(input('Qual a largura da sua parede? '))
altura = int(input('E qual a altura dela?  '))
trende = 2
print('Sua parede tem {} m² e, sendo assim, para pintá-la precisará de {} litros de tinta.'.format(largura*altura, (largura*altura)/trende))
print('---------')
seud = float(input('Quanto dinheiro você tem na carteira?  '))
dolar = 5.45
print('Com a cotação do dólar em 5,45, hoje seu dinheiro vale {:.2f} dólares.'.format(seud/dolar))

print('---------')
numero = int(input('Quer a tabuada de qual número?  '))
print('A tabuada de {} é {}, {}, {}, {}, {}, {}, {}, {}, {} e {}.'.format(numero, numero*1, numero*2, numero*3, numero*4, numero*5, numero*6, numero*7, numero*8, numero*9, numero*10))

print('---------')
alvo = int(input('Favor, digite um número:  '))
print('Então, você digitou {} e, sendo assim, o antecessor é {} e o sucessor é {}.'.format(alvo, alvo-1, alvo+1))
print('Além disso, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {}.'.format(alvo*2, alvo*3, alvo**(1/2)))

print('---------')
nota1 = int(input('Sua primeira nota foi: '))
nota2 = int(input('Sua segunda nota foi: '))
print('Com suas notas a média foi de {}.'.format((nota1+nota2)/2))
print('---------')
medida = int(input('Qual a medida em metros?  '))
print('A medida em metros é {}, que é igual a {} cm e igual a {} mm.'.format(medida, medida*100, medida*1000))

# Aula - Operadores aritméticos básicos
# Ordem de precedência:
# 1º  ( ) - diferente da Matemática, em Python [ ] e { } funcionam pra outras coisas,
# 2º  **
# 3º  *  ,  /  ,  //  ,  %  ,  por ordem em que aparecem da esquerda para direita
# 4º  +  e  -  binárias

n1 = 9
n2 = 2
print(n1 + n2) # soma
print(n1 - n2) # subtração
print(n1 * n2) # multiplicação
print(n1 / n2) # divisão, retornando valor decimal (float).
print(n1 // n2) # divisão inteira, desprezando parte decimal, não arredondando.
print(n1 % n2) # resto da divisão (também chamado de módulo), retornando valor inteiro.
print(n1 ** n2) # potenciação, que também pode ser com a função pow(x,y)
print(81**(1/2)) # uma das formas para raiz quadrada, que é o número elevado a meio.
print(81**(1/3)) # uma das formas para raiz cúbica, que é o número elevado a um terço.

print('---------')
print(6+3*2) # primeiro multiplicação
print(3*5+4**2) # primeiro a exponenciação
print(3*(5+4)**2) # primeiro os ( )
print('---------')

print('Oi'+'Olá')  # aqui temos concatenação (junção) de strings
print('Oi'*9)  # aqui temos multiplicação da string
print('---------')

n3 = int(input('Digite um novo número: '))
n4 = int(input('Agora, outro número: '))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
e = n3 ** n4
print('A soma é {}, o produto é {} e a divisão é {}.'.format(s, m, d))
print('A soma é {:.10f}, o produto é {:.2f} e a divisão é {:.3f}.'.format(s, m, d)) # Aqui a diferença é que informamos na máscara para
#obrigatoriamente gerar tantas casas decimais nos resultados.
print('Divisão inteira é {} e potência é {}.'.format(di, e))

print('A soma é {:.10f}, \n o produto é {:.2f} e \n a divisão é {:.3f}.'.format(s, m, d), end=' >*>') # Já aqui, o \n quebra em linhas e o end='' junta prints.
print('Divisão inteira é {} e potência é {}.'.format(di, e))


print('---------')
nome = input('Qual seu nome?  ')
print('Prazer em te conhecer, {}!'.format(nome)) # o que já fizemos até aqui, substituição simples em cima da "máscara" {}
print('Prazer em te conhecer, {:20}!'.format(nome)) # agora á substuição ocorre numa área de 20 espaços
print('Prazer em te conhecer, {:>20}!'.format(nome)) # agora á substuição ocorre numa área de 20 espaços e alinhada à direita
print('Prazer em te conhecer, {:<20}!'.format(nome)) # agora á substuição ocorre numa área de 20 espaços e alinhada à esquerda (que já é o padrão)
print('Prazer em te conhecer, {:^20}!'.format(nome)) # agora á substuição ocorre numa área de 20 espaços e alinhada ao centro
print('Prazer em te conhecer, {:=^20}!'.format(nome)) # agora á substuição ocorre numa área de 20 espaços, alinhada ao centro e completada
# com símbolo nas áreas vazias (mas espaços não são exatamente "área vazia")
