import protocol
from algo.monte_carlo import monte_carlo

def handle_turn(msg: str) -> None:
    if ((protocol.gameBoard is None) or (protocol.rows == 0 or protocol.cols == 0)):
        print("ERROR message - Game board is not initialized.")
        return
    try: 
        _, coordinates = msg.split()
        x, y = map(int, coordinates.split(','))
    except (IndexError, ValueError):
        print("ERROR message - Other player sent invalid coordinates")
        return

    if not (0 <= x < protocol.rows and 0 <= y < protocol.cols):
        print("ERROR message - Other player sent invalid coordinates")
        return

    protocol.gameBoard[x][y] = 2
    monte_carlo()
