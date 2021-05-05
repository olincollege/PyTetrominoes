'''
Import statements
'''
import pygame, time

from tetris_board import TetrisBoard
from tetris_piece import Piece, colors

# Initialize pygame
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set dimensions
WIDTH = 400
HEIGHT = 500
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyTetrominoes")

# Loop until the user clicks the close button.
clock = pygame.time.Clock()
tetris_game = TetrisBoard(20, 10)

def main():
    pressing_down = False

    run = True
    while run:
        if tetris_game.piece is None:
            tetris_game.new_piece()
        
        if tetris_game.state == "start":
            tetris_game.go_down()
        else:
            time.sleep(1)
            break
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    tetris_game.rotate()
                if event.key == pygame.K_DOWN:
                    tetris_game.go_down()
                if event.key == pygame.K_LEFT:
                    tetris_game.go_left()
                if event.key == pygame.K_RIGHT:
                    tetris_game.go_right()
                if event.key == pygame.K_SPACE:
                    tetris_game.smash()

        # Fills the screen with black
        screen.fill(BLACK)

        # Draws the blocks
        draw()
        
        # Display changes
        pygame.display.flip()

    # Quit the game when loop is completed
    pygame.quit()

def draw():
    # Draws the Screen
    for screen_row in range(tetris_game.height):
            for screen_column in range(tetris_game.width):
                pygame.draw.rect(
                    # in the playing screen
                    screen,
                    # make the playing board white
                    WHITE,
                    # build 20 rows
                    [tetris_game.x + tetris_game.size * screen_column,
                    # build 10 columns
                    tetris_game.y + tetris_game.size * screen_row,
                    # amplify the size of the columns
                    tetris_game.size,
                    # amplify the size of the rows
                    tetris_game.size],
                    # border radius
                    2)
    
    # Draws the falling pieces
    if tetris_game.piece:
        # For each 4x4 block space piece
        for block_row in range(4):
            for block_column in range(4):
                # Check each individual block in the 4x4 square for the piece
                if block_row * 4 + block_column in tetris_game.piece.piece_image():
                    pygame.draw.rect(
                        # in the playing screen
                        screen,
                        # draw the color of the piece
                        colors[tetris_game.piece.color],
                        # make the piece fall horizontally
                        [tetris_game.x + tetris_game.size * (block_column + tetris_game.piece.x) + 1,
                        # make the piece fall vertically
                        tetris_game.y + tetris_game.size * (block_row + tetris_game.piece.y) + 1,
                        # amplify the size of the piece
                        tetris_game.size - 2,
                        # amplify the size of the piece
                        tetris_game.size - 2]
                        )

    # Draws the Frozen Pieces
    for board_row in range(tetris_game.height):
            for board_column in range(tetris_game.width):
                if tetris_game.board[board_row][board_column]:
                    pygame.draw.rect(
                        # in the playing screen
                        screen, 
                        # get the current pieces on the board in the instance
                        colors[tetris_game.board[board_row][board_column]],
                        # draw the piece in the board squares
                        [(tetris_game.x) + (tetris_game.size * board_column + 1),
                        (tetris_game.y) + (tetris_game.size * board_row + 1),
                        # amplify the size of the piece
                        tetris_game.size - 2,
                        # amplify the size of the piece
                        tetris_game.size - 1]
                        )

if __name__ == "__main__":
    main()
