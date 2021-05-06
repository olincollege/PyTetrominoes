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
    state = "start"
    board = []
    x = 150
    y = 240
    height = 20
    width = 10
    size = 30
    score = 0
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
        # Creates the piece at the center, top of the board
        self.piece = Piece(3, 0)
        # If the piece intersects itself when created...
        if self.check_collision():
            # ...end the game
            self.state = "end"
        # Print current state (for testing)
        print(self.state)

    """
    Check if the falling piece is intersecting with something fixed on the field
    """
    def check_collision(self):
        collision = False
        # For each 4x4 block space piece
        for row in range(self.piece.size):
            for column in range(self.piece.size):
                # Check each individual block in the 4x4 square for the piece
                if row * self.piece.size + column in self.piece.piece_image():
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
        # Check each row
        for row in range(1, self.height):
            # Check for the number of empty blocks in a row
            empty_blocks = 0
            # For each block in the row
            for column in range(self.width):
                # If a block in a row is not empty
                if self.board[row][column] == 0:
                    # There must be a colored block, so add one
                    empty_blocks += 1
            # If there are no empty blocks in a single row,
            # there must be a completed row instead
            if empty_blocks == 0:
                # Since we know there is a completed row, add one
                self.score += 1
                # From the current row and upwards
                for colored_row in range(row, 1, -1):
                    # For each column in the board
                    for colored_column in range(self.width):
                        # replace the deleted row with the row above
                        self.board[colored_row][colored_column] = self.board[colored_row - 1][colored_column]
        # Print the current score (for testing)
        print(self.score)

    """
    Check if allowed to move or rotate the Figure
    """
    def freeze(self):
        # For each 4x4 block space piece
        for row in range(self.piece.size):
            for column in range(self.piece.size):
                # Check each individual block in the 4x4 square for the piece
                if row * self.piece.size + column in self.piece.piece_image():
                    # Make the grid points the colors of the halted piece
                    self.board[row + self.piece.y][column + self.piece.x] = self.piece.color
        # Checks to see if a line can be broken
        self.break_line()
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
