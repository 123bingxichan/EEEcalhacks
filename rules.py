import pygame
import random

#each "rule" is a valid move along the board
#there are proportionally more valid 2-space moves than 3, etc.
class Rules:
    intsToRules = {
        1: pygame.K_1,
        2: pygame.K_2,
        3: pygame.K_3,
        4: pygame.K_4,
        5: pygame.K_5,
        6: pygame.K_6,
        7: pygame.K_7,
        8: pygame.K_8
    }

    givenRules = [[pygame.K_2], [pygame.K_4], [pygame.K_6], [pygame.K_8]]
    winCondition = []
    loseCondition = []
    numTwoMoveRules = 5
    numAddtlRules = 5
    extraRules = []
    #legal moves = all moves above combined.
    #each legal move is one array of moves in order, e.g. 
    #in given rules, pygame.K_2 is valid, but
    #pygame.K_2, pygame.K_4 is not.
    legalMoves = []

    isRuleUncovered = []
    
    def __init__(self):
        self.winCondition = Rules.genRule(3, 6)
        self.loseCondition = Rules.genRule(2, 6)
        #below WILL NOT WORK d/t probs with combining 2D arrays
        for i in range(0, self.numTwoMoveRules):
            self.extraRules.append(Rules.genRule(2,2))
        for i in range(0, self.numAddtlRules):
            self.extraRules.append(Rules.genRule(2, 6))
        self.legalMoves = self.extraRules + self.givenRules + self.winCondition + self.loseCondition
        self.isRuleUncovered = [True if x == 0 else False for x in range(0, len(self.legalMoves))]

    '''
    Parameters:
    minimum rule length, max rule length,
    Produces a series of moves in logic (PyGame K.1, K.2, etc)
    To translate to english, use parseKeyToEnglish
    '''
    def genRule(self, min, max):
        length = random(min, max + 1)
        rule = []
        for l in range(0, length):
            rand = random(1, 9)
            rule.append(self.intsToRules.get(rand))
        return rule
    
    def isMoveValid(self, move):
        for r in self.legalMoves:
            if len(r) != len(move):
                return False
            for i in range(0, len(move)):
                if r[i] != move[i]:
                    return False
        return True
    
    def isMoveWin(self, move):
        return True if (move == self.winCondition[0]) else False
    
    def isMoveLose(self, move):
        return True if (move == self.loseCondition[0]) else False

    def uncoverRule(self):
        rand = random(0, len(self.uncoverRule))
        if (self.uncoverRule[rand] == False):
            self.uncoverRule[rand] = True
        else:
            self.uncoverRule()