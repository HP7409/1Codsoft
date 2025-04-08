import math

# Constants for the board
PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '  # Empty space on the board

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the game is a draw
def is_draw(board):
    return all([board[i][j] != EMPTY for i in range(3) for j in range(3)])

# Function to get all available moves
def available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, PLAYER_X):
        return -1  # Player X wins
    if check_winner(board, PLAYER_O):
        return 1  # AI (Player O) wins
    if is_draw(board):
        return 0  # It's a draw

    if is_maximizing:
        max_eval = -math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = PLAYER_O
            eval = minimax(board, depth + 1, False, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in available_moves(board):
            board[move[0]][move[1]] = PLAYER_X
            eval = minimax(board, depth + 1, True, alpha, beta)
            board[move[0]][move[1]] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to get the best move for the AI
def best_move(board):
    max_eval = -math.inf
    best_move = None
    for move in available_moves(board):
        board[move[0]][move[1]] = PLAYER_O
        eval = minimax(board, 0, False, -math.inf, math.inf)
        board[move[0]][move[1]] = EMPTY
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return best_move

# Function to play the game
def play_game():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("Player X is human, Player O is AI.")
    
    while True:
        print_board(board)
        
        # Human player's move (X)
        print("Your turn (Player X):")
        while True:
            try:
                row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_X
                    break
                else:
                    print("The spot is already taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column numbers (0-2).")
        
        # Check for win or draw
        if check_winner(board, PLAYER_X):
            print_board(board)
            print("Player X wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # AI's move (O)
        print("AI's turn (Player O):")
        ai_move = best_move(board)
        board[ai_move[0]][ai_move[1]] = PLAYER_O
        
        # Check for win or draw
        if check_winner(board, PLAYER_O):
            print_board(board)
            print("Player O (AI) wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
