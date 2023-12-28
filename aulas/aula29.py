'''enumerate - enumera iteráveis (índices)'''
lista = ['maria', 'helena', 'luiz']
lista.append('joao')

#maneira mais facil
for indice, nome in enumerate(lista):
    print(f'{indice} - {nome}')

for tupla_enumerada in enumerate(lista):
    print('for da tupla')
    for valor in tupla_enumerada:
        print(f'\t{valor}')