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


# Percorre a matriz e soma as coluna, linhas ou diagonais
def vitoria():
    soma1 = 0
    soma2 = 0
    for linha in range(0, 3):
        for coluna in range(0, 3):
            soma1 = soma1 + posicao_total[linha][coluna]
            soma2 = soma2 + posicao_total[coluna][linha]
    if soma1 == 3 or soma2 == 3:
        print('{} é o Vencedor'.format(jogador1))
    elif soma1 == -3 or soma2 - 3:
        print('{} é o Vencedor'.format(jogador2))

    diagonal1 = posicao_total[0][0] + posicao_total[1][1] + posicao_total[2][2]
    diagonal2 = posicao_total[0][2] + posicao_total[1][1] + posicao_total[2][0]
    if diagonal1 == 3 or diagonal2 == 3:
        print('{} é o Vencedor'.format(jogador1))
    elif diagonal1 == -3 or diagonal2 == -3:
        print('{} é o Vencedor'.format(jogador2))


jogador = 1

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
    vitoria()
    jogador = -1
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
        vitoria()
        jogador = 1
