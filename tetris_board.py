"""
Tetris Game Implementation
"""
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
        Piece: the piece
    """
    score = 0
    state = "start"
    board = []
    height = 20
    width = 10
    x_position = 100
    y_position = 60
    size = 20
    piece = None
    
    #Gives the relative coordinates on the board of a square
    #of index 0 to 15 in a mini-grid for quick transformations
    block_to_coordinates = [
        [0,0],[0,1],[0,2],[0,3],
        [1,0],[1,1],[1,2],[1,3],
        [2,0],[2,1],[2,2],[2,3],
        [3,0],[3,1],[3,2],[3,3]
        ]

    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = []
        self.score = 0
        self.level = 1 #Game Level
        self.state = "start"
        self.rows_cleared = 0
        #self.y = None
        #self.x = None
        # Create a empty playing field
        self.board = [[0 for _ in range(self.width)]\
        for _ in range(self.width)]
        
#         for row in range(height):
#             new_line = []
#             for column in range(width):
#                 new_line.append(0)
#             self.board.append(new_line)
    
    def __repr__(self):
        print(f"score: {self.score},\n ")
        print(f"current squares on board:\n{self.field}")
        print(f"Current level is {self.state}")

    """
    Creates a new active piece
    """
    def new_piece(self):
        self.piece = Piece(0,0)
        #preallocate the set of global coordinates for the piece for speed.
        self.piece.global_coordinates = [[0,0] for _ in range(4)]

    def global_coordinates(self, rotation = None):
        """
        Gives the global coordinates of a piece's location
        based on its rotation and the reference frame coordinates.

        sets self.global_coordinates to a list of four lists, each containing
        the y and x coordinates (row and column number) of each block in the
        piece.
        """
        if rotation == None:
            rotation = self.piece.rotation
        ref_frame = [0 for _ in range(4)]
        for i in range(4):
            ref_frame[i] = self.piece.type[rotation][i]
            self.piece.global_coordinates[i] = self.block_to_coordinates\
                [ref_frame[i]]
            self.piece.global_coordinates[i][0] += self.piece.y
            self.piece.global_coordinates[i][1] += self.piece.x

    """
    Check if the falling piece is touching with a block that is
    already fixed on the field
    """
    def touch_left(self):
        self.global_coordinates()
        #y = self.piece.global_coordinates[i][0]
        #x = self.piece.global_coordinates[i][1]
        for i in range(4):
            if self.field[self.piece.global_coordinates[i][0]]\
                [self.piece.global_coordinates[i][1] - 1] != 0:
                return True
        return False

    def touch_right(self):
        self.global_coordinates()
        for i in range(4):
            if self.field[self.piece.global_coordinates[i][0]]\
                [self.piece.global_coordinates[i][1] + 1] != 0:
                return True
        return False

    def touch_top(self):
        self.global_coordinates()
        for i in range(4):
            if self.field[self.piece.global_coordinates[i][0] - 1]\
                [self.piece.global_coordinates[i][1]] != 0:
                return True
        return False

"""
Check if the rotated block would touch another block
"""

    def touch_rotate(self):
        self.global_coordinates(self.piece.rotation + 1)
        for i in range(4):
            if self.field[self.piece.global_coordinates[i][0]]\
                [self.piece.global_coordinates[i][1]] != 0:
                return True
        return False

    """
    Check for line completions and remove them, then add points
    """
    def break_line(self):
        new_rows = 0
        for i in range(len(self.field)):
            if 0 not in self.field[i]:
                new_rows_cleared += 1
                self.field = self.field[0:i] + self.field[i+1:]
                self.field.insert(0, [0 for _ in range(10)])
        self.score += self.row_score[new_rows + 1] * (self.state + 1)
        self.rows_cleared += new_rows
        if self.rows_cleared >= 10:
            self.state += 1
            self.rows_cleared = self.rows_cleared % 10

    """
    Lock the active piece in place by writing it to the board
    """
    def freeze(self):
        self.global_coordinates()
        for i in range(4):
            self.field[self.piece.global_coordinates[i][0]]\
                [self.piece.global_coordinates[i][1]] = self.piece.color

    """
    Move the block all the way down until it can't move anymore ('smash' move)
    """
    def smash(self):
        while not self.touch_top():
            self.go_down()

    """
    Move the block down by one space or freeze the block when it hits bottom
    """
    def go_down(self):
        if not self.touch_top:
            self.piece.y = self.piece.y + 1
        self.freeze()

    """
    Move the block sideways
    """
    def go_left(self):
        if not self.touch_left():
            self.piece.x = self.piece.x - 1


    def go_right(self):
        if not self.touch_right():
            self.piece.x = self.piece.x + 1

    """
    Rotate the block
    """
    def rotate(self):
        if not self.touch_rotate():
            if self.piece.rotation >= self.piece.max_rotation - 1:
                self.piece.rotation = 0
            else:
                self.piece.rotation += 1
