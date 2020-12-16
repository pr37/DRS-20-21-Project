from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QFrame


class Drawer(QFrame):
    def __init__(self, height, widht):
        self.height = height
        self.widht = widht

    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()  # povrsina izmedju margina widgeta
        boardtop = rect.bottom() - self.height * self.square_height()

        for pos in self.snake.snakePosition:  # stavi prva dva kvadrata zmije na board pocetna poz
            self.draw_square(painter, rect.left() + pos[0] * self.square_width(),
                             boardtop + pos[1] * self.square_height())

    def draw_square(self, painter, x, y):  # crta kockicu zmijice
        color = QColor(0x302213)
        painter.fillRect(x + 1, y + 1, self.square_width() - 2,
                         self.square_height() - 2, color)

    def square_width(self):
        return self.contentsRect().width() / self.widht

    def square_height(self):
        return self.contentsRect().height() / self.height
