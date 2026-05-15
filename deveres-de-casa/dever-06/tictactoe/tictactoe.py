"""
Tic Tac Toe Logic - Refactored Version
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Inicia o tabuleiro 3x3 vazio.
    """
    return [[EMPTY for _ in range(3)] for _ in range(3)]


def player(board):
    """
    Determina de quem é a vez.
    """
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)

    return O if count_x > count_o else X


def actions(board):
    """
    Retorna uma lista de tuplas (r, c) com os movimentos disponíveis.
    """
    moves = set()
    for r in range(3):
        for c in range(3):
            if board[r][c] == EMPTY:
                moves.add((r, c))
    return moves


def result(board, action):
    """
    Gera um novo estado do tabuleiro após a jogada.
    """
    r, c = action
    if board[r][c] is not EMPTY:
        raise ValueError("Movimento inválido: posição já ocupada.")

    new_state = deepcopy(board)
    new_state[r][c] = player(board)
    return new_state


def winner(board):
    """
    Verifica se há um vencedor e o retorna.
    """
    # Verificação de Linhas e Colunas simultaneamente
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Diagonais
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    jogoa acabou?
    """
    if winner(board) is not None:
        return True

    return all(cell is not EMPTY for row in board for cell in row)


def utility(board):
    """
    X ganha (1), O ganha (-1), empate (0).
    """
    res = winner(board)
    if res == X:
        return 1
    elif res == O:
        return -1
    return 0


def minimax(board):
    """
    usando o algoritmo minimax.
    """
    if terminal(board):
        return None

    current_turn = player(board)

    if current_turn == X:
        _, best_move = _max_score(board)
    else:
        _, best_move = _min_score(board)

    return best_move


def _max_score(board):
    if terminal(board):
        return utility(board), None

    v = -math.inf
    move = None
    for action in actions(board):
        score, _ = _min_score(result(board, action))
        if score > v:
            v = score
            move = action
            if v == 1:
                break
    return v, move


def _min_score(board):
    if terminal(board):
        return utility(board), None

    v = math.inf
    move = None
    for action in actions(board):
        score, _ = _max_score(result(board, action))
        if score < v:
            v = score
            move = action
            if v == -1:
                break
    return v, move
