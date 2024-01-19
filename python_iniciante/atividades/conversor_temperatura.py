# solicita ao usuário que insira uma temperatura 
celcius = float(input("Digite a temperatura em celcius: "))
#a temperatura em graus Celsius é convertida em graus Fahrenheit usando a fórmula de conversão comum. 
fahrenheit = (celcius * 9/5) + 32
#imprime a temperatura em graus Fahrenheit na tela
print(f"A temperatura em Fahrenheit é: {fahrenheit}")