"""
Tetris Game User-Input Controller
"""
import pygame

from abc import ABC, abstractmethod

# Up key: rotate
    # Down key: move block down slightly quicker
    # Left key: go to the side left
    # Right key: go to the side right
    # Space key: go all the way down

class TetrisController(ABC):
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
        pass

class Controller(TetrisController):
    def move(self):
        pass
