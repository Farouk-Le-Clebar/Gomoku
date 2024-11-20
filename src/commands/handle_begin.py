import protocol
import random
from algo.find_empty_position import find_empty_position 

def handle_begin(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("ERROR message - Game board is not initialized.")
        return

    if protocol.gameBoard[protocol.rows // 2][protocol.cols // 2] == 0:
        protocol.gameBoard[protocol.rows // 2][protocol.cols // 2] = 1
        print(f"{protocol.rows // 2},{protocol.cols // 2}")
    else:
        protocol.gameBoard[protocol.rows // 2 + 1][protocol.cols // 2 + 1] = 1
        print(f"{protocol.rows // 2 + 1},{protocol.cols // 2 + 1}")