'''
Import statements
'''
import pygame

# Initialize pygame
pygame.init()

# Set dimensions
WIDTH, HEIGHT = 800,700
game_window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PyTetrominoes")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    pygame.quit()

if __name__ == "__main__":
    main()
