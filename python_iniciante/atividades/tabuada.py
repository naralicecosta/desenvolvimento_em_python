#nome do usuário
numero = int(input("Digite um número para ver a tabuada: "))
# Este é um loop for que itera de 1 a 10 . 
# Isso significa que i assumirá valores de 1 a 10 em cada iteração do loop.
for i in range(1,11):
    #: Dentro do loop, esta linha calcula o produto entre numero e i e armazena
    # o resultado na variável resultado. Isso corresponde a calcular a tabuada do
    # número inserido pelo usuário para cada valor de i no intervalo de 1 a 10.
    resultado = numero * i
    print (f"{numero} x {i} = {resultado}")