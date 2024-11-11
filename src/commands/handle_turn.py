import protocol

def handle_turn(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("Game board is not initialized.")
        return
    try: 
        _, coordinates = msg.split()
        x, y = map(int, coordinates.split(','))
    except (IndexError, ValueError):
        print("Other player sent invalid coordinates")
        return

    if not (0 <= x < protocol.rows and 0 <= y < protocol.cols):
        print("Other player sent invalid coordinates")
        return

    protocol.gameBoard[x][y] = 2
    ## ICI FAIRE LE CALCUL POUR LE PROCHIAN COUP A JOUER (EN GROS L'IA)
    ## 1 C'EST POUR NOUS ET 2 POUR L'ADVERSAIRE
    xBest, yBest = 0, 0
    protocol.gameBoard[xBest][yBest] = 1
    print(f"{xBest} {yBest}")
