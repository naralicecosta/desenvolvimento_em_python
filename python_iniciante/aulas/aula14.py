nome = input ("digite seu nome: ")
idade = input("digite sua idade: ")

if nome and idade:
    print(f'seu nome é {nome} e sua idade é {idade}')
    print(f'seu nome invertido é {nome[::-1]}')
     
    if ' ' in nome:
        print('seu nome contem espaço')
    else:
        print("seu nome não contem espaço")     
        
    print(f'seu nome tem {len(nome)}letras')
    print(f'a primeira letra do seu nome é {nome[0]}')
    print(f'a ultima letra do seu nome é {nome[-1]}')
