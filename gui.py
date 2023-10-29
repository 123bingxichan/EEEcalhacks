import pygame
import tkinter as tk
from tkinter import ttk

def draw_board(screen, n):
    """Draws an n x n board """

    curr_x= SCREEN_WIDTH//n-1
    curr_y= SCREEN_HEIGHT//n-1
    for row in range(n-1):
        pygame.draw.line(screen, (0,0,0), (curr_x, 0), (curr_x, SCREEN_HEIGHT), 5)
        curr_x += SCREEN_WIDTH//n-1
    for col in range(n-1):
        pygame.draw.line(screen, (0,0,0), (0, curr_y), (SCREEN_WIDTH, curr_y), 5)
        curr_y+= SCREEN_HEIGHT//n-1

def draw_box(screen, n , k ):
    box_width = ((SCREEN_WIDTH-((n-1)*5))//n)-2*k
    box_height = ((SCREEN_HEIGHT-((n-1)*5))//n) - 2*k
    for row in range(k,SCREEN_WIDTH, box_width+2*k+5):
        for col in range(k,SCREEN_HEIGHT, box_height+2*k+5):
            pygame.draw.rect(screen, (100,200,200), pygame.Rect(row,col,box_width,box_height))

# Initialize Pygame
pygame.init()

# Initialize TKinter
root = tk.Tk()
root.title("Pygame with TKinter")

# Pygame screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# Create Pygame screen
pygame_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a TKinter label
label = ttk.Label(root, text="Pygame with TKinter")
label.pack()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Pygame display
    pygame_screen.fill((255, 255, 255))
    draw_board(pygame_screen,5)
    draw_box(pygame_screen, 5,20)
    pygame.display.flip()

    # Update TKinter window
    root.update()

# Quit Pygame and TKinter
pygame.quit()
root.destroy()

