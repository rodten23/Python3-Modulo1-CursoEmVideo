# Relativo até Aula 09
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Por favor, digite seu nome completo: ')).strip()
print('Aguarde, estamos reconhecendo seu nome.')
print('Seu nome, em letras maiúsculas fica assim: ' + nome.upper())
print('Agora, em minúsculas fica assim: ' + nome.lower())
print('Ao todo, seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
# Nessa solução, nome sozinho perde a última letra e número de letras conta uma a menos.
print('Seu primeiro nome é {} e tem {} letras.'.format(nome[:nome.find(' ')], len(nome[:nome.find(' ')])))
# Nessa segunda solução, nome sozinho perde a última letra e número de letras mostra -1.
print('Seu primeiro nome é {} e tem {} letras.'.format(nome[:nome.find(' ')], nome.find(' ')))
# Essa é a solução correta, pois seja com nomes simples ou nomes compostos, tanto o nome quanto a contagem
# aparecem corretos.
print('Seu primeiro nome é {} e tem {} letras.'.format(nome.split()[0], len(nome.split()[0])))
