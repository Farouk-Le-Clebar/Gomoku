from algo.check_simulation import check_event_simulation
from algo.obvious_play import find_best_move
from algo.define_best_area_to_play import define_best_tale_to_play
from commands.handle_begin import handle_begin
import random
import protocol

def check_begin(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                return True
    return False

def monte_carlo():
    deep = 500

    if not check_begin(protocol.gameBoard):
        handle_begin("BEGIN")
        print("DEBUG BEGIN")
        return None

    best = find_best_move(protocol.gameBoard)

    if best is not None:
        protocol.gameBoard[best[0]][best[1]] = 1
        print("DEBUG OBVIOUS")
        return f"{best[0]},{best[1]}"
    else:
        empty_positions = define_best_tale_to_play(protocol.gameBoard, 1)
        win_counts = {pos: 0 for pos in empty_positions}
        reel_deep = deep // len(empty_positions)

        for position in empty_positions:
            for _ in range(reel_deep):
                board = [row[:] for row in protocol.gameBoard]
                board[position[0]][position[1]] = 1
                winner = simulate(board, 2, 0)
                if winner == 1:
                    win_counts[position] += 1

        best_position = max(win_counts, key=win_counts.get)
        protocol.gameBoard[best_position[0]][best_position[1]] = 1
        print(f"DEBUG MONTE CARLO : {win_counts}")
        return f'{best_position[0]},{best_position[1]}'

def simulate(board, player, winner) -> int:
    best_empty_positions = define_best_tale_to_play(board, player)
    y, x = random.choice(best_empty_positions)
    board[y][x] = player

    winner = check_event_simulation(board)
    if winner != 0:
        return winner

    return simulate(board, 3 - player, winner)
