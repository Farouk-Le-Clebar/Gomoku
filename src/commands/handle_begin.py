import protocol

def handle_begin(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("ERROR message - Game board is not initialized.")
        return

    x = 2
    y = 17

    protocol.gameBoard[x][y] = 1
    print(f"{x},{y}")

