from commands.handle_restart import handle_restart
from commands.handle_turn import handle_turn
import protocol

def handle_board(msg: str) -> None:
    handle_restart("")
    lines = msg.split(" ")

    for line in lines:
        line = line.strip()
        if line in ["BOARD", "DONE"]:
            continue
        row, col, val = line.split(',')
        if (val == "2"):
            oppsRow = row
            oppsCol = col
        protocol.gameBoard[int(row)][int(col)] = int(val)

    handle_turn("TURN" + " " + oppsRow + "," + oppsCol)