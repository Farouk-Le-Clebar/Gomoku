import tkinter as tk
from PIL import Image, ImageTk
import os
import time

BASE_PATH = os.path.dirname(__file__)
LOG_FILE = os.path.join(BASE_PATH, "../board.log")
EMPTY_IMG_PATH = os.path.join(BASE_PATH, "assets/empty.png")
PLAYER1_IMG_PATH = os.path.join(BASE_PATH, "assets/player1.png")
PLAYER2_IMG_PATH = os.path.join(BASE_PATH, "assets/player2.png")

def read_board_log(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            board = []
            for line in lines:
                line = line.strip()
                if line.startswith("-") or line.startswith("1") or line.startswith("2"):
                    board.append(list(line))
            return board
    except FileNotFoundError:
        print("Error: board.log file not found.")
        return []
    except Exception as e:
        print(f"Error: {str(e)}")
        return []

def get_board_size(file_path: str) -> tuple:
    board = read_board_log(file_path)
    if board:
        return len(board), len(board[0])
    return 0, 0

def get_file_modification_time(file_path: str) -> float:
    return os.path.getmtime(file_path)

class BoardGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Gomoku Board TTM")

        self.empty_img = ImageTk.PhotoImage(Image.open(EMPTY_IMG_PATH))
        self.player1_img = ImageTk.PhotoImage(Image.open(PLAYER1_IMG_PATH))
        self.player2_img = ImageTk.PhotoImage(Image.open(PLAYER2_IMG_PATH))

        self.labels = []
        self.last_mod_time = get_file_modification_time(LOG_FILE)
        self.update_board_size()
        self.create_board()

        self.check_for_updates()

    def update_board_size(self):
        global ROW_BOARD, COL_BOARD
        ROW_BOARD, COL_BOARD = get_board_size(LOG_FILE)

    def create_board(self):
        for i in range(ROW_BOARD):
            row_labels = []
            for j in range(COL_BOARD):
                label = tk.Label(self.root, image=self.empty_img)
                label.grid(row=i, column=j)
                row_labels.append(label)
            self.labels.append(row_labels)

    def update_board(self):
        board = read_board_log(LOG_FILE)
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == '-':
                    img = self.empty_img
                elif cell == '1':
                    img = self.player1_img
                elif cell == '2':
                    img = self.player2_img
                else:
                    img = self.empty_img

                self.labels[i][j].config(image=img)
                self.labels[i][j].image = img

    def check_for_updates(self):
        current_mod_time = get_file_modification_time(LOG_FILE)
        if current_mod_time != self.last_mod_time:
            self.last_mod_time = current_mod_time
            self.update_board()
        self.root.after(1000, self.check_for_updates)

if __name__ == "__main__":
    root = tk.Tk()
    app = BoardGUI(root)
    root.mainloop()