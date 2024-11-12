import protocol

def handle_restart(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("ERROR message - Game board is not initialized.")
        return
    protocol.gameBoard = [[0 for _ in range(protocol.cols)] for _ in range(protocol.rows)]
    protocol.settings ={
        "timeout_turn": 0, 
        "timeout_match": 0, 
        "max_memory": 0, 
        "time_left": 0, 
        "game_type": 0, 
        "rule": 0, 
        "evaluate": (0, 0), 
        "folder": ""
    }
    if (msg != "BOARD"):
        print("OK")

