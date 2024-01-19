'''
Introdução ao desempacotamento + tuplas (tuplas)
'''
'''nomes = ['Maria', 'Helena', 'Luiz']
nome1,nome2,nome3 = nomes
#nome1,nome2,nome3  = ['Maria', 'Helena', 'Luiz']
print(nome2)'''

nomes = ['Maria', 'Helena', 'Luiz']
nomes[1] = 'outro'
_, _, nome, *resto = nomes
print(nome)
print(nomes)

'''Tipo tupla - uma lista imutável

como criar'''
#nomes = '(Maria', 'Helena', 'Luiz')
#nomes = tuple(nomes)
nomes = 'Maria', 'Helena', 'Luiz'
#nomes = list(nomes)
print(nomes[-1])
