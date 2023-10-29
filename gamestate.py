from player import Player
from board import Board
from rules import Rules

class Gamestate():
    def __init__(self, rows, cols):
        self.rules = Rules()
        self.player = Player([int(rows/2), int(cols/2)], self.rules)
        self.board = Board(rows, cols)

        self.win = False
        self.lose = False


    def move_player(self, player_input):
        #get current player position
        x = self.player.position[0]
        y = self.player.position[1]

        #move if valid
        if self.rules.isMoveValid(player_input):
            self.player.move(player_input)
        #if not valid, just don't move

        #get position after move
        x = self.player.position[0]
        y = self.player.position[1]

        #update player values
        self.player.coins += self.board.selectTile(x, y).money

        #check if player won/lose
        self.check_end_conditions(player_input)

    def check_end_conditions(self, player_input):
        self.win = self.rules.isMoveWin(player_input)
        self.lose = self.rules.isMoveLose(player_input)

    def render(self, player_input):
        self.move_player(player_input)