# usuário insere um número, ê a entrada como uma string com input()
# converte essa string em um número inteiro (int) usando int().
# O número inserido pelo usuário é armazenado na variável numero.
numero = int(input("digite um numero: "))
# inicia uma estrutura condicional (um "if") para verificar se o número é par. 
# O operador % é usado para calcular o resto da divisão do número por 2.
# Se o resto for igual a zero,isso significa que o número é divisível por 2 e, portanto, é par.
if numero % 2 == 0:
    # Se o número for par, esta linha será executada, e o programa imprimirá "O número é par.", 
    print("O número é par")
else: # Se o número não for par, esta parte do código será executada.
    print("O número é impar")