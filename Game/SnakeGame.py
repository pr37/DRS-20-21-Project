from PyQt5.QtWidgets import *
from Board import Board


class SnakeGame(QMainWindow):
    def __init__(self,numOfPlayers):
        super(SnakeGame, self).__init__()
        self.sboard = Board(self, numOfPlayers)  # start the game with 2 players


        # primeri za pravljanje table
        # [x,y] 0,0 koordinata je gore levo (ne dole levo), x ide do 60, y do 40
        # exampleSnakes = [[[[5, 13], [5, 14], [5, 15]], [[7, 13], [7, 14]]],  # dve zmije prvom igracu
        #                  [[[9, 13], [9, 14]]],
        #                  [[[14, 13], [14, 14]]]]
        # exampleFoods = [[11, 9],
        #                 [24, 20],
        #                 [24, 21],
        #                 [1, 15],
        #                 [50, 8]]
        # exampleWalls = [[10, 10],
        #                 [11, 11],
        #                 [12, 12]]
        # self.sboard = Board(self, 3, startingSnakesPosition=exampleSnakes, startingFoods=exampleFoods, startingWalls=exampleWalls)

        self.sboard.setStyleSheet("QWidget {background-image: url(Images/background.jpg)}")
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

    def updateLabel(self, time):
        self.forma.updateLabel(time)

class FormWidget(QWidget):
    def __init__(self, parent):
        super(FormWidget, self).__init__()
        super(FormWidget, self).__init__()
        self.parent = parent
        self.layout = QVBoxLayout(self)
        self.labelTime = QLabel("Time : inf s")
        self.labelPlayer = QLabel("Playing : Player " + str(parent.sboard.turnPlayer.Name))
        self.labelPlayersNum = QLabel("Number of players: " + str(parent.sboard.numberOfPlayers1))
        self.previousSnake = QPushButton("Previous snake")
        self.previousSnake.setStyleSheet("QPushButton{"
                                   "color: white; background-color: black; font:bold; border-style: outset; border-width: 2px; border-color: grey"
                                   "}"
                                   "QPushButton:hover{"
                                   "background-color: #3F7FBF"
                                   "}")
        self.previousSnake.clicked.connect(self.previousSnakeClick)
        self.previousSnake.resize(10, 20)
        self.previousSnake.move(40, 40)
        self.nextSnake = QPushButton("Next snake")
        self.nextSnake.setStyleSheet("QPushButton{"
                                         "color: white; background-color: blue; font:bold; border-style: outset; border-width: 2px; border-color: grey"
                                         "}"
                                         "QPushButton:hover{"
                                         "background-color: #3F7FBF"
                                         "}")
        self.nextSnake.resize(10, 20)
        self.nextSnake.move(40, 40)
        self.nextSnake.clicked.connect(self.nextSnakeClick)

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
        self.layout.addWidget((self.labelTime))
        self.layout.addWidget(self.labelPlayersNum)
        self.layout.addWidget(self.labelPlayer)
        self.layout.addWidget(self.previousSnake)  # ja
        self.layout.addWidget(self.nextSnake)  # ja
        self.layout.addWidget(self.button1)
        # self.button2 = QPushButton("Button 2")
        # self.layout.addWidget(self.button2)

        self.setLayout(self.layout)

    def endTurnClick(self):
        self.parent.sboard.turnPlayer.endTurn()
        self.labelPlayer.setText("Playing : Player " + str(self.parent.sboard.turnPlayer.Name))
        self.parent.sboard.setFocus()

    def previousSnakeClick(self):
        self.parent.sboard.turnPlayer.prevSnake()
        self.parent.sboard.setFocus()

    def nextSnakeClick(self):
        self.parent.sboard.turnPlayer.nextSnake()
        self.parent.sboard.setFocus()

    def updateLabel(self, time):
        self.labelTime.setText("Time : " + str(time) + " s")
        self.labelPlayer.setText("Playing : Player " + str(self.parent.sboard.turnPlayer.Name))