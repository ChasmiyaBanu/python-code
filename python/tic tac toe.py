def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'O'

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        row = int(input("Enter row (1-2): ")) - 1
        col = int(input("Enter column (1-2): ")) - 1

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print("That position is already taken! Try again.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch turns
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
