import sys
from PyQt5.QtWidgets import QApplication
from SnakeGame import SnakeGame

if __name__ == '__main__':
    app = QApplication([])
    game = SnakeGame()
    sys.exit(app.exec_())
