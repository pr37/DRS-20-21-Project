from Service.Config import Config
from Snake import Snake


class Player(Config):
    def __init__(self, board, name, numberOfSnakes, positions, directions):
        self.board = board
        self.Snakes = []
        self.Name = name
        for i in range(numberOfSnakes):
            self.Snakes.append(Snake(board, positions[i], directions[i]))

        self.turnSnake = self.Snakes[0]
        self.turnSnakeIndex = 0
        self.canEnd = False

    def endTurn(self):
        if not self.canEnd:
            return

        self.resetSnakeMovements()
        self.board.nextPlayerTurn()
        self.canEnd = False

    def snakeMoved(self, snake):
        if snake.move():
            self.nextSnake(snake)

    def nextSnake(self, snake):
        index = (self.Snakes.index(snake) + 1) % len(self.Snakes)
        if index == 0:
            self.canEnd = True
        self.turnSnake = self.Snakes[index]
        self.turnSnakeIndex = index

    def resetSnakeMovements(self):
        for snake in self.Snakes:
            snake.resetMoves()

    def snakeDied(self, snake):
        if self.turnSnake == snake:
            self.nextSnake(snake)
        snake.die()
        self.Snakes.remove(snake)