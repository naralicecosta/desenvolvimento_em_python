'''Higher Order Function
- Funções de primeira classe'''

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(texto)

v = executa(saudacao, 'Bom dia')
printss(v)
    