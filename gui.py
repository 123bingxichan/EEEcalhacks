import pygame
from gamestate import Gamestate
class gui():

    ROWS = 5
    COLS = 5

    def __init__(self, width=1280, height=720):
        self.width = width;
        self.height = height;
        self.screen = pygame.display.set_mode((width, height))

        self.player_input = []
        self.gamestate = Gamestate(gui.ROWS, gui.COLS)

    def draw_board(self, n):
        """Draws an n x n board """

        curr_x= self.width//n-1
        curr_y= self.height//n-1
        for row in range(n-1):
            pygame.draw.line(self.screen, (0,0,0), (curr_x, 0), (curr_x, self.height), 5)
            curr_x += self.width//n-1
        for col in range(n-1):
            pygame.draw.line(self.screen, (0,0,0), (0, curr_y), (self.width, curr_y), 5)
            curr_y += self.height//n-1

    def draw_box(self, n , k ):

        box_width = ((self.width-((n-1)*5))//n)-2*k
        box_height = ((self.height-((n-1)*5))//n) - 2*k
        for row in range(k,self.width, box_width+2*k+5):
            for col in range(k,self.height, box_height+2*k+5):
                pygame.draw.rect(self.screen, (100,200,200), pygame.Rect(row,col,box_width,box_height))

    def get_keyboard_input(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_1]):
            self.player_input.append(pygame.K_1)
        if (keys[pygame.K_2]):
            self.player_input.append(pygame.K_2)
        if (keys[pygame.K_3]):
            self.player_input.append(pygame.K_3)
        if (keys[pygame.K_4]):
            self.player_input.append(pygame.K_4)
        if (keys[pygame.K_5]):
            self.player_input.append(pygame.K_5)
        if (keys[pygame.K_6]):
            self.player_input.append(pygame.K_6)
        if (keys[pygame.K_7]):
            self.player_input.append(pygame.K_7)
        if (keys[pygame.K_8]):
            self.player_input.append(pygame.K_8)

        if(len(self.player_input) > len(self.gamestate.rules.winCondition)):
            self.player_input.pop(0)

    def update(self):
        # Update Pygame display
        self.screen.fill((255, 255, 255))
        self.draw_board(5)
        self.draw_box(5, 20)

        self.get_keyboard_input()

        self.gamestate.render(self.player_input)




