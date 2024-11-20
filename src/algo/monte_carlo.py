import protocol
import random
from algo.find_empty_position import find_empty_position 
from algo.check_simulation import check_event_simulation
from algo.obvious_play import find_best_move
from algo.define_best_area_to_play import define_best_tale_to_play
from commands.handle_begin import handle_begin

def check_begin(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                return True
    return False

def monte_carlo():
    deep = 25
    if not check_begin(protocol.gameBoard):
        handle_begin("BEGIN")
        print("DEBUG BEGIN")
        return None

    best = find_best_move(protocol.gameBoard)
    best_score = [float('inf'), 0, 0]
    list_score = []

    if best is not None:
        protocol.gameBoard[best[0]][best[1]] = 1
        print("DEBUG OBVIOUS")
        return f"{best[0]},{best[1]}"
    else:
        empty_positions = define_best_tale_to_play(protocol.gameBoard, 1)
        for i in range(len(empty_positions)):
            x, y = empty_positions[i]
            copyBoard = [row[:] for row in protocol.gameBoard]
            copyBoard[x][y] = 1
            score = simulate(copyBoard, deep, 2, 0)
            list_score.append([score, x, y])

        for score, x, y in list_score:
            if score < best_score[0]:
                best_score = [score, x, y]
        
        print(f"DEBUG MONTE CARLO : {best_score}")
        protocol.gameBoard[best_score[1]][best_score[2]] = 1
        return f'{best_score[1]},{best_score[2]}'

def simulate(board, profondeur, player, score) -> int:
    score += 1

    if profondeur == 0:
        return score

    if player == 1:
        best = find_best_move(protocol.gameBoard)
        if best:
            board[best[0]][best[1]] = player
            score = simulate(board, profondeur - 1, 3 - player, score)
            return score

    empty_positions = define_best_tale_to_play(board, player)
    randTale = random.choice(empty_positions)
    board[randTale[0]][randTale[1]] = player

    check = check_event_simulation(board)

    if check == 1:
        print("DEBUG MC WIN")
        return score
    elif check == 2:
        print("DEBUG MC LOOSE")
        return score

    score = simulate(board, profondeur - 1, 3 - player, score)
    return score