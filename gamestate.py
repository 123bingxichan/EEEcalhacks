from player import Player
from board import Board
from rules import Rules

class Gamestate():
    def __init__(self, rows, cols):
        self.player = Player([rows/2, cols/2])
        self.board = Board(rows, cols)
        self.rules = Rules()

        self.win = False
        self.lose = False


    def move_player(self, player_input):
        #get current player position
        x = self.player.position[0]
        y = self.player.position[1]

        self.player.move(player_input)

        #get position after move
        x = self.player.position[0]
        y = self.player.position[1]

        #update player values
        self.player.money += self.board.getPosition(x, y).get("money")

    def check_end_conditions():
        self.win = False
        self.lose = False

    def render(self, player_input):
        self.move_player(player_input)
        self.check_end_conditions()