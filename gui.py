import pygame
import tkinter as tk
from tkinter import ttk

def draw_board(screen, n):
    """Draws an n x n board """

    w = screen.get_rect()[2]
    h = screen.get_rect()[3]

    curr_x= w//n-1
    curr_y= h//n-1
    for row in range(n-1):
        pygame.draw.line(screen, (0,0,0), (curr_x, 0), (curr_x, h), 5)
        curr_x += w//n-1
    for col in range(n-1):
        pygame.draw.line(screen, (0,0,0), (0, curr_y), (w, curr_y), 5)
        curr_y+= h//n-1

def draw_box(screen, n , k ):

    w = screen.get_rect()[2]
    h = screen.get_rect()[3]

    box_width = ((w-((n-1)*5))//n)-2*k
    box_height = ((h-((n-1)*5))//n) - 2*k
    for row in range(k,w, box_width+2*k+5):
        for col in range(k,h, box_height+2*k+5):
            pygame.draw.rect(screen, (100,200,200), pygame.Rect(row,col,box_width,box_height))

def render(screen):
    # Update Pygame display
    screen.fill((255, 255, 255))
    draw_board(screen, 5)
    draw_box(screen, 5, 20)
