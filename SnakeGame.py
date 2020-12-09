from PyQt5.QtWidgets import QMainWindow


class SnakeGame(QMainWindow):
    def init(self):
        self.setStyleSheet("QWidget {background-image: url(grass.jpg)}")