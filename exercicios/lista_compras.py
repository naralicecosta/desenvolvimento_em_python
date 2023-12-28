'''
faça uma lista de compras que permita o usuário
inserir, apagar e listar valores da lista
'''

import os

lista = []
while True:
    print('selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
        
    elif opcao == 'a':
        indice_str = input(
            'Escolha o indice para apagar'
        )
        
        try:
            indice = int(indice_str)
            del lista[indice]
        except :
            print('Não foi possivel apagar esse indice')
    
    elif opcao == 'l':
        os.system('clear')
        
        if len(lista) == 0:
            print('A lista está vazia')
            
        for i, valor in enumerate(lista):
            print(i, valor)
        