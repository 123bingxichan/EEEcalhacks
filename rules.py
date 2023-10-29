import pygame
import random

#each "rule" is a valid move along the board
#there are proportionally more valid 2-space moves than 3, etc.
class Rules:
    givenRules = [[pygame.K_2], [pygame.K_4], [pygame.K_6], [pygame.K_8]]
    winCondition = []
    loseCondition = []
    numExtraRules = 10
    extraRules = []
    #legal moves = all moves above combined.
    #each legal move is one array of moves in order, e.g. 
    #in given rules, pygame.K_2 is valid, but
    #pygame.K_2, pygame.K_4 is not.
    legalMoves = givenRules
    
    def __init__(self):
        self.winCondition = Rules.genRule(3, 6)
        self.loseCondition = Rules.genRule(2, 6)
        #below WILL NOT WORK d/t probs with combining 2D arrays
        self.extraRules = self.givenRules + self.winCondition + self.loseCondition

    '''
    Parameters:
    minimum rule length, max rule length,
    Produces a series of moves in logic (PyGame K.1, K.2, etc)
    To translate to english, use parseKeyToEnglish
    '''
    def genRule(min, max):
        length = random(min, max + 1)
        rule = []
        for l in range(0, length):
            rule.append(exec(f'pygame.K_{random(1, 9)}'))
        return rule
        