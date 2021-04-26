"""Code for the model of the tetromino drop game."""

class board:
    """
    The board and the pieces that go on it.

    #the following positions represent the model of each piece on our board.
    #uh this might not be necessary
    #i_block = [[0, 0, 0, 1, 1, 1, 1, 0, 0, 0,]]
    #j_block = [[],[]]
    """
    
    def __init__(self):
        #creates a 20 tall 10 wide board with no pieces.
        #board[0] is the bottom row. board[0][9] is bottom right.
        self.board = np.array([[0 for x in range(10)] for _ in range(20)])

    def __repr__(self):
        print(self.board)

    def move(self, active_piece):

    def move_left(self):
        target = self.move
        self.board

    def move_right(self):


    def rotate(self):
        """
        Rotates the piece clockwise.
        """


class piece:
    """
    Handles the pieces.

    I-block: a 4x1 row. Example below.
    ■■■■
    J-block: a 3x1 row with a block on the top left. Example below.
    ■
    ■■■
    L-block: a 3x1 row with a block on the top right. Example below.
      ■
    ■■■
    O-block: a 2x2 block. Example below.
    ■■
    ■■
    S-block: a 2x1 row with a 2x1 row appended to the top right. Example below.
     ■■
    ■■
    T-block: a 3x1 row with a block on the top middle. Example below.
     ■
    ■■■
    Z-block: a 2x1 row with a 2x1 row appended to the top left. Example below.
    ■■
     ■■
    """ 

    i_block = np.array([[0, 0, 0, 1, 1, 1, 1, 0, 0, 0]])
    
    j_block = np.array([[0, 0, 0, 2, 0, 0, 0, 0, 0, 0],\
                        [0, 0, 0, 2, 2, 2, 0, 0, 0, 0]])

    l_block = np.array([[0, 0, 0, 0, 0, 3, 0, 0, 0, 0],\
                        [0, 0, 0, 3, 3, 3, 0, 0, 0, 0]])

    o_block = np.array([[0, 0, 0, 0, 4, 4, 0, 0, 0, 0],\
                        [0, 0, 0, 0, 4, 4, 0, 0, 0, 0]])

    s_block = np.array([[0, 0, 0, 5, 5, 0, 0, 0, 0, 0],\
                        [0, 0, 0, 0, 5, 5, 0, 0, 0, 0]])

    t_block = np.array([[0, 0, 0, 0, 6, 0, 0, 0, 0, 0],\
                        [0, 0, 0, 6, 6, 6, 0, 0, 0, 0]])

    z_block = np.array([[0, 0, 0, 7, 7, 0, 0, 0, 0, 0],\
                        [0, 0, 0, 0, 7, 7, 0, 0, 0, 0]])
    pass

class score:
    """
    Keeps tabs on the current score and the player level.
    """



"""
Code for the view of the tetromino drop game.
"""
#Create a main view with subcomponent views (calls draw method for each etc)

#From the PyGame docs. Make sure to use pip install pygame if not installed.
import pygame
import pygame.locals
class boardView:
    pass

class pygameBoardView(boardView):
    pass

class scoreView:
    """
    Displays both the game level and the game score from the game model.
    """
    pass

class pygameScoreView(scoreView):
    pass


"""Code for the control interface of the tetromino drop game."""

class movePiece:
    pass

class pygameMovePiece(movePiece):
    pass