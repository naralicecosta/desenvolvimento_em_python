'''
Listas em python
tipo list - mutável
suporta vários valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento

métodos úteis: append, insert, pop, del, clear, extend, + 
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

'''
append -> adiciona um item ao final
insert -> adiciona um item no indice escolhido
pop -> remove do final ou doi indice escolhido
del -> apaga um indice
clear -> limpa a lista
extend -> estende a lista

'''
#metodo append e pop
lista = [10, 20, 30, 40, 50, 60, 70, 80,]
#adicionar mais coisas ao final da lista com o método append
lista.append('nara') #adiciona a ultima posição
#nome = lista.pop() #remove o nome nara
lista.append(1233)
del lista [-1]
#lista.pop() #removeu o ultimo item da lista
#lista.clear()
lista.insert(0, 'oie') #o primeiro numero é a posição e o segundo item é o que vai ficar no lugar da posição escolhida
print(lista)
