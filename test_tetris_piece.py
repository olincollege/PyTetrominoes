"""
Test that the piece is implemented properly.
"""
from tetris_piece import Piece

def test_orientation_wraparound():
    """
    Test that piece orientations will wrap around when rotating at the last
    available position.
    """
    testpiece = Piece(3,1)
    testpiece.orientation = 3
    testpiece.rotate()
    assert testpiece.orientation == 0

def test_limited_orientation():
    """
    Test that a piece that has more limited orientations than other piece types
    will stay within those limitations.
    """
    testpiece = Piece(3, 4, 6) #O-block, which has only one orientation
    testpiece.rotate()
    assert testpiece.orientation == 0
