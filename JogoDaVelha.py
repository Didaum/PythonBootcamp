jogador1 = input('Digite o nome do Jogador 1: ')
jogador2 = input('Digite o nome do Jogador 2: ')

# Exemplo das posições
print('\n')
print('POSIÇÔES')
print('7 | 8 | 9')
print('4 | 5 | 6')
print('1 | 2 | 3')

# Matriz de posições
posicao_lista1 = [0] * 3
posicao_lista2 = [0] * 3
posicao_lista3 = [0] * 3
posicao_total = [posicao_lista1, posicao_lista2, posicao_lista3]

# Matriz de simbolos
simbolo_lista1 = [' '] * 3
simbolo_lista2 = [' '] * 3
simbolo_lista3 = [' '] * 3
simbolo_total = [simbolo_lista1, simbolo_lista2, simbolo_lista3]


# Gera o tabuleiro com a jogada
def board():
    for linha in range(0, 3):
        for coluna in range(0, 3):
            if posicao_total[linha][coluna] == 1:
                simbolo_total[linha][coluna] = 'X'
            elif posicao_total[linha][coluna] == -1:
                simbolo_total[linha][coluna] = 'O'
    print('{} | {} | {}'.format(simbolo_total[2][0], simbolo_total[2][1], simbolo_total[2][2]))
    print('{} | {} | {}'.format(simbolo_total[1][0], simbolo_total[1][1], simbolo_total[1][2]))
    print('{} | {} | {}'.format(simbolo_total[0][0], simbolo_total[0][1], simbolo_total[0][2]))


jogador = 1


# Percorre a matriz e soma as coluna, linhas ou diagonais
def vitoria():
    # Identifica se algum jogador completou alguma linha
    somal1 = 0
    somal2 = 0
    somal3 = 0
    for linha1 in posicao_lista1:
        somal1 += linha1
        if somal1 == 3:
            print('{} é o Vencedor'.format(jogador1))
        elif somal1 == -3:
            print('{} é o Vencedor'.format(jogador2))
    for linha2 in posicao_lista2:
        somal2 += linha2
        if somal2 == 3:
            print('{} é o Vencedor'.format(jogador1))
        elif somal2 == -3:
            print('{} é o Vencedor'.format(jogador2))
    for linha3 in posicao_lista3:
        somal3 += linha3
        if somal3 == 3:
            print('{} é o Vencedor'.format(jogador1))
        elif somal3 == -3:
            print('{} é o Vencedor'.format(jogador2))
    # Identifica se algum jogador completou alguma coluna
    somac1 = 0
    somac2 = 0
    somac3 = 0
    for coluna1 in range(0, 3):
        col1 = 0
        somac1 += posicao_total[coluna1][col1]
        if somac1 == 3:
            print('{} é o Vencedor'.format(jogador1))
        elif somac1 == -3:
            print('{} é o Vencedor'.format(jogador2))
    for coluna2 in range(0, 3):
        col2 = 1
        somac2 += posicao_total[coluna2][col2]
        if somac2 == 3:
            print('{} é o Vencedor'.format(jogador1))
        elif somac2 == -3:
            print('{} é o Vencedor'.format(jogador2))
    for coluna3 in range(0, 3):
        col3 = 2
        somac3 += posicao_total[coluna3][col3]
        if somac3 == 3:
            print('{} é o Vencedor'.format(jogador1))
        elif somac3 == -3:
            print('{} é o Vencedor'.format(jogador2))
    # Identifica se algum jogador completou alguma diagonal
    somad1 = posicao_total[0][0] + posicao_total[1][1] + posicao_total[2][2]
    somad2 = posicao_total[2][0] + posicao_total[1][1] + posicao_total[0][2]
    if somad1 == 3 or somad2 == 3:
        print('{} é o Vencedor'.format(jogador1))
    elif somad1 == -3 or somad2 == -3:
        print('{} é o Vencedor'.format(jogador2))


while jogador == 1:
    posicao = int(input(f'\nDigite uma posição {jogador1}: '))
    if posicao == 1:
        posicao_total[0][0] = 1
    elif posicao == 2:
        posicao_total[0][1] = 1
    elif posicao == 3:
        posicao_total[0][2] = 1
    elif posicao == 4:
        posicao_total[1][0] = 1
    elif posicao == 5:
        posicao_total[1][1] = 1
    elif posicao == 6:
        posicao_total[1][2] = 1
    elif posicao == 7:
        posicao_total[2][0] = 1
    elif posicao == 8:
        posicao_total[2][1] = 1
    elif posicao == 9:
        posicao_total[2][2] = 1
    board()
    jogador = -1
    vitoria()
    while jogador == -1:
        posicao = int(input(f'\nDigite uma posição {jogador2}: '))
        if posicao == 1:
            posicao_total[0][0] = -1
        elif posicao == 2:
            posicao_total[0][1] = -1
        elif posicao == 3:
            posicao_total[0][2] = -1
        elif posicao == 4:
            posicao_total[1][0] = -1
        elif posicao == 5:
            posicao_total[1][1] = -1
        elif posicao == 6:
            posicao_total[1][2] = -1
        elif posicao == 7:
            posicao_total[2][0] = -1
        elif posicao == 8:
            posicao_total[2][1] = -1
        elif posicao == 9:
            posicao_total[2][2] = -1
        board()
        jogador = 1
        vitoria()
