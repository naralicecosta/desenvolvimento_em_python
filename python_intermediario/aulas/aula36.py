import json
#salvando dados python em JSON com modulo json
pessoa = {
    'nome': 'Naralice',
    'sobrenome': 'Cavalcante',
    'enderecos': [
        {'rua': 'R1', 'numero': 33},
        {'rua': 'R2', 'numero': 32},
    ],
    'altura': 1.67,
    'numeros_preferidos': (2, 4, 5,6, 7),
    'dev': True,
    'nada': None,
}

with open('aula36.json', 'r', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2 )