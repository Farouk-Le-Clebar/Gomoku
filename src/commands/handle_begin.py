import protocol

def handle_begin(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("ERROR message - Game board is not initialized.")
        return

    x = 0
    y = 0

    x = (protocol.rows // 2)
    y = (protocol.cols // 2)

    protocol.gameBoard[x][y] = 1
    print(f"{x},{y}")

