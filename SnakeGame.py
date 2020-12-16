from PyQt5.QtWidgets import QMainWindow


class SnakeGame(QMainWindow):
    def init(self):
        super(SnakeGame, self).__init__()
        self.sboard = Board(self)

        self.setCentralWidget(self.sboard)
        self.setWindowTitle('DRS Snake Game')
        self.setStyleSheet("QWidget {background-image: url(background.jpg)}")
        self.resize(600, 400)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)

        self.sboard.start()
        self.show()