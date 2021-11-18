frase = 'Curso em Vídeo Python'  # String, cadeia de caracteres ou também cadeia de texto. Esse exemplo tem 21 "mini áreas
#de memória", ou seja, 21 caracteres (inclui todos os espaços), contados a partir do índice 0 ao 20.

# [ ] em Python é o identificador de lista.

# Python é case-sensitive.

print(frase)
print(frase[9])
print(frase[9:13]) # No Python, ele vai do primeiro índice informado até um índice antes do último informado, ou seja, o índice final informado
#não é considerado. Essa seleção da lista é chamada de range.

print(frase[9:21]) # Pode colocar o índice final maior do que realmente existe e o Python vai acabar a seleção certinho. Porém não é adequado
#fazer dessa forma.

print(frase[9:21:2]) # Com esse terceiro item, o fatiamento será de 2 em 2 posições.
print(frase[::3]) # Como não dei o início, nem o final, será a string inteira, mas pulando de 3 em 3.

print(frase[:5]) # Vai do zero até o índice 4.

print(frase[15:]) # Vai do índice informado até o final da string.

print(frase[9::3])

print(len(frase)) # Len de length (comprimento em Inglês), função que retorna tamanho da string.

print(frase.count('o')) # O método .count, conta quantas vezes temos a string informada dentro da string principal.

print(frase.count('o', 0, 13)) # Agora, a contagem será feita apenas dentro do range informado.
frase2 = 'A casa do sabido é um salão.'
print(frase2.find('sa')) # O método .find (encontrar) encontra a string informada, retornando o índice onde ele começa.

print(frase.find('Android')) # Se o Python retornar -1, significa que valor informado está fora da string, pois essa sempre começa em zero e,
#portanto, esse valo não existe.

print('Curso' in frase) # Operador in significa em, então "existe Curso dentro da string frase?". Resultado é boleano.

frase.upper() # Transforma toda string em maiúsculas.
frase.lower() # Transforma toda string em minúsculas.
frase.capitalize() # Deixa a primeira da string toda em maiúscula e o restante em minúsculas.
frase.title() # Deixa a primeira letra de cada palavra em maiúsculas e o restante em minúsculas.
frase.strip() # Remove espaços inúteis no início e no final da string
frase.rstrip() # Remove os espaços inúteis no final da string, lado right.
frase.lstrip() # Remove os espaços inúteis no começo da string, lado left.

frase.upper().count('O') # Posso combinar métodos.

frase.replace('Python', 'Android') # Uma string é imutável, então não conseguimos alterá-la de fato,
# mas sim gerar uma nova instância que não guarda sua nova condição.
frase = frase.replace('Python', 'Android') # Agora vai manter a nova formatação, pois foi atribuida a uma variável.
print(frase)

frase.split() # Divide (split) a string por palavras (cada uma com seu índice), quebrando em seus espaços (por padrão, mas pode ser alterado)
# e gerando uma lista de strings (então, cada palavra será um índice da lista criada).
frase3 = frase.split()
print(frase3)

'-'.join(frase3) # Juntar (join) a lista de string, usando o - como separador (por exemplo).
print('-'.join(frase3)) # Juntou nessa instância do print, mas não salvou, então isso não existe em mais nenhum lugar.

print('''aocoanaonva
voaonvoanvnaonoav
aonoavnoanvonavoanonvaonvaoa
anoavnoanvaonvaonaonaovnoa''') # Com 3 aspas, posso trabalhar com blocos de strings.

