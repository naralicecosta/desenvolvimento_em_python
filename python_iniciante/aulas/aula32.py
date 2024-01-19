'''lista de listas e seus indices'''

salas = [
    ['MARIA', 'HELENA',],
    ['ELAINE',],
    ['LUIZ', 'JOAO']
]
print(salas[1][0])

print(salas[0][1])
print(salas[2][2])

#ou

for sala in salas:
    for item in sala:
        print(item)