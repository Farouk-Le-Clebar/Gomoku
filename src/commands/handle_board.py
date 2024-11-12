from commands.handle_restart import handle_restart
from commands.handle_turn import handle_turn
import protocol

def handle_board(msg: str) -> None:
    handle_restart("BOARD")
    while True:
        msg = input()
        if msg == "DONE":
            break
        try:
            row, col, val = msg.split(',')
        except ValueError:
            print("ERROR: Invalid input format. Expected 'row,col,val'")
            continue
        if val == "2":
            oppsRow, oppsCol = row, col
        if val != "1" and val != "2":
            print("ERROR: The value must be 1 or 2")
            continue
        if int(row) >= protocol.rows or int(col) >= protocol.cols:
            print("ERROR: The row or column is out of bounds")
            continue
        if int(row) < 0 or int(col) < 0:
            print("ERROR: The row or column is out of bounds")
            continue
        protocol.gameBoard[int(row)][int(col)] = int(val)

    handle_turn(f"TURN {oppsRow},{oppsCol}")
