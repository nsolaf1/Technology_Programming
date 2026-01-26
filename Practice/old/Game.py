import tkinter as tk
import random


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.configure(bg="#1A1A2E")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.difficulty = tk.StringVar(value="Easy")
        self.user_wins = 0
        self.bot_wins = 0

        self.create_ui()
        self.window.mainloop()

    def create_ui(self):
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.window, text="", font=("Arial", 24, "bold"), height=2, width=5,
                            bg="#0F3460", fg="#E94560", relief="ridge", bd=3,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        difficulty_menu = tk.OptionMenu(self.window, self.difficulty, "Easy", "Medium", "Hard")
        difficulty_menu.config(font=("Arial", 12), bg="#16213E", fg="white", relief="ridge")
        difficulty_menu.grid(row=3, column=0, columnspan=3, pady=10)

        self.status_label = tk.Label(self.window, text="Your turn!", font=("Arial", 14, "bold"), bg="#1A1A2E",
                                     fg="white")
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)

        self.leaderboard_label = tk.Label(self.window, text=f"User: {self.user_wins} | Bot: {self.bot_wins}",
                                          font=("Arial", 12, "bold"), bg="#1A1A2E", fg="white")
        self.leaderboard_label.grid(row=5, column=0, columnspan=3, pady=5)

        self.restart_button = tk.Button(self.window, text="Restart", font=("Arial", 14, "bold"), bg="#E94560",
                                        fg="white", relief="ridge", bd=3, command=self.restart_game)
        self.restart_button.grid(row=6, column=0, columnspan=3, pady=10)
        self.restart_button.grid_remove()

    def on_click(self, index):
        if self.board[index] == "" and self.current_player == "X":
            self.make_move(index, "X")
            if not self.check_winner():
                self.window.after(500, self.bot_move)

    def make_move(self, index, player):
        self.board[index] = player
        self.buttons[index].config(text=player, state=tk.DISABLED)
        self.current_player = "O" if player == "X" else "X"

    def bot_move(self):
        if self.current_player == "O":
            index = self.get_bot_move()
            if index is not None:
                self.make_move(index, "O")
                self.check_winner()

    def get_bot_move(self):
        if self.difficulty.get() == "Easy":
            return random.choice([i for i in range(9) if self.board[i] == ""])
        elif self.difficulty.get() == "Medium":
            return self.medium_bot_move()
        else:
            return self.minimax(self.board, "O")[1]

    def medium_bot_move(self):
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "O"
                if self.check_winner(simulate=True):
                    self.board[i] = ""
                    return i
                self.board[i] = ""
        return random.choice([i for i in range(9) if self.board[i] == ""])

    def minimax(self, board, player):
        opponent = "X" if player == "O" else "O"
        winner = self.check_winner(simulate=True)
        if winner == "X": return (-1, None)
        if winner == "O": return (1, None)
        if "" not in board: return (0, None)

        best_score = -float("inf") if player == "O" else float("inf")
        best_move = None

        for i in range(9):
            if board[i] == "":
                board[i] = player
                score = self.minimax(board, opponent)[0]
                board[i] = ""

                if (player == "O" and score > best_score) or (player == "X" and score < best_score):
                    best_score, best_move = score, i

        return (best_score, best_move)

    def check_winner(self, simulate=False):
        for line in [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != "":
                if not simulate:
                    self.status_label.config(text=f"{self.board[line[0]]} wins!")
                    if self.board[line[0]] == "X":
                        self.user_wins += 1
                    else:
                        self.bot_wins += 1
                    self.leaderboard_label.config(text=f"User: {self.user_wins} | Bot: {self.bot_wins}")
                    for btn in self.buttons:
                        btn.config(state=tk.DISABLED)
                    self.restart_button.grid()
                return self.board[line[0]]
        if "" not in self.board:
            if not simulate:
                self.status_label.config(text="It's a tie!")
                self.restart_button.grid()
            return "Tie"
        return None

    def restart_game(self):
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state=tk.NORMAL)
        self.status_label.config(text="Your turn!")
        self.restart_button.grid_remove()


TicTacToe()

def outer(x): def inner(y): return y * 2; for i in range(3): x = inner(x); return x; print(outer(5))?