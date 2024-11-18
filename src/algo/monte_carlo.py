import protocol
import random
from algo.find_empty_position import find_empty_position 
from algo.check_simulation import check_event_simulation
from algo.obvious_play import find_best_move
from algo.check_simulation import check_event_simulation

def monte_carlo():
    empty_positions = find_empty_position(protocol.gameBoard)
    best = find_best_move(protocol.gameBoard)
    if (best != None):
        print(f"{best[0]},{best[1]}")
        protocol.gameBoard[best[0]][best[1]] = 1
        return
    else:
        print(f"{empty_positions[0][0]},{empty_positions[0][1]}")
        protocol.gameBoard[empty_positions[0][0]][empty_positions[0][1]] = 1
        return

#     empty_positions = find_empty_position(protocol.gameBoard)
#     for i in range(len(empty_positions)):
#         x, y = empty_positions[i]
#         copyBoard = protocol.gameBoard
#         copyBoard[x][y] = 1

# def simulate(board, profondeur, player, score):
#     if (profondeur == 0):
#         return
#     empty_positions = find_empty_positions(board)
