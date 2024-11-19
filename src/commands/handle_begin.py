import protocol
import random

def handle_begin(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("ERROR message - Game board is not initialized.")
        return

    x = random.choice(range(protocol.rows))
    y = random.choice(range(protocol.cols))

    protocol.gameBoard[x][y] = 1
    print(f"{x},{y}")
