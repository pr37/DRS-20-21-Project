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

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()  #povrsina izmedju margina widgeta
        boardtop = rect.bottom() - Board.HEIGHTINBLOCKS * self.square_height()

        for pos in self.snake.snakePosition:  #stavi prva dva kvadrata zmije na board pocetna poz
            self.draw_square(painter, rect.left() + pos[0] * self.square_width(),
                             boardtop + pos[1] * self.square_height())

    def draw_square(self, painter, x, y): #crta kockicu zmijice
        color = QColor(0x302213)
        painter.fillRect(x + 1, y + 1, self.square_width() - 2,
                        self.square_height() - 2, color)

    def keyPressEvent(self, event) -> None: self.Movement.keyPressEvent(self, event)

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.Movement.move_snake(self)
            self.update()
