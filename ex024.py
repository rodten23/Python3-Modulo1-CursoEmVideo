# Relativo até Aula 09
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Favor, diga-nos sua cidade: ')).strip()

# Solução correta conforme meus testes.
if cidade.lower().find('sant') == 0:
    print('Você mora numa cidade com "Santo".')
elif cidade.lower().find('são') == 0:
    print('Você mora numa cidade com "São".')
elif cidade.lower().find('sao') == 0:
    print('Você mora numa cidade com "São".')
else:
    print('Você não mora numa cidade com "Santo" ou "São".')

# Solução boa, mas que pode apresentar problema com algumas cidades.
if 'sant' in cidade.lower():
    print('Você mora numa cidade com "Santo".')
elif 'são' in cidade.lower():
    print('Você mora numa cidade com "São".')
elif 'sao' in cidade.lower():
    print('Você mora numa cidade com "São".')
else:
    print('Você não mora numa cidade com "Santo" ou "São".')

# Solução simples do Guanabara.
print(cidade[:4].lower() == 'sant')


