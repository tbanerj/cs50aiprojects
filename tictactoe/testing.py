import sys
import time

from tictactoe import *


board = [['O', 'X', 'X'],
        ['O', 'X', 'X'],
        ['O', "O", "X"]]
print(winner(board))