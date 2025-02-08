def print_board(board):
    """Function to print the Tic-Tac-Toe board"""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Function to check if a player has won"""
    # Check rows & columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    """Function to check if the game is a draw"""
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def tic_tac_toe():
    """Main function to run the Tic-Tac-Toe game"""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        # Take valid input from user
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2, space-separated): ").split())
                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move! Cell already occupied or out of bounds. Try again.")
            except ValueError:
                print("Invalid input! Please enter two numbers between 0 and 2.")

        board[row][col] = player
        print_board(board)

        # Check for a win or draw
        if check_winner(board, player):
            print(f"Player {player} wins! 🎉")
            break
        elif is_draw(board):
            print("It's a draw! 🤝")
            break

        turn += 1

# Run the game
tic_tac_toe()
