import random

from GridElement import GridElementType
from Movement import MovementDirection


def getLeftDirection(direction):
    if direction == MovementDirection.Up:
        return MovementDirection.Left
    elif direction == MovementDirection.Right:
        return MovementDirection.Up
    elif direction == MovementDirection.Down:
        return MovementDirection.Right
    else:  # left
        return MovementDirection.Down


def getRightDirection(direction):
    if direction == MovementDirection.Up:
        return MovementDirection.Right
    elif direction == MovementDirection.Right:
        return MovementDirection.Down
    elif direction == MovementDirection.Down:
        return MovementDirection.Left
    else:  # left
        return MovementDirection.Up


class Snake:
    def __init__(self, board, position, direction):
        self.board = board
        self.snakePosition = position
        self.oldPosition = []
        self.current_x_head = self.snakePosition[0][0]
        self.current_y_head = self.snakePosition[0][1]
        self.updateBoardOfPosition()
        self.direction = direction
        self.moves = len(self.snakePosition)

    # calculate number of moves for the snake and return a bool indicating the snake finished its turn
    def move(self):
        self.updateBoardOfPosition()
        self.moves -= 1
        if self.moves == 0:
            self.moves = len(self.snakePosition)
            return True
        return False

    def resetMoves(self):
        self.moves = len(self.snakePosition)

    def die(self):
        self.oldPosition = self.snakePosition
        self.snakePosition = []
        self.updateBoardOfPosition()

    def updateBoardOfPosition(self):
        self.board.snakeUpdate(self.snakePosition, self.oldPosition)

    def checkCapture(self):
        headPos = [[self.current_x_head, self.current_y_head]]
        frontPos = self.board.Movement.calculateNewPos(self.board.WIDTHINBLOCKS, self.board.HEIGHTINBLOCKS,
                                                       headPos, self.direction)

        if self.board.Movement.checkCollision(self.board, frontPos[0][0],
                                              frontPos[0][1]) != GridElementType.SnakePart:
            return False

        leftPos = self.board.Movement.calculateNewPos(self.board.WIDTHINBLOCKS, self.board.HEIGHTINBLOCKS,
                                                      headPos, getLeftDirection(self.direction))

        if self.board.Movement.checkCollision(self.board, leftPos[0][0],
                                              leftPos[0][1]) != GridElementType.SnakePart:
            return False

        rightPos = self.board.Movement.calculateNewPos(self.board.WIDTHINBLOCKS, self.board.HEIGHTINBLOCKS,
                                                       headPos, getRightDirection(self.direction))

        if self.board.Movement.checkCollision(self.board, rightPos[0][0],
                                              rightPos[0][1]) != GridElementType.SnakePart:
            return False

        # ako je stigao do ovde zmija je zarobljena
        print("Zmija je zarobljena")
        return True
