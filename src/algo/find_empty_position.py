import protocol

def find_empty_position(simulationBoard) -> int:
    rows = len(simulationBoard)
    cols = len(simulationBoard[0])   
    emptyBoard = []


    for y in range(cols):
        for x in range(rows):
            if simulationBoard[y][x] == 0:
                emptyBoard.append((y, x))
    return emptyBoard