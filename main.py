# Example file showing a basic pygame "game loop"
import pygame
from gui import gui

# pygame setup
pygame.init()
clock = pygame.time.Clock()
running = True
display = gui()

while running:
    # poll for events
    # pygame.QUIT event means the user python3 -m pip install pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RENDER YOUR GAME HERE
    display.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(500)  # limits FPS to 60

pygame.quit()