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

        # Draw the objects onto the board
        for row in range(tetris_game.height):
            for column in range(tetris_game.width):
                # Draw the 10 x 20 board
                pygame.draw.rect(
                    # Within the black screen
                    screen, 
                    # Make the 10 x 20 field white
                    WHITE,
                    # Make 10 columns
                    [tetris_game.x + tetris_game.size * column,
                    # Make 20 rows
                    tetris_game.y + tetris_game.size * row,
                    # Amplify the columns by the game size
                    tetris_game.size,
                    # Amplify the rows by the game size
                    tetris_game.size],
                    # Border radius
                    1)

        # Draw the piece onto the board
        if tetris_game.piece is not None:
            # For the width of the 4x4 space
            for box_row in range(4):
                # For the height of the 4x4 space
                for box_column in range(4):
                    # Get the piece
                    colored_piece = box_row * 4 + box_column
                    # If the piece is the same as the image of the piece (always True)
                    if colored_piece in tetris_game.piece.piece_image():
                        pygame.draw.rect(
                        # Within the black screen
                        screen,
                        # With the colors of the game piece
                        colors[tetris_game.piece.color],
                        # x position of the piece
                        [tetris_game.x + tetris_game.size * (box_column + tetris_game.piece.x) + 1,
                        # y position of the piece
                        tetris_game.y + tetris_game.size * (box_row + tetris_game.piece.y) + 1,
                        # Amplify the vertical size by the size of the board
                        tetris_game.size-2,
                        # Amplify the horizontal size of the block by the size of the board
                        tetris_game.size-2])

        # Display game over here when finishing looping through everything

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
