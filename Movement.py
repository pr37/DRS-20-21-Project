import enum

from PyQt5.QtCore import QBasicTimer, Qt

from GridElement import GridElementType


class MovementDirection(enum.Enum):
    Left = 1
    Right = 2
    Down = 3
    Up = 4


def checkCollision(board, x, y) -> GridElementType:
    return board.Grid[x][y]


class Movement:

    @staticmethod
    def keyPressEvent(board, event):  # levo1 desno2 dole3 gore4
        player = board.turnPlayer

        if player.canEnd:
            return

        snake = player.turnSnake
        key = event.key()
        if key == Qt.Key_Left:
            if snake.direction == MovementDirection.Right:  # ako je isao desno ne moze levo
                return
            else:
                snake.direction = MovementDirection.Left
        elif key == Qt.Key_Right:
            if snake.direction == MovementDirection.Left:
                return
            else:
                snake.direction = MovementDirection.Right
        elif key == Qt.Key_Down:
            if snake.direction == MovementDirection.Up:
                return
            else:
                snake.direction = MovementDirection.Down
        elif key == Qt.Key_Up:
            if snake.direction == MovementDirection.Down:
                return
            else:
                snake.direction = MovementDirection.Up
        else: #bad key
            return
        board.Movement.move_snake(board, snake)
        player.snakeMoved(snake)
        board.update()

    @staticmethod
    def move_food(board, food, direction, steps):
        position = food.position
        for i in range(steps):
            position = Movement.calculateNewPos(board.WIDTHINBLOCKS, board.HEIGHTINBLOCKS, position, direction)
            if checkCollision(board, position[0][0], position[0][1]) != GridElementType.Empty:
                break
        food.position = position

    @staticmethod
    def calculateNewPos(width, height, position, direction):
        if direction == MovementDirection.Left:
            x = position[0][0] - 1
            if x < 0:
                x = width - 1 - abs(x)
            return [[x, position[0][1]]]
        elif direction == MovementDirection.Right:
            x = (position[0][0] + 1) % width
            return [[x, position[0][1]]]
        elif direction == MovementDirection.Down:
            y = (position[0][1] + 1) % height
            return [[position[0][0], y]]
        else:  # Up
            y = position[0][1] - 1
            if y < 0:
                y = height - 1 - abs(y)
            return [[position[0][0], y]]

    @staticmethod
    def move_snake(board, snake):
        snakePickedFood = False
        newPos = Movement.calculateNewPos(board.WIDTHINBLOCKS, board.HEIGHTINBLOCKS,
                                          [[snake.current_x_head, snake.current_y_head]], snake.direction)
        newPosX, newPosY = newPos[0][0], newPos[0][1]
        if checkCollision(board, newPosX, newPosY) == GridElementType.Empty or \
                checkCollision(board, newPosX, newPosY) == GridElementType.Food:
            snake.current_x_head, snake.current_y_head = newPosX, newPosY
            snakePickedFood = checkCollision(board, newPosX, newPosY) == GridElementType.Food
            if snakePickedFood:
                board.foodUpdate([], [newPosX, newPosY])

            head = [snake.current_x_head, snake.current_y_head]
            snake.snakePosition.insert(0, head)

        if not snakePickedFood:
            snake.oldPosition = snake.snakePosition.pop()
        else:
            snake.moves += 1

    #
    # @staticmethod
    # def move_snake(board, snake):
    #     snakePickedFood = False
    #     if snake.direction == MovementDirection.Left:
    #         newPosX, newPosY = snake.current_x_head - 1, snake.current_y_head
    #         if checkCollision(board, newPosX, newPosY) == GridElementType.Empty or \
    #                 checkCollision(board, newPosX, newPosY) == GridElementType.Food:
    #             snake.current_x_head, snake.current_y_head = newPosX, newPosY
    #             if snake.current_x_head < 0:
    #                 snake.current_x_head = Movement.WIDTHINBLOCKS - 1
    #             snakePickedFood = checkCollision(board, newPosX, newPosY) == GridElementType.Food
    #             if snakePickedFood:
    #                 board.foodUpdate([], [newPosX, newPosY])
    #
    #     if snake.direction == MovementDirection.Right:
    #         newPosX, newPosY = snake.current_x_head + 1, snake.current_y_head
    #         if checkCollision(board, newPosX, newPosY) == GridElementType.Empty or \
    #                 checkCollision(board, newPosX, newPosY) == GridElementType.Food:
    #             snake.current_x_head, snake.current_y_head = newPosX, newPosY
    #             if snake.current_x_head == Movement.WIDTHINBLOCKS:
    #                 snake.current_x_head = 0
    #             snakePickedFood = checkCollision(board, newPosX, newPosY) == GridElementType.Food
    #             if snakePickedFood:
    #                 board.foodUpdate([], [newPosX, newPosY])
    #
    #     if snake.direction == MovementDirection.Down:
    #         newPosX, newPosY = snake.current_x_head, snake.current_y_head + 1
    #         if checkCollision(board, newPosX, newPosY) == GridElementType.Empty or \
    #                 checkCollision(board, newPosX, newPosY) == GridElementType.Food:
    #             snake.current_x_head, snake.current_y_head = newPosX, newPosY
    #             if snake.current_y_head == Movement.HEIGHTINBLOCKS:
    #                 snake.current_y_head = 0
    #             snakePickedFood = checkCollision(board, newPosX, newPosY) == GridElementType.Food
    #             if snakePickedFood:
    #                 board.foodUpdate([], [newPosX, newPosY])
    #
    #     if snake.direction == MovementDirection.Up:
    #         newPosX, newPosY = snake.current_x_head, snake.current_y_head - 1
    #         if checkCollision(board, newPosX, newPosY) == GridElementType.Empty or \
    #                 checkCollision(board, newPosX, newPosY) == GridElementType.Food:
    #             snake.current_x_head, snake.current_y_head = newPosX, newPosY
    #             if snake.current_y_head < 0:
    #                 snake.current_y_head = Movement.HEIGHTINBLOCKS
    #             snakePickedFood = checkCollision(board, newPosX, newPosY) == GridElementType.Food
    #             if snakePickedFood:
    #                 board.foodUpdate([], [newPosX, newPosY])
    #
    #     head = [snake.current_x_head, snake.current_y_head]
    #     snake.snakePosition.insert(0, head)
    #
    #     if not snakePickedFood:
    #         snake.oldPosition = snake.snakePosition.pop()
    #     else:
    #         snake.moves += 1

    # def timerEvent(self, event):
    #    if event.timerId() == self.timer.timerId():
    # self.move_snake()
    # self.update()
