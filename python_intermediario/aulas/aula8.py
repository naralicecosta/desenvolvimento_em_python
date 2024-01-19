'''Closure e funções que retornam outras funções'''

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar()


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['maria', 'joana', 'luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))
'''VER ALGO MAIS PRATICO QUE ISSO
'''