import sys
import time

from tictactoe import *


board = [[O, X, O],
        [O, X, O],
        [X, O, X]]

print("Player " + player(board))
print("Actions ")
print(actions(board))
for i in actions(board):
    print("Result ")
    print(result(board, i))

print("Winner " + str(winner(board)))
print("Terminal " + str(terminal(board)))
print("Utility " + str(utility(board)))