import os
os.system("clear")

class Board():
    """tic-tac-toe board layout."""

    def __init__(self):
         self.cells = [" "," "," "," "," "," "," "," "," "," "]

    def display(self):
        print(f" {self.cells[1]}|{self.cells[2]}|{self.cells[3]}")
        print("-------")
        print(f" {self.cells[4]}|{self.cells[5]}|{self.cells[6]}")
        print("-------")
        print(f" {self.cells[7]}|{self.cells[8]}|{self.cells[9]}")

    def update_box(self, box_no, player):
        if self.cells[box_no] == " ":
            self.cells[box_no] = player

    def to_win(self, player):
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            return True

    def reset(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]

board = Board()

def print_header():
    print("Welcome to tic-tac-toe\n")

def refresh_screen():
    os.system("clear")
    print_header()
    board.display()

while True:
    refresh_screen()
    #get player X's input
    x_input = int(input("\n (Player X) Choose a box between 1-9. > "))
    board.update_box(x_input, "x")

    refresh_screen()

    if board.to_win("x"):
        print("\n X wins! \n")
        new_game = input("Would you like to play again? (Y/N) >").upper()
        if new_game == "Y":
            board.reset()
            continue
        else:
            break

    #get player o's input
    o_input = int(input("\n Player O) Choose a box between 1-9. > "))
    board.update_box(o_input, "o")
