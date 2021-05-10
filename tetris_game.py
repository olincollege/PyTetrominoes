"""
Runs the main game.
"""
import pygame

from tetris_board import TetrisBoard
from tetris_piece import colors
from tetris_controller import Controller

# Initialize pygame
pygame.init() # pylint: disable=no-member

# Initialize the colors for the board
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)

# Set dimensions
WIDTH = 600
HEIGHT = 1000
size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("PyTetrominoes")

# Initialize and play the music continuously
lofi_tetris = pygame.mixer.music.load("music/tetris_music.wav")
pygame.mixer.music.play(-1)

# Loop until the user clicks the close button.
clock = pygame.time.Clock()
tetris_game = TetrisBoard()
controller = Controller(tetris_game)

def main():
    """
    Loops through the game commands until the game is quit
    """
    run = True
    while run and tetris_game.state != "quit":

        # Fills the screen with black
        screen.fill(BLACK)

        # If there are no falling pieces, create a new piece
        if tetris_game.piece is None:
            tetris_game.new_piece()

        # If the game state is "start", make the piece move down
        if tetris_game.state == "start":
            tetris_game.go_down()

        # User Controls
        controller.move()

        if tetris_game.state == "quit":
            pygame.quit() # pylint: disable=no-member
            return "quit"

        # Draws the blocks
        draw()

        # Display the score
        display_score()

        # Display the Game Over Screen when Triggered
        game_over()

        # Display changes
        pygame.display.flip()

        # End-of-game actions
        controller.end_actions()
        if tetris_game.state == "quit":
            return "quit"


def draw():
    """
    Draws the pieces on the board
    """
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
        for block_row in range(tetris_game.piece.size):
            for block_column in range(tetris_game.piece.size):
                # Check each individual block in the 4x4 square for the piece
                if block_row * tetris_game.piece.size + block_column in\
                    tetris_game.piece.piece_image():
                    pygame.draw.rect(
                        # in the playing screen
                        screen,
                        # draw the color of the piece
                        colors[tetris_game.piece.color],
                        # make the piece fall horizontally
                        [tetris_game.x + tetris_game.size * (block_column\
                            + tetris_game.piece.x_col) + 1,
                        # make the piece fall vertically
                        tetris_game.y + tetris_game.size * (block_row +\
                            tetris_game.piece.y_row) + 1,
                        # amplify the size of the piece
                        tetris_game.size - 2,
                        # amplify the size of the piece
                        tetris_game.size - 2]
                        )


    # Draws the Frozen Pieces
    for board_row in range(tetris_game.height):
        for board_column in range(tetris_game.width):
            if tetris_game.board[board_row][board_column] != -1:
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


def display_score():
    """
    Displays the current score
    """
    score_font = pygame.font.Font('fonts/pigment.otf', 72)
    score_text = score_font.render("Score: " + str(tetris_game.score), True, WHITE)
    screen.blit(score_text, [50, 50])


def game_over():
    """
    Display the game over screen
    """
    if tetris_game.state == "end":
        # Fill the screen with black so text can be seen more easily
        screen.fill(BLACK)
        # Render and display the game over text
        game_over_font = pygame.font.Font('fonts/pigment.otf', 100)
        game_over_text = game_over_font.render("Game Over!", True, colors[0])
        game_over_rect = game_over_text.get_rect(center = (WIDTH/2, HEIGHT/3))
        screen.blit(game_over_text, game_over_rect)
        # Render and display the first line to ask users to play again
        try_again_font = pygame.font.Font('fonts/pigment.otf', 60)
        try_again_text = try_again_font.render("Press ENTER to", True, colors[2])
        text_rect = try_again_text.get_rect(center=(WIDTH/2, 2*HEIGHT/3))
        screen.blit(try_again_text, text_rect)
        # Render the second line to ask users to play again
        try_again_text_1 = try_again_font.render("try again!", True, colors[2])
        text_rect_1 = try_again_text_1.get_rect(center=(WIDTH/2, 3*HEIGHT/4))
        screen.blit(try_again_text_1, text_rect_1)


if __name__ == "__main__":
    main()
