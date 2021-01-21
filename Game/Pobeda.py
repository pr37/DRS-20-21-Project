import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView
from PyQt5 import QtGui
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt
from multiprocessing import Process
from threading import Thread
from PyQt5.QtCore import QThread, QProcess

from welcome_scene import *
from about_scene import *
from mode_scene import *
from win_scene import *

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
        #self.welcomeScene.exitBtn.clicked.connect(self.ExitGame)
        self.winScene = WinScene(self,self.widths,self.heights,"")
        self.winScene.exitBtn.clicked.connect(self.ExitGame)
        #self.welcomeScene.winBtn.clicked.connect(self.WinGame)#ja
        self.aboutScene = None
        self.modeScene = None
        self.winScene = None#ja
        self.game = None
        #self.setScene(self.welcomeScene)
        #self.setScene(self.winScene)

        #self.show()


    def NewGame(self):
        self.modeScene = ModeScene(self, self.widths, self.heights)
        self.modeScene.playButton.clicked.connect(self.PlayGame)
        self.modeScene.returnBtn.clicked.connect(self.ReturnToWelcome)
        self.setScene(self.modeScene)


    def AboutGame(self):
        self.aboutScene = AboutScene(self, self.widths, self.heights)
        self.aboutScene.returnBtn.clicked.connect(self.ReturnToWelcome)
        self.setScene(self.aboutScene)

    #ja o
    def WinGame(self, txt):
        self.winScene = WinScene(self, self.widths, self.heights, txt)
        self.winScene.exitBtn.clicked.connect(self.ExitGame)
        self.setScene(self.winScene)
        self.show()
    #ja d

    def ExitGame(self):
        self.close()


    def ReturnToWelcome(self):
        self.setScene(self.welcomeScene)