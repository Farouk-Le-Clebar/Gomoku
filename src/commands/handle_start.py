import protocol

def handle_start(msg: str) -> None:
    if len(msg.split()) != 2:
        print("erro command start just accept 2 arguments")
        return
    try:
        size = int(msg.split()[1])
    except (IndexError, ValueError):
        print("unsupported size or other error")
        return

    if size != 20:
        print(" unsupported size or other error")
        return
    protocol.gameBoard = [[0 for _ in range(size)] for _ in range(size)]
    protocol.rows = size
    protocol.cols = size
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
