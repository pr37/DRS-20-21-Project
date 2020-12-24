import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from SnakeGame import SnakeGame
from PyQt5.QtCore import QSize, QDir, Qt
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel



class MainWindow(QGraphicsView):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.width = 602
        self.height = 502
        self.setWindowTitle('DRS Snake Game Main Window')
        self.iconName = "snakeHead.png"
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setFixedWidth(self.width)
        self.setFixedHeight(self.height)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(round((screen.width() - size.width()) / 2), round((screen.height() - size.height()) / 2))
        self.InitUI()

        vbox = QHBoxLayout()
        vbox.addWidget(self.groupBox)

        self.setLayout(vbox)

        self.show()


    def InitUI(self):
        self.groupBox = QGroupBox("Snek")
        self.gridLayout = QGridLayout()

        self.labelT = QLabel("Choose", self)
        self.gridLayout.addWidget(self.labelT, 0, 1)
        self.labelT.setMaximumHeight(40)
        self.labelT.setMaximumWidth(200)
        self.labelT.setAlignment(QtCore.Qt.AlignCenter)
        #self.labelT.setStyleSheet("background")

        self.buttonNewGame = QPushButton("New Game", self)
        self.buttonNewGame.setIcon(QtGui.QIcon("snakeHead.png"))
        self.buttonNewGame.setIconSize(QtCore.QSize(40, 40))
        self.buttonNewGame.setMinimumHeight(40)
        self.buttonNewGame.setMaximumWidth(200)
        self.gridLayout.addWidget(self.buttonNewGame, 1, 1)

        self.buttonNewGame.clicked.connect(self.NewGameBtnClicked)

        self.buttonAbout = QPushButton("About", self)
        self.buttonAbout.setIcon(QtGui.QIcon("about.png"))
        self.buttonAbout.setIconSize(QtCore.QSize(40, 40))
        self.buttonAbout.setMinimumHeight(40)
        self.buttonAbout.setMaximumWidth(200)
        self.gridLayout.addWidget(self.buttonAbout, 2, 1)

        self.buttonAbout.clicked.connect(self.AboutBtnClicked)

        self.buttonExit = QPushButton("Exit Game", self)
        self.buttonExit.setIcon(QtGui.QIcon("exit.png"))
        self.buttonExit.setIconSize(QtCore.QSize(40, 40))
        self.buttonExit.setMinimumHeight(40)
        self.buttonExit.setMaximumWidth(200)
        self.gridLayout.addWidget(self.buttonExit, 3, 1)

        btbStyle = ("QPushButton{"
                           "color: white; background-color: green; font:bold; border-style: outset; border-width: 2px; border-color: grey"
                           "}"
                           "QPushButton:hover{"
                           "background-color: #3F7FBF"
                           "}")

        #button style
        self.buttonNewGame.setStyleSheet(btbStyle)
        self.buttonAbout.setStyleSheet(btbStyle)
        self.buttonExit.setStyleSheet(btbStyle)



        self.buttonExit.clicked.connect(self.ExitbtnClicked)

        self.groupBox.setLayout(self.gridLayout)


    def NewGameBtnClicked(self):
        self.labelT.setText("implement")



    def AboutBtnClicked(self):
        self.close()
        #baca exception na skoro bilo sta
        #self.dialog.show()


    def ExitbtnClicked(self):
        self.close()
