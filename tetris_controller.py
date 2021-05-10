"""
Tetris Game User-Input Controller
"""
from abc import ABC, abstractmethod
import pygame

class TetrisController(ABC):
    """
    Abstract base class for the game controller.
    """
    def __init__(self, TetrisBoard):
        """
        Stores 'TicTacToeBoard' as a private instance attribute

        Arguments:
            - self: represents the instance of the class
            - TetrisBoard: the Tetris board

        Returns:
            TetrisBoard as a private instance attribute
        """
        self._board = TetrisBoard

    @property
    def board(self):
        """
        Gets the board from TetrisBoard

        Arguments:
            - self: represents the instance of the class

        Returns:
            the Tetris Board stored in the TetrisBoard instance
        """
        return self._board

    @abstractmethod
    def move(self):
        """
        Abstract Method to be implemented later
        for players to make moves on the Tetris board

        Arguments:
           - self: represents the instance of the class
        """

class Controller(TetrisController):
    """
    Implements the controls for the Tetris Game

    Arguments:
        TetrisController: the abstract base controller class of the Tetris Board
    """
    # pylint: disable=no-member
    def move(self):
        for event in pygame.event.get():
            # While the game is running
            if self.board.state == "start":
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.board.state = "quit"
                # Get User Input with Keyboard
                if event.type == pygame.KEYDOWN:
                    # If "Up" Key is Pressed
                    if event.key == pygame.K_UP:
                        # Rotate the piece
                        self.board.rotate()
                    # If "Down" Key is Pressed
                    if event.key == pygame.K_DOWN:
                        # Move the piece down by one space
                        self.board.go_down()
                    # If "Left" Key is Pressed
                    if event.key == pygame.K_LEFT:
                        # Move the piece to the left by one space
                        self.board.go_left()
                    # If "Right" Key is Pressed
                    if event.key == pygame.K_RIGHT:
                        # Move the piece to the right by one piece
                        self.board.go_right()
                    # If "Space" Key is Pressed
                    if event.key == pygame.K_SPACE:
                        # Move the piece all the way down
                        self.board.smash()
    #pylint: enable=no-member

    def end_actions(self):
    # pylint: disable=no-member
        """
        Options for game over and if the user closes the window
        """
        # Quit Game if User Closes the Window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                self.board.state = "quit"
            if event.type == pygame.KEYDOWN:
                # If the "Return" key is Pressed
                if event.key == pygame.K_RETURN:
                    # Start a new game
                    self.board.__init__()
                # If the "Q" key is Pressed
                if event.key == pygame.K_q:
                    pygame.quit()
                    self.board.state = "quit"
    #pylint: enable=no-member
    