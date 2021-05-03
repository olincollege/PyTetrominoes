'''
Import statements
'''
import pygame
from tetris_board import TetrisBoard
from tetris_piece import Piece, colors

# Initialize pygame
pygame.init()

# Initialize colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set dimensions
WIDTH = 400
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyTetrominoes")

# Loop until user clicks the close button
clock = pygame.time.Clock()
tetris_game = TetrisBoard(20, 10)
pressing_down = False

def main():
    pressing_down = False

    run = True
    while run:
        # If game state is start, start pulling blocks down
        if tetris_game.piece is None:
            tetris_game.new_piece()

        if tetris_game.state == "start":
            tetris_game.go_down()

        # Place controls in here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Make blocks here
        screen.fill(BLACK)

        # Create a 10 x 20 base grid for Tetris
        for row in range(tetris_game.height):
            for column in range(tetris_game.width):
                pygame.draw.rect(screen, GRAY, [tetris_game.x + tetris_game.zoom * column, tetris_game.y + tetris_game.zoom * row, \
                    tetris_game.zoom, tetris_game.zoom], 1)
                if tetris_game.board[row][column] > 0:
                    pygame.draw.rect(screen, colors[tetris_game.piece[row][column]],
                                    [tetris_game.x + tetris_game.zoom * column + 1, tetris_game.y + tetris_game.zoom * row + 1, tetris_game.zoom - 2, tetris_game.zoom - 1])

        # Create the blocks within the square

        # Display game over here when finishing looping through everything

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
