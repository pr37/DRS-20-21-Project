from PyQt5.QtCore import QBasicTimer, Qt

class Movement():
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40

    @staticmethod
    def keyPressEvent(self, event):  # levo1 desno2 dole3 gore4
        key = event.key()
        if key == Qt.Key_Left:
            if self.direction != 2:  # ako je isao desno ne moze levo
                self.direction = 1
        elif key == Qt.Key_Right:
            if self.direction != 1:
                self.direction = 2
        elif key == Qt.Key_Down:
            if self.direction != 4:
                self.direction = 3
        elif key == Qt.Key_Up:
            if self.direction != 3:
                self.direction = 4
        self.Movement.move_snake(self)
        self.update()

    @staticmethod
    def move_snake(self):
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