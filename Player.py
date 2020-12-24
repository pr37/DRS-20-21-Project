from Config import Config

class Player(Config):
    def __init__(self, board, name, numberOfSnakes, positions, directions):
        self.board = board
        self.Snakes = []
        self.Name = name
        for i in range(numberOfSnakes):
            self.Snakes.append(Snake(board, positions[i], directions[i]))

        self.turnSnake = self.Snakes[0]
        self.canEnd = False