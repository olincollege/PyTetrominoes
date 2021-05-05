"""
Tetris Game Implementation
"""
import time
from tetris_piece import Piece

class TetrisBoard:
    """
    Tetris Board with basic play functionality

    Attributes:
        height: height of the board
        width: width of the board
        board: current 20x10 playing field
        score: current game score
        level: game level based on rows cleared
        state: current state of game (start or finish)
        Piece: the piece
    """
    score = 0
    state = "start"
    board = []
    height = 20
    width = 10
    x = 100
    y = 60
    size = 20
    piece = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = []
        self.score = 0
        self.level = 1
        self.state = "start"
        for row in range(height):
            new_line = []
            for column in range(width):
                new_line.append(0)
            self.board.append(new_line)
    
    def __repr__(self):
        print(f"score: {self.score},\n ")
        print(f"current squares on board:\n{self.board}")
        print(f"Current level is {self.level}")

    """
    Creates a new piece
    """
    def new_piece(self):
        self.piece = Piece(3,0)

    """
    Check if the piece is touching something fixed on the field
    """
    def touches(self):
        pass

    """
    Destroy line if pieces make a row
    """
    def break_line(self):
        pass


    """
    Check if allowed to move or rotate the Figure
    """
    def freeze(self):
        pass

    """
    Move the block all the way down until it can't move anymore
    """
    def smash(self):
        pass

    """
    Move the block down by one space
    """
    def go_down(self):
        self.piece.y += 1
        time.sleep(0.2)

    """
    Move the block sideways
    """
    def go_side(self):
        pass

    """
    Rotate the block
    """
    def rotate(self):
        pass
