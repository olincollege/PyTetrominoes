
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
    (0, 0, 255), # blue
    (46, 43, 95), # indigo
    (139, 0, 255), # violet
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
        self.type = random.choice(self.all_pieces)
        self.color = random.choice(colors)
        self.rotation = 0
        self.empty = (0,0,0)

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
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])

    # """
    # Rotate the block
    # """
    # def rotate(self):
    #     if not self.touch_rotate():
    #         if self.piece.rotation >= self.piece.max_rotation - 1:
    #             self.piece.rotation = 0
    #         else:
    #             self.piece.rotation += 1
