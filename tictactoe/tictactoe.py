"""
Tic Tac Toe Player
"""
import copy
from hashlib import new
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    if board == initial_state():
        return X
    else:
        xcount = 0
        ocount = 0
        for i in board:
            for j in i:
                if j == X:
                    xcount +=1
                elif j == O:
                    ocount +=1
                else:
                    continue
        if xcount > ocount:
            return O
        else:
            return X


def actions(board):
    emptySpaces = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                emptySpaces.append([i,j])
    return emptySpaces
    

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    currPlayer = player(board)
    if action == None:
        raise Exception('not valid action')
    i = action[0]
    j= action[1]
    if newBoard[i][j] != None:
        raise Exception('not valid space')
    newBoard[i][j] = player(board)
    return newBoard
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i] == [X,X,X]:
            return X
        elif board[i] == [O,O,O]:
            return O
        if [board[0][i],board[1][i],board[2][i]] == [X,X,X]:
            return X
        elif [board[0][i],board[1][i],board[2][i]] == [O,O,O]:
            return O
    if [board[0][0],board[1][1],board[2][2]] == [X,X,X]:
        return X
    elif [board[0][0],board[1][1],board[2][2]] == [O,O,O]:
        return O
    elif [board[0][2],board[1][1],board[2][0]] == [X,X,X]:
        return X
    elif [board[0][2],board[1][1],board[2][0]] == [O,O,O]:
        return O
    else:
        return None
        
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        for j in i:
            if j == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    actionlist = actions(board)
    for i in actionlist:
        updatedBoard = result(board, i)
        if terminal(updatedBoard):
            return i
        else:
            minimax(updatedBoard)
