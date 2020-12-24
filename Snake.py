import random

class Snake():
    def __init__(self, board, position, direction):
        self.board = board
        self.snakePosition = position
        self.oldPosition = []
        self.current_x_head = self.snakePosition[0][0]
        self.current_y_head = self.snakePosition[0][1]
        self.updateBoardOfPosition()
        self.direction = direction
        self.moves = len(self.snakePosition)