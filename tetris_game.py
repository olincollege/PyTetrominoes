'''
Import statements
'''
import pygame
from tetris_board import TetrisBoard

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
game = TetrisBoard(20, 10) # NOTE: Need to finish initializing
pressing_down = False

def main():
    pressing_down = False

    run = True
    while run:
        # If game state is start, start pulling blocks down

        # Initialize controls here

        # Place controls in here
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Make blocks here
        screen.fill(WHITE)

        # Make the screen here

        # Create the blocks within the square

        # Display game over here when finishing looping through everything

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
