import protocol

def handle_restart(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("Game board is not initialized.")
        return
    protocol.gameBoard = [[0 for _ in range(protocol.cols)] for _ in range(protocol.rows)]
    print("OK")

