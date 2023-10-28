# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user python3 -m pip install pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RENDER YOUR GAME HERE
    screen.fill("black")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()