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

    #calculate number of moves for the snake and return a bool indicating the snake finished its turn
    def move(self):
        self.updateBoardOfPosition()
        self.moves -= 1
        if self.moves == 0:
            self.moves = len(self.snakePosition)
            return True
        return False

    def resetMoves(self):
        self.moves = len(self.snakePosition)

    def updateBoardOfPosition(self):
        self.board.snakeUpdate(self.snakePosition, self.oldPosition)


