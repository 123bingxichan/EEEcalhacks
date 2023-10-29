#create the board
import random

class Tile:
    # The Tile class contains a random amount of money (an integer from zero to ten)
    def __init__(self, money=random.choice(range(10))):
        self.money = money

    def addMoney(self, amount):
        # addMoney is a method that takes in an integer value to modify the amount of money in a tile
        self.money += amount
    def money(self):
        return f"Money: {self.money}"
    


class Board:
    # The Board class is a row x cols 2D array, containing Tile objects
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.dimensions = rows * cols
        self.tiles = [[Tile() for _ in range(cols)]]*rows

    def selectTile(self, x, y):
        # selectTile takes in integers for an x coordinate and a y coordinate to single out a particular tile
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.tiles[x][y]

    def getMoney(self, x, y):
        # getMoney takes in integers for an x coordinate and a y coordinate to get the amount of money on a given tile
        if 0 <= x < self.rows and 0 <= y < self.cols:
            return self.tiles[x][y].money
    

# Example usage:

# Create a 5 x 5 board
board = Board(5,5)
print(board.tiles)

# Select a tile
selectedTile = board.selectTile(2,2)
print(selectedTile)
print(selectedTile.money)

# Add some money to that tile
selectedTile.addMoney(10)

# Check if there is money on that tile 
money_on_center_tile = board.getMoney(2,2)
print(f"Money on center tile: {money_on_center_tile}")

