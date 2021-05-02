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
    field = None
    height = 0
    width = 0
    x = None
    y = None
    figure = None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.field = []
        self.score = 0
        self.state = "start"
        # Create a empty playing field
        for row in range(height):
            new_line = []
            for column in range(width):
                new_line.append(0)
            self.field.append(new_line)

    """
    Creates a new active piece
    """
    def new_piece(self):
        self.piece = Piece(0,0)

    def global_coordinates(self):
        """
        Gives the global coordinates of a piece's location
        based on its rotation and the reference frame coordinates.

        returns:
            global_coordinates:
            A list of four lists, each containing the x and y coordinates
            (column and row number) of each block in the piece.
        """

        blocks = self.piece.type[self.piece.rotation]
        
        #maps each square from 0 to 15 in our mini-grid system to a coordinate
        block_to_coordinates = [
            [0,0],[1,0],[2,0],[3,0],
            [0,1],[1,1],[2,1],[3,1],
            [0,2],[1,2],[2,2],[3,2],
            [0,3],[1,3],[2,3],[3,3]
            ]

        x = self.piece.x
        y = self.piece.y
        for i in range(4):
            ref_frame[i] = self.piece.type[self.piece.rotation][i]
            global_coordinates[i] = block_to_coordinates[ref_frame[i]]

        return global_coordinates







    """
    Check if the falling piece is intersecting with something fixed on the field
    """
    def left_touch(self):
        for global_coordinates(self)
        if self.piece

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
        if not left_touch(self):
            self.piece.x = self.piece.x - 1
    
    def go_right(self):
        if not right_touch(self):
            self.piece.x = self.piece.x + 1

    """
    Rotate the block
    """
    def rotate(self):
        if self.piece.rotation >= self.piece.max_rotation - 1:
            self.piece.rotation = 0
        else:
            self.piece.rotation += 1
