"""
Tetris Game Implementation
"""
import time
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
        piece: the tetris piece
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
        self.score = 0
        self.state = "start"
        self.board = [[0 for _ in range(self.width)] for _ in range(self.height)]

    """
    Creates a new piece
    """
    def new_piece(self):
        self.piece = Piece(3, 0)

    """
    Check if the falling piece is intersecting with something fixed on the field
    """
    def check_collision(self):
        collision = False
        # For each 4x4 block space piece
        for row in range(4):
            for column in range(4):
                # Check each individual block in the 4x4 square for the piece
                if row * 4 + column in self.piece.piece_image():
                    # Conditional by row:
                    # - If the current piece width and the piece height
                    # is greater than the base of the board (bottom),
                    # - If the current piece height and the piece width
                    # is greater than the sides of the board (right side), 
                    # - If the current piece height and the piece width
                    # is less than zero (left side),
                    # - If the pieces on the board make contact with each other
                    if row + self.piece.y > self.height - 1 or \
                            column + self.piece.x > self.width - 1 or \
                            column + self.piece.x < 0 or \
                            self.board[row + self.piece.y][column + self.piece.x] > 0:
                        collision = True
        return collision

    """
    Destroy line if pieces make a row
    """
    def break_line(self):
        pass

    """
    Check if allowed to move or rotate the Figure
    """
    def freeze(self):
        # For each 4x4 block space piece
        for row in range(4):
            for column in range(4):
                # Check each individual block in the 4x4 square for the piece
                if row * 4 + column in self.piece.piece_image():
                    # Make the grid points the colors of the halted piece
                    self.board[row + self.piece.y][column + self.piece.x] = self.piece.color
        # Checks to see if a line can be broken
        self.break_line() #TODO: Implement
        # Creates a new piece on the board
        self.new_piece()

    """
    Move the block all the way down until it can't move anymore
    """
    def smash(self):
        # Until the block collides with something
        while self.check_collision() is False:
            # Bring the piece down
            self.piece.y += 1
        # When it collides with something, stop the piece
        self.piece.y -= 1
        self.freeze()

    """
    Move the block down by one space
    """
    def go_down(self):
        # Make the block go down by one
        self.piece.y += 1
        time.sleep(0.2)
        # When the piece collides with something, stop it
        if self.check_collision():
            self.piece.y -= 1
            self.freeze()

    """
    Move the block to the left
    """
    def go_left(self):
        # Moves the object to the left
        self.piece.x -= 1
        # Reject going left if necessary
        if self.check_collision():
            self.piece.x += 1

    """
    Move the block to the right
    """
    def go_right(self):
        # Moves the object to the right
        self.piece.x += 1
        # Reject going right if necessary
        if self.check_collision():
            self.piece.x -= 1

    """
    Rotate the block
    """
    def rotate(self):
        # Save the original orientation
        original_orientation = self.piece.orientation
        # Rotate the object
        self.piece.rotate()
        # Reject the rotation if necessary
        if self.check_collision():
            self.piece.orientation = original_orientation
