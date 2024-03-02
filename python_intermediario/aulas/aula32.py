# groupby - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'luiz', 'nota': 'A'},
    {'nome': 'ana', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'D'},
    {'nome': 'Geralda', 'nota': 'F'},
    {'nome': 'Susen', 'nota': 'A'},
    {'nome': 'Joana', 'nota': 'B'},
    {'nome': 'Nara', 'nota': 'A'},
]
#ordenando lista
def ordena(aluno):
    return aluno['nota']
alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
        
