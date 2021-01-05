from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Board import Board
from Player import Player


class SnakeGame(QMainWindow):
    def __init__(self):
        super(SnakeGame, self).__init__()
        self.sboard = Board(self, 2)  # start the game with 2 players
        self.sboard.setStyleSheet("QWidget {background-image: url(background.jpg)}")
        self.setCentralWidget(self.sboard)
        self.setWindowTitle('DRS Snake Game')
        # self.setStyleSheet("QWidget {background-image: url(background.jpg)}")
        self.setFixedSize(1200, 900)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)
        self.form_widget = FormWidget(self)
        layout = QGridLayout(self)
        layout.addWidget(self.sboard, 0, 0, 7, 6)  # od 0 - 3 row, 0 - 2 clmn
        self.forma = FormWidget(self)
        # self.forma.setStyleSheet("background-color: yellow;")
        # layout.addWidget(FormWidget(self))
        widget = QWidget()
        # self.forma.move(150,150)
        # self.forma.resize(50,50)
        layout.addWidget(self.forma, 6, 6)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # self.sboard.start()
        self.show()


class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout(self)
        self.labelPlayer = QLabel("Playing : Player " + str(parent.sboard.turnPlayer.Name))
        self.labelPlayersNum = QLabel("Number of players: " + str(parent.sboard.numberOfPlayers))
        self.button1 = QPushButton("End turn")
        self.button1.setStyleSheet("QPushButton{"
                                      "color: white; background-color: green; font:bold; border-style: outset; border-width: 2px; border-color: grey"
                                      "}"
                                      "QPushButton:hover{"
                                      "background-color: #3F7FBF"
                                      "}")
        self.button1.resize(20, 30)
        self.button1.move(50, 50)
        self.button1.clicked.connect(self.endTurnClick)
        self.layout.addWidget(self.labelPlayersNum)
        self.layout.addWidget(self.labelPlayer)
        self.layout.addWidget(self.button1)
        #self.button2 = QPushButton("Button 2")
        #self.layout.addWidget(self.button2)

        self.setLayout(self.layout)

    def endTurnClick(self):
        self.parent.sboard.turnPlayer.endTurn()
        self.labelPlayer.setText("Playing : Player " + str(self.parent.sboard.turnPlayer.Name))