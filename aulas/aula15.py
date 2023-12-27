'''
introdução ao try/except
try -> tenta executar o código

except -> ocorreu algum erro ao tentar execurar
'''
numero_str = input("vou dobrar o numero que voce digitar")

try:
    print("STR:", numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2}')
except:
    print('isso não é um número')
