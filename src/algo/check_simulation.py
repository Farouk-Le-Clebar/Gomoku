import protocol

def check_event_simulation(simulationBoard) -> int:
    rows = len(simulationBoard)
    cols = len(simulationBoard[0])    
    for y in range(cols):
        for x in range(rows):
            if simulationBoard[x][y] == 1:
                if check_event(simulationBoard, x, y, 1):
                    return 1
            if simulationBoard[x][y] == 2:
                if check_event(simulationBoard, x, y, 2):
                    return 2
    return 0

def check_event(simulationBoard, x, y, value) -> bool:
    if check_horizontal(simulationBoard, x, y, value):
        return True
    if check_vertical(simulationBoard, x, y, value):
        return True
    if check_diagonal1(simulationBoard, x, y, value):
        return True
    if check_diagonal2(simulationBoard, x, y, value):
        return True
    return False

def check_horizontal(simulationBoard, x, y, value) -> bool:
    count = 0
    for i in range(5):
        if y + i >= 20:
            break
        if simulationBoard[x][y + i] == value:
            count += 1
        else:
            break
    if count == 5:
        return True
    return False

def check_vertical(simulationBoard, x, y, value) -> bool:
    count = 0
    for i in range(5):
        if x + i >= 20:
            break
        if simulationBoard[x + i][y] == value:
            count += 1
        else:
            break
    if count == 5:
        return True
    return False

def check_diagonal1(simulationBoard, x, y, value) -> bool:
    count = 0
    for i in range(5):
        if x + i >= 20 or y + i >= 20:
            break
        if simulationBoard[x + i][y + i] == value:
            count += 1
        else:
            break
    if count == 5:
        return True
    return False

def check_diagonal2(simulationBoard, x, y, value) -> bool:
    count = 0
    for i in range(5):
        if x + i >= 20 or y - i < 0:
            break
        if simulationBoard[x + i][y - i] == value:
            count += 1
        else:
            break
    if count == 5:
        return True
    return False