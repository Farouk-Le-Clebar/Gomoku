import protocol
import random
from algo.find_empty_position import find_empty_position 

def handle_begin(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("ERROR message - Game board is not initialized.")
        return

    empty_positions = find_empty_position(protocol.gameBoard)
    y, x = random.choice(empty_positions)
    protocol.gameBoard[y][x] = 1
    print(f"{y},{x}")
