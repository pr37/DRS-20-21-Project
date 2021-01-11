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
from mode_scene import *



class MainWindow(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Snake Game"
        self.iconName = "snakeHead.png"
        self.widths = 602
        self.heights = 502
        self.rect().center()
        self.setFixedWidth(self.widths)
        self.setFixedHeight(self.heights)

        self.welcomeScene = WelcomeScene(self, self.widths, self.heights)
        self.welcomeScene.newGameBtn.clicked.connect(self.NewGame)
        self.welcomeScene.aboutGameBtn.clicked.connect(self.AboutGame)
        self.welcomeScene.exitBtn.clicked.connect(self.ExitGame)
        self.aboutScene = None
        self.modeScene = None
        self.setScene(self.welcomeScene)

        self.show()


    def NewGame(self):
        self.modeScene = ModeScene(self, self.widths, self.heights)
        self.modeScene.playButton.clicked.connect(self.PlayGame)

        self.modeScene.returnBtn.clicked.connect(self.ReturnToWelcome)
        self.setScene(self.modeScene)


    def AboutGame(self):
        self.aboutScene = AboutScene(self, self.widths, self.heights)
        self.aboutScene.returnBtn.clicked.connect(self.ReturnToWelcome)
        self.setScene(self.aboutScene)


    def ExitGame(self):
        self.close()


    def ReturnToWelcome(self):
        self.setScene(self.welcomeScene)


    def PlayGame(self):
        numOfPlayers = self.modeScene.playerComboBox.currentText()
        print("broj igraca: ", numOfPlayers)
        game = SnakeGame()
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    #game = SnakeGame()
    mw = MainWindow()
    sys.exit(app.exec_())
