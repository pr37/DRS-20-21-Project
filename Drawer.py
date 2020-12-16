from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QFrame

class Drawer(QFrame):
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40

    def __init__(self, snakePos):
        super(Drawer, self).__init__()
        self.snakePosition = snakePos

    @staticmethod
    def paintEvent(self, event):
        painter = QPainter(self)
        rect = self.contentsRect()  # povrsina izmedju margina widgeta
        boardtop = rect.bottom() - Drawer.HEIGHTINBLOCKS * self.square_height()

        for pos in self.snakePosition:  # stavi prva dva kvadrata zmije na board pocetna poz
            self.drawer.draw_square(painter, rect.left() + pos[0] * self.square_width(),
                             boardtop + pos[1] * self.square_height(), self.square_width(), self.square_height())

    def draw_square(self, painter, x, y, w, h):  # crta kockicu zmijice
        color = QColor(0x302213)
        painter.fillRect(x + 1, y + 1, w - 2,
                         h - 2, color)
