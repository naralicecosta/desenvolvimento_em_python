frase = 'o python é uma linguagem de programação' \
        'multiparadigma' \
        'o python foi criado por Guido van Rossum'
        
i = 0
qts_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
        letra_atual = frase [i]
        
        if letra_atual == ' ':
                i += 1
                continue
        
        
        qts_apareceu_mais_vezes_atual = frase.count(letra_atual)
        
        if qts_apareceu_mais_vezes < qts_apareceu_mais_vezes_atual:
                qts_apareceu_mais_vezes = qts_apareceu_mais_vezes_atual
                letra_apareceu_mais_vezes = letra_atual
                
        i += 1  #iteração
print('A letra que apareceu mais vezes foi'
f' "{ letra_apareceu_mais_vezes }" que apareceu'
f' { qts_apareceu_mais_vezes } x'
)