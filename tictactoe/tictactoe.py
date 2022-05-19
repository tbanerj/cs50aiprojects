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
    i = action[0][0]
    j= action[1][1]
    board[i][j] = player(board)
    return board
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i] == [X,X,X]:
            return X
        elif board[i] == [O,O,O]:
            return O
    if [board[0],board[1],board[2]] == [X,X,X]:
        print([board[0],board[1],board[2]])
        return X
    elif [board[0],board[1],board[2]] == [O,O,O]:
        print([board[0],board[1],board[2]])
        return O
    elif [board[0][0],board[1][1],board[2][2]] == [X,X,X]:
        print([board[0][0],board[1][1],board[2][2]])
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
    for i in board:
        for j in i:
            if j == None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
