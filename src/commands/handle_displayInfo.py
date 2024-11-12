import protocol

def handle_displayInfo(msg: str) -> None:
    print(protocol.settings)
    for row in protocol.gameBoard:
        print(row)
