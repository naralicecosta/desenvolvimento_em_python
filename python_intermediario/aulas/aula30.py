# lista_a = [1,2,3,4,5,6,7,8,9,10]
# lista_b = [1,2,3,4,5,6,7,8]

# lista_soma = []
# for i in range(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)


#################################

# lista_a = [1,2,3,4,5,6,7,8,9,10]
# lista_b = [1,2,3,4,5,6,7,8]

# lista_soma = []
# for i, _ in enumerate(len(lista_b)):
#     lista_soma.append(lista_a[i] + lista_b[i])
# print(lista_soma)

lista_a = [1,2,3,4,5,6,7,8,9,10]
lista_b = [1,2,3,4,5,6,7,8]

lista_soma = [ x + y for x, y in zip(lista_a, lista_b)]
print(list(zip(lista_a, lista_b)))



'''
from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]
'''