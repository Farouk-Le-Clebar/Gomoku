import protocol

def handle_rectstart(msg: str) -> None:
    if len(msg.split()) != 3:
        print("erro command start just accept 3 arguments")
        return
    try:
        sizeX = int(msg.split()[1])
        sizeY = int(msg.split()[2])
    except (IndexError, ValueError):
        print("unsupported size or other error")
        return

    protocol.gameBoard = [[0 for _ in range(sizeY)] for _ in range(sizeX)]
    protocol.rows = sizeX
    protocol.cols = sizeY
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
    print("OK")
