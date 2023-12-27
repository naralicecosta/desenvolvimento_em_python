'''calculadora com while'''

while True:

    numero_1 = input("digite um número: ")
    numero_2 = input("digite outro número: ")
    operador = input('digite um operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
       
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print("um ou ambos números digitados são inválidos")
        continue
    
    operador_permitido = '+ - / *'
    
    if operador_permitido not in operador_permitido:
        print("o operador digitado é inválido")
        continue
    
    if len(operador) > 1:
        print("digite apenas um operador")
        continue
    
    print("realizando sua conta, confira o resultado abaixo")
    if operador == "+":
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
        
    elif operador == "-":
        print(f'{num_1_float} - {num_2_float} =',num_1_float - num_2_float)
        
    elif operador == "*":
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
        
    elif operador == "/":
        print(f'{num_1_float} / {num_2_float} =',num_1_float / num_2_float)
        
    else:
        print("nunca deveria chegar aqui")

    sair = input("quer sair? [s]im: ").lower().startswith('s')
        
    if sair is True:
        break