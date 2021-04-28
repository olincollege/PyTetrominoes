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
    Tetris Piece
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = None # TODO: must initialize the pieces first
        self.color = random.randint(1, len(colors) - 1)
        self.rotation = 0