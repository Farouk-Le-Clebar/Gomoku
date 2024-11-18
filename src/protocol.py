import sys
from enum import Enum
from typing import Callable
# COMMANDS
from commands.handle_about import handle_about
from commands.handle_begin import handle_begin
from commands.handle_board import handle_board
from commands.handle_end import handle_end
from commands.handle_info import handle_info
from commands.handle_start import handle_start
from commands.handle_turn import handle_turn
# BONUS
from commands.handle_restart import handle_restart
from commands.handle_displayInfo import handle_displayInfo
from commands.handle_rectstart import handle_rectstart
from commands.handle_takeback import handle_takeback

settings = { 
    "timeout_turn": 0, 
    "timeout_match": 0, 
    "max_memory": 0, 
    "time_left": 0, 
    "game_type": 0, 
    "rule": 0, 
    "evaluate": (0, 0), 
    "folder": ""
}

need_stop = False
gameBoard = None
rows = 0
cols = 0

class LogType(Enum):
    UNKNOWN = 0
    ERROR = 1
    MESSAGE = 2
    DEBUG = 3

    def __str__(self):
        return f"{self.name}"


def send_log(log_type: LogType, msg: str):
    print(f"{str(log_type)} {msg}")


COMMAND_MAPPINGS: dict[str, Callable[[str], None]] = {
    "ABOUT": handle_about,
    "START": handle_start,
    "END": handle_end,
    "INFO": handle_info,
    "BEGIN": handle_begin,
    "TURN": handle_turn,
    "BOARD": handle_board,
    "RESTART": handle_restart,
    "DISPLAYINFO": handle_displayInfo,
    "RECTSTART": handle_rectstart,
    "TAKEBACK": handle_takeback,
}

def handle_command(cmd: str) -> None:
    cmd_u = cmd.split()[0].upper()
    if cmd_u not in COMMAND_MAPPINGS:
        return send_log(LogType.UNKNOWN, "command is not implemented")
    return COMMAND_MAPPINGS[cmd_u](cmd)


def main() -> int:
    while need_stop is False:
        try:
            cmd = input()
        except EOFError:
            return 0
        handle_command(cmd)
    return 0


if __name__ == "__main__":
    sys.exit(main())