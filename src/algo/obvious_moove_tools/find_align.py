def horizontal_search(board, i, j, search_len, player):
    moves = []
    if j + search_len - 1 < 20 and all(board[i][j + k] == player for k in range(search_len)):
        if j + search_len < 20 and board[i][j + search_len] == 0:
            moves.append((i, j + search_len))
        if j - 1 >= 0 and board[i][j - 1] == 0:
            moves.append((i, j - 1))
    return moves

def vertical_search(board, i, j, search_len, player):
    moves = []
    if i + search_len - 1 < 20 and all(board[i + k][j] == player for k in range(search_len)):
        if i + search_len < 20 and board[i + search_len][j] == 0:
            moves.append((i + search_len, j))
        if i - 1 >= 0 and board[i - 1][j] == 0:
            moves.append((i - 1, j))
    return moves

def fall_diag_search(board, i, j, search_len, player):
    moves = []
    if i + search_len - 1 < 20 and j + search_len - 1 < 20 and all(board[i + k][j + k] == player for k in range(search_len)):
        if i + search_len < 20 and j + search_len < 20 and board[i + search_len][j + search_len] == 0:
            moves.append((i + search_len, j + search_len))
        if i - 1 >= 0 and j - 1 >= 0 and board[i - 1][j - 1] == 0:
            moves.append((i - 1, j - 1))
    return moves

def up_diag_search(board, i, j, search_len, player):
    moves = []
    if i + search_len - 1 < 20 and j - (search_len - 1) >= 0 and all(board[i + k][j - k] == player for k in range(search_len)):
        if i + search_len < 20 and j - search_len >= 0 and board[i + search_len][j - search_len] == 0:
            moves.append((i + search_len, j - search_len))
        if i - 1 >= 0 and j + 1 < 20 and board[i - 1][j + 1] == 0:
            moves.append((i - 1, j + 1))
    return moves

def find_align(board, search_len, player):
    """
    Cherche des alignements pour le joueur donné.
    Retourne les coordonnées de la case vide à compléter.
    """
    possible_moves = set()
    for i in range(20):
        for j in range(20):
            if board[i][j] == player:
                possible_moves.update(
                    horizontal_search(board, i, j, search_len, player) +
                    vertical_search(board, i, j, search_len, player) +
                    fall_diag_search(board, i, j, search_len, player) +
                    up_diag_search(board, i, j, search_len, player)
                )
    return list(possible_moves) if possible_moves else None
