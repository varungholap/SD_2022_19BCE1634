from Pieces import *

from Pieces.Pieces1 import Piece1
from Position import Position
class Chess:
    def __init__(self,n,A,B):
        self.n=n
        self.board = [[Piece1("-",0,0,0) for i in range(n)] for i in range(n)]
        self.board[0]=B
        self.board[n-1]=A
        self.flag=True
