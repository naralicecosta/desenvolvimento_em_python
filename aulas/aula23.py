'''
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento

métodos úteis: append, insert, pop, del, clear, extend, + 
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''
string = 'ABCDE'
lista = [123, True, 'Nara', 1.2, []]
print(lista)
print(lista[2])
print(lista[2].upper(), type(lista[2])) #mostra o item na posição 2 e transforma em letras maiusculas

#print(bool([])) # falsy
#print(lista)

lista = [10, 20, 30, 40, 50, 60, 70, 80,]
lista[2] = 300
del lista[2]
print(lista)
print(lista[2]) #mostra qua item da posiçaõ 2