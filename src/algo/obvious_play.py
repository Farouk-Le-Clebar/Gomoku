import protocol
from obvious_moove_tools.find_align import find_align
from obvious_moove_tools.find_gap_align import find_gap_completion

def find_best_move():
    board = protocol.gameBoard

# Étape 1 : Compléter un alignement direct de 5 pour P1
    coup = find_align(board, search_len=4, player=1)
    if coup:
        return coup

# Étape 1.2 : Compléter un alignement à trou de 5 pour P1
    coup = find_gap_completion(board, search_len=4, player=1)
    if coup:
        return coup

# Étape 2 : Bloquer un alignement direct de 5 pour P2 (adverse)
    coup = find_align(board, search_len=4, player=2)
    if coup:
        return coup
    
# Étape 2.2 : Bloquer un alignement à trou de 5 pour P2 (adverse) 
    coup = find_gap_completion(board, search_len=4, player=2)
    if coup:
        return coup

# Étape 3 : Bloquer un alignement direct de 4 pour P2 (adverse)
    coup = find_align(board, search_len=3, player=2)
    if coup:
        return coup

# Étape 3.2 : Bloquer un alignement à trou de 4 pour P2 (adverse)
    coup = find_gap_completion(board, search_len=3, player=2)
    if coup:
        return coup

# Étape 4 : Compléter un alignement de 4 pour P1
    coup = find_align(board, search_len=3, player=1)
    if coup:
        return coup

# Étape 4.2 : Compléter un alignement à trou de 4 pour P1
    coup = find_gap_completion(board, search_len=3, player=1)
    if coup:
        return coup

    return None
