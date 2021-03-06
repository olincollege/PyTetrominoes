"""
Tetris Gameboard Implementation
"""
import time
import pygame
from tetris_piece import Piece

pygame.init() # pylint: disable=no-member

# Initialize sound effects
new_piece_sound = pygame.mixer.Sound("music/new_piece.wav")
place_piece_sound = pygame.mixer.Sound("music/place_piece.wav")
clear_row_sound = pygame.mixer.Sound("music/clear_row.wav")

class TetrisBoard:
    """
    Tetris Board with basic play functionality

    Attributes:
        score: current game score
        state: current state of game (start or finish or quit)
        board: current 20x10 playing field
        height: height of the board
        width: width of the board
        piece: the tetris piece
        x: Left padding of the gameboard
        y: Top padding of the gameboard
    """
    state = "start"
    board = []
    x = 150
    y = 200
    height = 20
    width = 10
    size = 30
    score = 0
    piece = None

    def __init__(self):
        self.score = 0
        self.state = "start"
        self.board = [[-1 for _ in range(self.width)] for _ in range(self.height)]

    def new_piece(self, alt_type = -1):
        """
        Creates a new piece for the gameboard.
        """
        # Creates the piece at the center, top of the board
        self.piece = Piece(3, 0, alt_type)
        # Play the new piece sound effect
        new_piece_sound.play()
        # If the piece intersects itself when created...
        if self.check_collision():
            # ...end the game
            self.state = "end"

    def check_collision(self):
        """
        Check if the falling piece is intersecting with something fixed on the field.
        """
        collision = False
        # For each 4x4 block space piece
        for row in range(self.piece.size):
            for column in range(self.piece.size):
                # Cycles through each 4-length row in a 0-15 reference grid
                # that piece.image is represented with and considers the
                # positions that match those squares
                if row * self.piece.size + column in self.piece.piece_image():
                    # Conditional by row:
                    # - If the current piece width and the piece height
                    # is greater than the base of the board (bottom),
                    # - If the current piece height and the piece width
                    # is greater than the sides of the board (right side),
                    # - If the current piece height and the piece width
                    # is less than zero (left side),
                    # - If the pieces on the board make contact with each other
                    if row + self.piece.y_row > self.height - 1 or \
                            column + self.piece.x_col > self.width - 1 or \
                            column + self.piece.x_col < 0 or \
                            self.board[row + self.piece.y_row][column + self.piece.x_col] != -1:
                        collision = True
        return collision

    def break_line(self):
        """
        Destroy line if pieces make a row.
        """
        # Check each row
        for row in range(1, self.height):
            # Check for the number of empty blocks in a row
            empty_blocks = 0
            # For each block in the row
            for column in range(self.width):
                # If a block in a row is not empty
                if self.board[row][column] == -1:
                    # There must be an empty block, so add one
                    empty_blocks += 1
            # If there are no empty blocks in a single row,
            # there must be a completed row instead
            if empty_blocks == 0:
                # Play the clear row sound effect
                clear_row_sound.play()
                # Since we know there is a completed row, add one
                self.score += 1
                # From the current row and upwards
                for colored_row in range(row, 0, -1):
                    # For each column in the board
                    for colored_column in range(self.width):
                        # replace the deleted row with the row above
                        self.board[colored_row][colored_column] = self.board\
                            [colored_row - 1][colored_column]

    def freeze(self):
        """
        Fix the block in place.
        """
        # For each 4x4 block space piece
        for row in range(self.piece.size):
            for column in range(self.piece.size):
                # Check each individual block in the 4x4 square for the piece
                if row * self.piece.size + column in self.piece.piece_image():
                    # Make the grid points the colors of the halted piece
                    self.board[row + self.piece.y_row][column + self.piece.x_col] = self.piece.color
        # Checks to see if a line can be broken
        self.break_line()
        # Play the place piece sound effect
        place_piece_sound.play()
        # Creates a new piece on the board
        self.new_piece()

    def smash(self):
        """
        Move the block all the way down until it can't move anymore

        Returns:
            landing: the piece before the smash occurred
        """
        # Until the block collides with something
        while self.check_collision() is False:
            # Bring the piece down
            self.piece.y_row += 1
        # When it collides with something, stop the piece
        self.piece.y_row -= 1
        landing = self.piece
        self.freeze()
        return landing

    def go_down(self):
        """
        Move the block down by one space
        """
        # Make the block go down by one
        self.piece.y_row += 1
        time.sleep(0.2)
        # When the piece collides with something, stop it
        if self.check_collision():
            self.piece.y_row -= 1
            self.freeze()

    def go_left(self):
        """
        Move the block to the left
        """
        # Moves the object to the left
        self.piece.x_col -= 1
        # Reject going left if necessary
        if self.check_collision():
            self.piece.x_col += 1

    def go_right(self):
        """
        Move the block to the right.
        """
        # Moves the object to the right
        self.piece.x_col += 1
        # Reject going right if necessary
        if self.check_collision():
            self.piece.x_col -= 1

    def rotate(self):
        """
        Rotate the block if it can be rotated
        """
        # Save the original orientation
        original_orientation = self.piece.orientation
        # Rotate the object
        self.piece.rotate()
        # Reject the rotation if necessary
        if self.check_collision():
            self.piece.orientation = original_orientation
