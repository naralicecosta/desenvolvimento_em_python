 #solicita ao usuário  que insira o primeiro número lê a entrada como uma string com input(),
 #e então converte essa string em um número de ponto flutuante (float) usando float().
 # O resultado é armazenado na variável num1.
num1 = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))

# os valores de num1 e num2 são somados e o resultado é armazenado na variável soma.
soma = num1+ num2
# o programa imprime a soma dos números na tela,
# utilizando uma f-string para incorporar o valor da variável soma na mensagem exibida.
print(f"a soma é:{soma}")