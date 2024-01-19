#usuário digitar um número que sera convertido para float e armazenado em numX
num1 = float(input("Digite um número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

#media que vai fazer o calculo dos numeros armazenados
media = (num1 + num2 + num3) /3
#mprime a média calculada na tela
# usando uma f-string para incorporar o valor da variável media na mensagem de saída. 
print(f"a media é:{media}")