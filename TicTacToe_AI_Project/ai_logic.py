import random

# win patterns for 3x3
wins_3 = [
(0,1,2),(3,4,5),(6,7,8),
(0,3,6),(1,4,7),(2,5,8),
(0,4,8),(2,4,6)
]

# win patterns for 4x4
wins_4 = [
(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15),
(0,4,8,12),(1,5,9,13),(2,6,10,14),(3,7,11,15),
(0,5,10,15),(3,6,9,12)
]

def check_winner(board):

    size = int(len(board) ** 0.5)

    wins = wins_3 if size == 3 else wins_4

    for combo in wins:
        values = [board[i] for i in combo]

        if values.count(values[0]) == len(values) and values[0] != "":
            return values[0]

    if "" not in board:
        return "Draw"

    return None


# minimax for 3x3
def minimax(board,is_max):

    result = check_winner(board)

    if result == "O":
        return 1

    if result == "X":
        return -1

    if result == "Draw":
        return 0


    if is_max:

        best = -100

        for i in range(len(board)):

            if board[i] == "":
                board[i] = "O"
                score = minimax(board,False)
                board[i] = ""
                best = max(score,best)

        return best

    else:

        best = 100

        for i in range(len(board)):

            if board[i] == "":
                board[i] = "X"
                score = minimax(board,True)
                board[i] = ""
                best = min(score,best)

        return best


def best_move(board):

    size = int(len(board) ** 0.5)

    # 3x3 use minimax
    if size == 3:

        best_score = -100
        move = -1

        for i in range(len(board)):

            if board[i] == "":
                board[i] = "O"
                score = minimax(board,False)
                board[i] = ""

                if score > best_score:
                    best_score = score
                    move = i

        return move

    # 4x4 smart random move
    else:

        empty = [i for i in range(len(board)) if board[i] == ""]
        return random.choice(empty)