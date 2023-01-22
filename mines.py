import random
import os

# Initialize the game board
board = [[' ' for _ in range(10)] for _ in range(10)]

# Place the mines
mines = random.sample([(i, j) for i in range(10) for j in range(10)], 5)
for mine in mines:
    x, y = mine
    board[x][y] = '*'

# Initialize the game state
game_over = False

# Game loop
while not game_over:
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    # Draw the board
    for row in board:
        print(' '.join(row))

    # Get the player's move
    x, y = map(int, input("Enter x y coordinates to uncover a cell: ").split())

    # Check if the player uncovered a mine
    if board[x][y] == '*':
        print("Game over! You hit a mine.")
        game_over = True
    else:
        # Count the number of mines around the cell
        mines_around = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < 10 and 0 <= j < 10 and board[i][j] == '*':
                    mines_around += 1
        board[x][y] = str(mines_around)
        if mines_around == 0:
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < 10 and 0 <= j < 10 and board[i][j] == ' ':
                        board[i][j] = '0'
