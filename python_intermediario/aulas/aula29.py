#exercicio -  unir listas

# def ziper(lista1, lista2):
#     intervalo_maximo = min(len(lista1), len(lista2))
#     return [(lista1, lista2) for i in range (intervalo_maximo)]
    
    
# l1 = ['salvador', 'natal', 'ceara']
# l2 = ['BA', 'RN', 'CE', 'MG']

# print(ziper(l1,l2))
    
from intertools import zip_longest

l1 = ['salvador', 'natal', 'ceara']
l2 = ['BA', 'RN', 'CE', 'MG']
print(list(zip(l1,l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))

