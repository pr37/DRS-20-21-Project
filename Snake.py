import random

class Snake():
    def __init__(self):
        self.growSnake = False
        self.snakePosition = [[5, 10], [5, 11], [5, 12]]
        self.current_x_head = self.snakePosition[0][0]
        self.current_y_head = self.snakePosition[0][1]