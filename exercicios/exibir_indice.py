'''
exiba os indices da lista

Maria
Helena
Luiz
'''
lista = ['Maria', 'Helena', 'Luiz']
lista.append('nara')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))