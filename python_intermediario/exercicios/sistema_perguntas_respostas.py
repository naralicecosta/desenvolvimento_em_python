#exericio - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Qual evento marcou o início da Segunda Guerra Mundial em 1939?',
        'Opções': ['Invasão da Polônia pela Alemanha', 'Bombardeio de Pearl Harbor', 'Assinatura do Tratado de Versalhes'],
        'Resposta': 'Invasão da Polônia pela Alemanha'
    },
    {
        'Pergunta': 'Quem foi o líder dos Estados Unidos durante a Guerra Civil Americana?',
        'Opções': ['George Washington', 'Abraham Lincoln', 'Thomas Jefferson'],
        'Resposta': 'Abraham Lincoln'
    },
    {
        'Pergunta': 'Qual foi a principal causa da Revolução Francesa?',
        'Opções': ['Escassez de pão', 'Má administração financeira da monarquia', 'Guerras Napoleônicas'],
        'Resposta': 'Má administração financeira da monarquia'
    }
    
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')