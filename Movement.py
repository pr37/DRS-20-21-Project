import enum

from PyQt5.QtCore import QBasicTimer, Qt


class MovementDirection(enum.Enum):
    Left = 1
    Right = 2
    Down = 3
    Up = 4


class Movement():
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40

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
        board.Movement.move_snake(board, snake)
        player.snakeMoved(snake)
        board.update()


    @staticmethod
    def move_snake(self, board, snage):
        if self.direction == 1:
            self.snake.current_x_head, self.snake.current_y_head = self.snake.current_x_head - 1, self.snake.current_y_head
            if self.snake.current_x_head < 0:
                self.snake.current_x_head = Movement.WIDTHINBLOCKS - 1
        if self.direction == 2:
            self.snake.current_x_head, self.current_y_head = self.snake.current_x_head + 1, self.snake.current_y_head
            if self.snake.current_x_head == Movement.WIDTHINBLOCKS:
                self.snake.current_x_head = 0
        if self.direction == 3:
            self.snake.current_x_head, self.snake.current_y_head = self.snake.current_x_head, self.snake.current_y_head + 1
            if self.snake.current_y_head == Movement.HEIGHTINBLOCKS:
                self.snake.current_y_head = 0
        if self.direction == 4:
            self.snake.current_x_head, self.snake.current_y_head = self.snake.current_x_head, self.snake.current_y_head - 1
            if self.snake.current_y_head < 0:
                self.snake.current_y_head = Movement.HEIGHTINBLOCKS

        head = [self.snake.current_x_head, self.snake.current_y_head]
        self.snake.snakePosition.insert(0, head)

        if not self.snake.growSnake:
            self.snake.snakePosition.pop()  # da zmija ne bude beskonacno dugacka

    #def timerEvent(self, event):
    #    if event.timerId() == self.timer.timerId():
            #self.move_snake()
            #self.update()