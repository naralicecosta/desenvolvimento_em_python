'''
crie uma função que multiplica todos os argumentos não nomeados recebidos
retorne o total para uma variavel e mostre o valor da variavel

crie uma função fala se um  número é par ou impar.
retorne se o número é par ou ímpar.
'''

def multiplicar(**args):
    total = 1
    for numero in args: #multiplicar todos os argumentps
        total *= numero
    return total
multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)

def par_impar(numero):
    return numero %2 == 0

print(par_impar(2))
print(par_impar(3))