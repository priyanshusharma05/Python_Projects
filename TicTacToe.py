import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()

    def create_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2, command=lambda row=row, col=col: self.make_move(row, col))
                self.buttons[row][col].grid(row=row, column=col)

    def make_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(row, col):
                self.display_winner()
            elif self.check_draw():
                self.display_draw()
            else:
                self.switch_player()

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def check_win(self, row, col):
        for i in range(3):
            if self.board[i][col] != self.current_player:
                break
        else:
            return True

        for j in range(3):
            if self.board[row][j] != self.current_player:
                break
        else:
            return True

        if row == col:
            for i in range(3):
                if self.board[i][i] != self.current_player:
                    break
            else:
                return True

        if row + col == 2:
            for i in range(3):
                if self.board[i][2-i] != self.current_player:
                    break
            else:
                return True

        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def display_winner(self):
        messagebox.showinfo("Winner!", f"{self.current_player} wins!")
        self.reset_board()

    def display_draw(self):
        messagebox.showinfo("Draw!", "It's a draw!")
        self.reset_board()

    def reset_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
                self.board[row][col] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()


