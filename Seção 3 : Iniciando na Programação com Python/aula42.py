frase = 'O python é uma linguagem ' \
        'Multiparadigma.' \
        'Python foi criado por Guido Van Rossum.'

i = 0
qtd_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
        letra_atual = frase[i]
        qtd_vezes_atual = frase.count(letra_atual)

        if letra_atual == ' ':
                i += 1
                continue

        if qtd_mais_vezes <qtd_vezes_atual:
                qtd_mais_vezes = qtd_vezes_atual
                letra_apareceu_mais_vezes = letra_atual
        i += 1

print('A Letra que apareceu mais vezes foi'
      f' "{letra_apareceu_mais_vezes}" que apareceu '
      f'{qtd_mais_vezes}x')