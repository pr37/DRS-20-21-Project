import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt
from SnakeGame import SnakeGame
from multiprocessing import Process
from threading import Thread
from PyQt5.QtCore import QThread, QProcess

from welcome_scene import *
from about_scene import *



class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Snake Game"
        self.iconName = "snakeHead.png"
        self.widths = 602
        self.heights = 502
        self.rect().center()    # sta?
        self.setFixedWidth(self.widths)
        self.setFixedHeight(self.heights)

        self.welcomeScene = WelcomeScene(self, self.widths, self.heights)
        self.welcomeScene.newGameBtn.clicked.connect(self.NewGame)
        self.welcomeScene.aboutGameBtn.clicked.connect(self.AboutGame)
        self.welcomeScene.exitBtn.clicked.connect(self.ExitGame)
        self.aboutScene = None
        self.setScene(self.welcomeScene)

        self.show()

    def NewGame(self):
        self.close()

    def AboutGame(self):
        self.aboutScene = AboutSene(self, self.widths, self.heights)
        self.aboutScene.returnBtn.clicked.connect(self.ReturnToWelcome)
        self.setScene(self.aboutScene)


    def ExitGame(self):
        self.close()


    def ReturnToWelcome(self):
        self.setScene(self.welcomeScene)


if __name__ == '__main__':
    app = QApplication([])
    #game = SnakeGame()
    mw = MainWindow()
    sys.exit(app.exec_())
