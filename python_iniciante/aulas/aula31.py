'''
split e join com list e str
split - divide uma string
join- une uma string
'''

frase = 'olha so         que, coisa       interessante'
lista_frases_cruas = frase.split(', ')

lista_frases = []

for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases[i].strip())
    #print(lista_frases[i].strip()) #strip corta os espaços do começo e do fim, lstrip - esquerda, rstrip - direita
frases_unidas = ', ' .join(lista_frases)
print(lista_frases)