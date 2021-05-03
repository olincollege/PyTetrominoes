"""
Tetris Piece Implementation
"""
# Import random used to shuffle the different pieces
import random

# Rainbow Colors
colors = [
    (255, 0, 0),
    (255, 127, 0),
    (255, 215, 0),
    (0, 255, 0),
    (0, 0, 255),
    (46, 43, 95),
    (139, 0, 255),
]

class Piece:
    """
    A Tetronominoes Piece

    Attributes:
        x: column of the piece
        y: row of the piece
        type: the type of piece
            (S-shape, Z-shape, T-shape, L-shape,
            Line-shape, Mirrored L-shape, and Square-shape)
        color: color of the piece
        rotation: the orientation of the piece
    """
    # All the pieces in a 4x4 square and their corresponding rotations
    all_pieces = [
        [[1, 5, 9, 13], [4, 5, 6, 7]], # Line block
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]], # J-block
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]], # L-block
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]], # T-block
        [[5, 6, 8, 9], [1, 5, 6, 10]], # S block
        [[4, 5, 9, 10], [2, 5, 6, 9]], # Z block
        [[1, 2, 5, 6]],  # Square block

    # Piece attributes
    def __init__(self, y, x):
        self.x = x
        self.y = y
        self.type = random.choice(self.all_pieces)
        self.color = random.choice(self.colors)
        self.rotation = 0
        self.max_rotation = len(self.type)

    """
    Gets the image of the piece

    Arguments:
        self: represents the instance of the class
    
    Returns:
        the piece type with its current orientation
    """
    def piece_image(self):
        return self.all_pieces[self.type][self.rotation]

    """
    Rotates the piece by choosing the next rotation in line

    Arguments:
        self: represents the instance of the class
    
    Returns:
        the piece type with its current orientation
    """
    