"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None

ROW = 3
COL = 3
N = 3

def initial_state():
    """
    Returns starting state of the board.
    """

    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = sum(row.count(X) for row in board)
    oCount = sum(row.count(O) for row in board)

    return X if xCount <= oCount else O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for row in range(ROW):
        for col in range(COL):
            if board[row][col] == EMPTY: 
                actionSet.add((row, col))
    
    return actionSet

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY:
        raise NameError('InvalidActionError')
    
    resultBoard = [[None for _ in range(ROW)] for _ in range(COL)]
    curPlayer = player(board)

    for row in range(ROW):
        for col in range(COL):
            if row == action[0] and col == action[1]:
                resultBoard[row][col] = curPlayer
            else:
                resultBoard[row][col] = board[row][col]
    
    return resultBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    row_x, col_x, row_o, col_o = [0]*ROW, [0]*COL, [0]*ROW, [0]*COL
    diag_x = anti_diag_x = diag_o = anti_diag_o = 0

    for row in range(ROW):
        for col in range(COL):

            if board[row][col] == X:
                row_x[row] += 1
                col_x[col] += 1               
                if row == col:
                    diag_x += 1
                if row + col == N - 1:
                    anti_diag_x += 1
                
                if N in [row_x[row], col_x[col], diag_x, anti_diag_x]:
                    return X

            elif board[row][col] == O:
                row_o[row] += 1
                col_o[col] += 1
                if row == col:
                    diag_o +=1
                if row + col == N - 1:
                    anti_diag_o += 1
                
                if 3 in [row_o[row], col_o[col], diag_o, anti_diag_o]:
                    return O
    
    return EMPTY

def filled(board):
    if not any(tile is EMPTY for row in board for tile in row):
        return True
    else: 
        return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    if filled(board) or winner(board) != EMPTY:
        return True
    
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player_won = winner(board)
    if player_won == X:
        return 1
    elif player_won == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def recurse(board, limit):
        if terminal(board):
            return utility(board), None
    
        cur_player = player(board)

        if cur_player == X: # need to maximize
            max_score = -float('inf')
            for action in actions(board):
                resultBoard = result(board, action)
                score, _ = recurse(resultBoard, limit)
                if  score > max_score:
                    max_score = score
                    best_action = action

                    if limit != None and score <= limit:
                        break
                    limit = score

            return max_score, best_action
        
        else: # need to minimize
            min_score = float('inf')
            for action in actions(board):
                resultBoard = result(board, action)
                score, _ = recurse(resultBoard, limit)
                if score < min_score:
                    min_score = score
                    best_action = action

                    if limit != None and score >= limit:
                        break
            return min_score, best_action
    
    _, optimalAction = recurse(board, None)
    return optimalAction

    

    



