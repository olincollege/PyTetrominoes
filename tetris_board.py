"""
Tetris Game Implementation
"""
from tetris_piece import Piece

class TetrisBoard:
    """
    Tetris Board with basic play functionality

    Attributes:
        score: current game score
        state: current state of game (start or finish)
        board: current 20x10 playing field
        height: height of the board
        width: width of the board
        Piece: the piece
    """
    score = 0
    state = None
    board = []
    height = 0
    width = 0
    Piece = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.box = []
        self.score = 0
        self.state = "start"
        # Create a empty playing field
        for row in range(height):
            new_line = []
            for column in range(width):
                new_line.append(0)
            self.box.append(new_line)

    """
    Creates a new piece
    """
    def new_piece(self):
        self.piece = Piece(0,0)

    """
    Check if the falling piece is intersecting with something fixed on the field
    """
    def intersects(self):
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
    def go_space(self):
        pass

    """
    Move the block down by one space
    """
    def go_down(self):
        pass

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
