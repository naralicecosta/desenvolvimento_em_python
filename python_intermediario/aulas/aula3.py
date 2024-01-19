'''
valores padrao para parametros
ao definir uma função, os parametros podem
ter valores padrao. Caso o valor nao seja enviado para o parametro, o valor padrao sera usado
'''
def soma(x, y,z=None):
    if z is not None:
        print(f'{x=} {z=}', x + y+z)
    else:
        print(f'{x=} {y=}', x + z)
        
soma (1,2)
soma(4,4)