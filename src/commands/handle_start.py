import protocol

def handle_start(msg: str) -> None:
    try:
        size = int(msg.split()[1])
    except (IndexError, ValueError):
        print("unsupported size or other error")
        return

    if size != 20:
        print(" unsupported size or other error")
        return
    protocol.gameBoard = [[0 for _ in range(20)] for _ in range(20)]
    protocol.rows = 20
    protocol.cols = 20
    print("OK")
