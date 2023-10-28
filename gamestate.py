class Gamestate():

    def __init__(self, rows, cols):
        self.player = Player(rows/2, cols/2)
        self.board = Board(rows, cols)

    def render(self, player_input):
        self.player.move(player_input)

        #get current player position
        x = self.player.position[0]
        y = self.player.position[1]

        #set player is false at current board
        self.board.getPosition(x,y).player = False

        self.player.move(self.player_input)

        #get position after move
        x = self.player.position[0]
        y = self.player.position[1]

        #update player values
        self.player.money += self.board.getPosition(x, y).get("money")
        #set player is false at current board
        self.board.getPosition(x,y).player = True