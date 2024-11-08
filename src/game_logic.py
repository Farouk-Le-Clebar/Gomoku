class GomokuGame:
    def __init__(self):
        self.board = [[0 for _ in range(20)] for _ in range(20)]

    def play_move(self, x: int, y: int, player: int) -> bool:
        if self.board[x][y] == 0:
            self.board[x][y] = player
            return True
        return False

    def check_winner(self) -> int:
        pass