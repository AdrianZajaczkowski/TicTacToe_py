from board import Board
from constants import SIZE
import tkinter as tk
from tkinter import ttk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.round = 1
        self.title("TicTacToe: Menu")
        positionRight = int(
            self.winfo_screenwidth()/2 - SIZE["WIDTH"])
        positionDown = int(
            self.winfo_screenheight()/2 - SIZE["HEIGHT"])

        self.geometry(f"{positionRight}x{positionDown}")
        print(f"{positionRight}x{positionDown}")

        self.start = ttk.Button(
            self, text="Start the game", command=self._start, width=50)

        self.start.pack()

    def _start(self):

        Board(self.round)
        self.round += 1


if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
