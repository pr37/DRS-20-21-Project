

class Food:
    def __init__(self, board, position):
        self.oldPosition = []
        self.position = [position]
        self.board = board
        self.updateBoard()

    def move(self):
        self.updateBoard()
        #TODO move food to a valid slot moving  1-3 tiles in a random direction

    def updateBoard(self):
        self.board.foodUpdate(self.position, self.oldPosition)
