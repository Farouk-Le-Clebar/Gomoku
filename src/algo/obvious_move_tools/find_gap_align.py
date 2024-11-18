import protocol

def is_within_bounds(*indices):
    return all(0 <= idx < protocol.cols if i % 2 else 0 <= idx < protocol.rows for i, idx in enumerate(indices))


def horizontal_gap_completion(board, i, j, search_len, player):
    moves = []
    if search_len == 4:
        # 2 - gap - 2
        if is_within_bounds(j - 2, j - 1, j + 1, j + 2) and \
           board[i][j - 2] == player and board[i][j - 1] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j] == 0:
            moves.append((i, j))
        # 3 - gap - 1
        if is_within_bounds(j - 3, j - 2, j - 1, j + 1) and \
           board[i][j - 3:j] == [player, player, player] and board[i][j + 1] == player and board[i][j] == 0:
            moves.append((i, j))
        # 1 - gap - 3
        if is_within_bounds(j - 1, j + 1, j + 2, j + 3) and \
           board[i][j - 1] == player and board[i][j + 1:j + 4] == [player, player, player] and board[i][j] == 0:
            moves.append((i, j))
    elif search_len == 3:
        # 1 - gap - 2
        if is_within_bounds(j - 1, j + 1, j + 2) and \
           board[i][j - 1] == player and board[i][j + 1:j + 3] == [player, player] and board[i][j] == 0:
            moves.append((i, j))
        # 2 - gap - 1
        if is_within_bounds(j - 2, j - 1, j + 1) and \
           board[i][j - 2:j] == [player, player] and board[i][j + 1] == player and board[i][j] == 0:
            moves.append((i, j))
    return moves


def vertical_gap_completion(board, i, j, search_len, player):
    moves = []
    if search_len == 4:
        # 2 - gap - 2
        if is_within_bounds(i - 2, i - 1, i + 1, i + 2) and \
           board[i - 2][j] == player and board[i - 1][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i][j] == 0:
            moves.append((i, j))
        # 3 - gap - 1
        if is_within_bounds(i - 3, i - 2, i - 1, i + 1) and \
           [board[i - 3 + k][j] for k in range(3)] == [player, player, player] and board[i + 1][j] == player and board[i][j] == 0:
            moves.append((i, j))
        # 1 - gap - 3
        if is_within_bounds(i - 1, i + 1, i + 2, i + 3) and \
           board[i - 1][j] == player and [board[i + 1 + k][j] for k in range(3)] == [player, player, player] and board[i][j] == 0:
            moves.append((i, j))
    elif search_len == 3:
        # 1 - gap - 2
        if is_within_bounds(i - 1, i + 1, i + 2) and \
           board[i - 1][j] == player and [board[i + 1 + k][j] for k in range(2)] == [player, player] and board[i][j] == 0:
            moves.append((i, j))
        # 2 - gap - 1
        if is_within_bounds(i - 2, i - 1, i + 1) and \
           [board[i - 2 + k][j] for k in range(2)] == [player, player] and board[i + 1][j] == player and board[i][j] == 0:
            moves.append((i, j))
    return moves


def fall_diag_gap_completion(board, i, j, search_len, player):
    moves = []
    if search_len == 4:
        # 2 - gap - 2
        if is_within_bounds(i - 2, i + 2, j - 2, j + 2) and \
           board[i - 2][j - 2] == player and board[i - 1][j - 1] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i][j] == 0:
            moves.append((i, j))
        # 3 - gap - 1
        if is_within_bounds(i - 3, i + 1, j - 3, j + 1) and \
           [board[i - 3 + k][j - 3 + k] for k in range(3)] == [player, player, player] and board[i + 1][j + 1] == player and board[i][j] == 0:
            moves.append((i, j))
        # 1 - gap - 3
        if is_within_bounds(i - 1, i + 3, j - 1, j + 3) and \
           board[i - 1][j - 1] == player and [board[i + 1 + k][j + 1 + k] for k in range(3)] == [player, player, player] and board[i][j] == 0:
            moves.append((i, j))
    elif search_len == 3:
        # 1 - gap - 2
        if is_within_bounds(i - 1, i + 2, j - 1, j + 2) and \
           board[i - 1][j - 1] == player and [board[i + 1 + k][j + 1 + k] for k in range(2)] == [player, player] and board[i][j] == 0:
            moves.append((i, j))
        # 2 - gap - 1
        if is_within_bounds(i - 2, i + 1, j - 2, j + 1) and \
           [board[i - 2 + k][j - 2 + k] for k in range(2)] == [player, player] and board[i + 1][j + 1] == player and board[i][j] == 0:
            moves.append((i, j))
    return moves


def up_diag_gap_completion(board, i, j, search_len, player):
    moves = []
    if search_len == 4:
        # 2 - gap - 2
        if is_within_bounds(i - 2, i + 2, j + 2, j - 2) and \
           board[i + 2][j - 2] == player and board[i + 1][j - 1] == player and board[i - 1][j + 1] == player and board[i - 2][j + 2] == player and board[i][j] == 0:
            moves.append((i, j))
        # 3 - gap - 1
        if is_within_bounds(i - 3, i + 1, j + 1, j - 3, i+3) and \
           [board[i + 3 - k][j - 3 + k] for k in range(3)] == [player, player, player] and board[i - 1][j + 1] == player and board[i][j] == 0:
            moves.append((i, j))
        # 1 - gap - 3
        if is_within_bounds(i + 1, i - 3, j - 1, j + 3) and \
           board[i + 1][j - 1] == player and [board[i - 1 - k][j + 1 + k] for k in range(3)] == [player, player, player] and board[i][j] == 0:
            moves.append((i, j))
    elif search_len == 3:
        # 1 - gap - 2
        if is_within_bounds(i + 1, i - 2, j - 1, j + 2) and \
           board[i + 1][j - 1] == player and [board[i - 1 - k][j + 1 + k] for k in range(2)] == [player, player] and board[i][j] == 0:
            moves.append((i, j))
        # 2 - gap - 1
        if is_within_bounds(i + 2, i - 1, j - 2, j + 1) and \
           [board[i + 2 - k][j - 2 + k] for k in range(2)] == [player, player] and board[i - 1][j + 1] == player and board[i][j] == 0:
            moves.append((i, j))
    return moves


def find_gap_completion(board, search_len, player):
    moves = set()
    for i in range(protocol.rows):
        for j in range(protocol.cols):
            moves.update(horizontal_gap_completion(board, i, j, search_len, player))
            moves.update(vertical_gap_completion(board, i, j, search_len, player))
            moves.update(fall_diag_gap_completion(board, i, j, search_len, player))
            moves.update(up_diag_gap_completion(board, i, j, search_len, player))
    return list(moves)
