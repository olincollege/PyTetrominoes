"""
Tetris Piece Implementation
"""
# Import random used to shuffle the different pieces
import random

# Rainbow Colors
colors = [
    (255, 0, 0), # red
    (255, 127, 0), # orange
    (255, 215, 0), # yellow
    (0, 255, 0), # green
    (0, 255, 255), # blue
    (139, 0, 255), # violet
    (255, 20, 147) # pink
]

class Piece:
    """
    A Tetronominoes Piece

    Attributes:
        x: location of the piece on the x-axis
        y: location of the piece on the y-axis
        type: the type of piece
            (S-shape, Z-shape, T-shape, L-shape,
            Line-shape, Mirrored L-shape, and Square-shape)
        color: color of the piece
        rotation: the orientation of the piece
        size: dimension of the piece in its rotation
    """
    # All the pieces in a 4x4 square and their corresponding rotations
    all_pieces = [
        [[1, 5, 9, 13], [4, 5, 6, 7]], # Line block
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]], # L-block
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], # Mirrored L-block
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], # T-block
        [[5, 6, 8, 9], [1, 5, 6, 10]], # S block
        [[4, 5, 9, 10], [2, 5, 6, 9]], # Z block
        [[1, 2, 5, 6]],  # Square block
    ]

    # Piece attributes
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.all_pieces) - 1)
        self.color = random.randint(1, len(colors) - 1)
        self.orientation = 0
        self.size = 4

    """
    Gets the image of the piece

    Arguments:
        self: represents the instance of the class
    
    Returns:
        the piece type with its current orientation
    """
    def piece_image(self):
        return self.all_pieces[self.type][self.orientation]

    """
    Rotates the piece by choosing the next rotation in line

    Arguments:
        self: represents the instance of the class
    
    Returns:
        the piece type with its current orientation
    """
    def rotate(self):
        # get the original orientation before rotation
        original_orientation = self.orientation
        # if the original orientation is going to be out of bounds
        if original_orientation >= len(self.all_pieces[self.type])-1:
            # change the orientation to the initial orientation
            self.orientation = 0
        else:
            # if not, go to the next orientation
            self.orientation += 1
