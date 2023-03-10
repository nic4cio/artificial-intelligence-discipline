import math

# shows the tic tac toe board game
def show_board(board):
    print("-------------")
    ## size of the board
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + str(board[i][j]) + " |", end="")
        print("\n-------------")

# function that gets available moves for players to mark the position
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                moves.append((i, j))
    return moves

# function that gets the score of the game 
def get_score(board):
    score = 0
    # check rows
    for i in range(3):
        row_sum = sum(board[i])
        if row_sum == 3:
            ## if row_sum == 3 score is the positive infinity
            score = math.inf
            break
        elif row_sum == -3:
            ## if row_sum == -3 score is the negative infinity
            score = -math.inf
            break
    # check columns
    if score == 0:
        for i in range(3):
            # column sum
            col_sum = board[0][i] + board[1][i] + board[2][i]
            if col_sum == 3:
                score = math.inf
                break
            elif col_sum == -3:
                score = -math.inf
                break
    # checking diagonals
    if score == 0:
        # principal diagonal 
        diag1_sum = board[0][0] + board[1][1] + board[2][2]
        # secondary diagonal
        diag2_sum = board[0][2] + board[1][1] + board[2][0]
        if diag1_sum == 3 or diag2_sum == 3:
            score = math.inf
        elif diag1_sum == -3 or diag2_sum == -3:
            score = -math.inf
    return score

# minimax algorithm
def minimax(board, depth, is_maximizer):
    available_moves = get_available_moves(board)
    score = get_score(board)
    if score == math.inf:
        return score - depth
    elif score == -math.inf:
        return score + depth
    elif not available_moves:
        return 0
    if is_maximizer:
        best_score = -math.inf
        for move in available_moves:
            new_board = [row[:] for row in board]
            new_board[move[0]][move[1]] = 1
            score = minimax(new_board, depth+1, False)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in available_moves:
            new_board = [row[:] for row in board]
            new_board[move[0]][move[1]] = -1
            score = minimax(new_board, depth+1, True)
            best_score = min(best_score, score)
        return best_score

def get_best_move(board):
    available_moves = get_available_moves(board)
    best_score = -math.inf
    best_move = None
    for move in available_moves:
        new_board = [row[:] for row in board]
        new_board[move[0]][move[1]] = 1
        score = minimax(new_board, 0, False)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("welcome to tic tac toe")
    show_board(board)
    while True:
        player_move = input("insira o movimento no seguinte formato: row,col: ")
        row, col = map(int, player_move.split(","))
        if board[row][col] != 0:
            print("invalid move, try again.")
            continue
        board[row][col] = -1
        show_board(board)
        if get_score(board) == -math.inf:
            print("you win!")
            break
        if not get_available_moves(board):
            print("draw!")
            break
        computer_move = get_best_move(board)
        board[computer_move[0]][computer_move[1]] = 1
        print("machine move: " + str(computer_move))
        show_board(board)
        if get_score(board) == math.inf:
            print("machine wins!")
            break
        if not get_available_moves(board):
            print("draw!")
            break


def main():
    play()

if __name__ == "__main__":
    main()
