from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QFrame
from Movement import Movement
from Snake import Snake

class Board(QFrame):
    SPEED = 150
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40

    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.timer = QBasicTimer()
        self.snake = Snake()
        self.board = []
        self.direction = 1
        self.setFocusPolicy(Qt.StrongFocus)
        self.Movement = Movement()

    def start(self):
        self.timer.start(Board.SPEED, self) #na 150 msec radi tajmer

    def square_width(self):
        return self.contentsRect().width() / Board.WIDTHINBLOCKS

    def square_height(self):
        return self.contentsRect().height() / Board.HEIGHTINBLOCKS


    def keyPressEvent(self, event) -> None: self.Movement.keyPressEvent(self, event)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.Movement.move_snake(self)
            self.update()
