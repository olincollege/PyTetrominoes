"""
Tests for the game board class.
"""

from tetris_board import TetrisBoard


def test_check_collision():
    """
    Check that collisions are handled properly.
    """
    board = TetrisBoard()
    #Places a z block at the top of the board
    board.new_piece(5)
    board.board[2][5] = 3 #Places a Green square at the 3rd row and 5th column,
    #which should intersect with the bottom right corner of the z-block.
    assert board.check_collision() == True

def test_new_piece():
    """
    Check that the board properly handles new pieces
    """
    board = TetrisBoard()
    board.new_piece()
    assert not board.check_collision()

def test_go_right():
    """
    Check that a collision with the right wall is detected
    """
    #creates an empty board
    board = TetrisBoard()
    #creates an "O" block at the right wall
    board.new_piece(6)
    board.piece.x_col = 7
    board.piece.y_row = 0
    board.go_right()
    #write the piece onto the board
    board.freeze()
    print(str(board))
    #Tests the square that would be empty if collision detection were to fail
    assert board.board[0][8] == 6

def test_go_left():
    """
    Check that a collision with the left wall is detected
    """
    #creates an empty board
    board = TetrisBoard()
    #creates an O block at the left wall in the board coordinate system
    board.new_piece(6)
    board.piece.x_col = -1
    board.piece.y_row = 0
    board.go_left()
    board.freeze()
    #Tests the square that would be empty if collision detection were to fail
    assert board.board[0][1] == 6

def test_rotation():
    #Collision with a clockwise rotation. The obstruction is a piece that
    #is fixed in the 3rd row and 5th column.
    board = TetrisBoard()
    board.new_piece(0)
    board.board[1][4] = 2
    board.rotate()
    board.freeze()
    #Tests that the rotation did not change because a collision was detected
    assert board.piece.orientation == 0

def test_smash():
    """
    Check that a smash leaves the block on the appropriate level and that
    after a smash, the y_row value of the piece on the board resets to 0.
    """
    board = TetrisBoard()
    board.board[19][3] = 5 #Puts a green block on the 20th row and 4th column.
    board.new_piece(0) #Places a Line block which by default runs column 3-6
    board.smash()
    assert board.board[18][4] == 0
    assert board.piece.y_row == 0

def test_freeze():
    """
    Check that a block will freeze at the proper coordinates.
    """
    board = TetrisBoard()
    board.new_piece(1) #Creates L-block at the 4th-5th column and 
    board.piece.orientation = 2 #sets upside-down orientation
    board.freeze()
    assert board.board[0][4] == 1
    assert board.board[0][5] == 1
    assert board.board[1][5] == 1
    assert board.board[2][5] == 1
    assert board.board[2][4] != 1
    assert board.board[19][4] == -1

def test_go_down():
    """
    Tests that the go_down function properly pushes blocks down.
    """
    board = TetrisBoard()
    board.new_piece(0) #places a line block
    #Checks the board below the line block for an empty space
    assert board.board[4][4] == -1
    board.go_down()
    board.freeze()
    assert board.board[4][4] == 0 #Checks that the block has moved into place
    assert board.board[0][4] == -1 #checks the block above the spawnpoint for
    #a vacancy


def test_break_line():
    """
    Check that a line break shifts all lines above down properly.
    """
    board = TetrisBoard()
    #Fill 4 rows in the middle of the board, with full rows sandwiching
    #an incomplete row and with another incomplete row on top
    for y in range(4):
        for x in range(10):
            board.board[y+13][x] = 5
    board.board[13][6] = 2
    board.board[13][9] = -1
    board.board[15][4] = -1
    board.break_line()
    #Check that the uncleared line was moved down by 1
    assert board.board[16][7] == 5
    assert board.board[16][2] == 5
    #Check that the cleared lines did not drop more than 1
    assert board.board[17][7] == -1
    #Check that the top uncleared line was moved down by 2
    assert board.board[15][2] == 5
    assert board.board[15][4] == 5
    assert board.board[15][6] == 2
    assert board.board[14][2] == -1