#combinations, permutations e product - intertools
#combinação - ordem não importa - iterável _ tamanho do grupo
#permutação - ordem importa
#produto - ordem importa e repete valores únnicos

from itertools import combinations

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()
    
pessoas = [
    'João', 'Ana', 'Luiz', 'Leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino']
    ['algodao', 'poliester']
]
    
# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))