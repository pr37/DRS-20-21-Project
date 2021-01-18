from Service.Config import Config
from Game.GameObjects.Snake import Snake
#from Game.main import MainWindow#ja


class Player(Config):
    def __init__(self, board, name, numberOfSnakes, positions, directions):
        self.board = board
        self.Snakes = []
        self.Name = name
        for i in range(numberOfSnakes):
            self.Snakes.append(Snake(board, positions[i], directions[i]))

        self.turnSnake = self.Snakes[0]
        self.turnSnakeIndex = 0

    def endTurn(self):
        self.resetSnakeMovements()
        self.board.nextPlayerTurn()

    def snakeMoved(self, snake):
        if snake.move():
            self.nextSnake()

    def nextSnake(self):
        if len(self.Snakes) == 0:
            return
        index = (self.Snakes.index(self.turnSnake) + 1) % len(self.Snakes)
        self.turnSnake = self.Snakes[index]
        self.turnSnakeIndex = index

    def prevSnake(self):
        if len(self.Snakes) == 0:
            return
        index = self.Snakes.index(self.turnSnake) - 1
        if index < 0:
            index = len(self.Snakes) - abs(index)
        self.turnSnake = self.Snakes[index]
        self.turnSnakeIndex = index

    def resetSnakeMovements(self):
        for snake in self.Snakes:
            snake.resetMoves()

    def snakeDied(self, snake):
        if self.turnSnake == snake:
            self.nextSnake()
        snake.die()
        self.Snakes.remove(snake)
        if len(self.Snakes) == 0:
            self.board.playerLost(self)
