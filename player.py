import pygame

class player:
    #current position as an array (x, y)
    position = int[2]
    coins = int
    rulesUncovered = bool[5]
    #parse moving (diag)
    '''
    startingPoz = starting position as (x, y) int array
    '''
    def __init__(self, startingPoz):
        self.position = startingPoz
        self.coins = 0
        self.rulesUncovered = [False, False, False, False, False]

    #define move as numbers, 1 -> 8. 
    # 1 is diag left, goes clockwise around
    # allows us to define difference between corner move and diagonal
    # move is understood to be a single int/string or an array, loops over array
    def parseMove(self, moves):
        if type(moves) == str or int:
            moves = [moves]
        for move in moves:
            #diag UL
            if (move == pygame.K_1):
                self.position[1] = self.position[1] + 1
                self.position[0] = self.position[0] - 1               
            #up
            if (move == pygame.K_2):
                self.position[1] = self.position[1] + 1
            #diag UR
            if (move == pygame.K_3):
                self.position[1] = self.position[1] + 1
                self.position[0] = self.position[0] + 1
            #right
            if (move == pygame.K_4):
                self.position[0] = self.position[0] + 1
            #diag DR
            if (move == pygame.K_5):
                self.position[1] = self.position[1] - 1
                self.position[0] = self.position[0] + 1
            #down
            if (move == pygame.K_6):
                self.position[1] = self.position[1] - 1
            #diag DL
            if (move == pygame.K_7):
                self.position[1] = self.position[1] - 1
                self.position[0] = self.position[0] - 1            
            #left
            if (move == pygame.K_8):
                self.position[0] = self.position[0] - 1