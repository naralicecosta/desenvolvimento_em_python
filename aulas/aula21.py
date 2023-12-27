'''
For + Range

range -> range(start, stop, step)
'''

'''numeros = range(5,10,2)

for numero in numeros: #para cada percorrida em números ele adiciona em numero]
    print(numero)
    '''
##################################################################
'''
iterável -> str, range, stc
iterador -> quem sabe entrgar um valor po vez
next -> me entregue o proximo valor
iter -> me entregue seu iterador
'''
texto = 'nara'
iterador = iter(texto)

while True:
    try:
        letra = next(iterador)
        print(letra)
        
    except StopIteration:
        break

