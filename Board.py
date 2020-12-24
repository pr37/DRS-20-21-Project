from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QFrame
import random

from Config import Config
from GridElement import GridElementType

from Movement import Movement
from Player import Player
from Drawer import Drawer


class Board(QFrame):
    SPEED = 150
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40
    Timer = QBasicTimer()
    Players = []
    Movement = Movement()
    Drawer = Drawer()

    def __init__(self, parent, numberOfPlayers):
        super(Board, self).__init__(parent)
        self.Foods = []
        self.config = Config()
        self.setFocusPolicy(Qt.StrongFocus)
        self.numberOfPlayers = numberOfPlayers

        self.Grid = self.createGrid()

        for i in range(numberOfPlayers):
            offset = i * 10
            snake1 = [[5 + offset, 13], [5 + offset, 14], [5 + offset, 15]]
            snake2 = [[9 + offset, 13], [9 + offset, 14], [9 + offset, 15]]
            snake3 = [[13 + offset, 13], [13 + offset, 14], [13 + offset, 15]]
            positions = [snake1, snake2, snake3]
            directions = [1, 1, 1]
            self.Players.append(Player(self, i, 3, positions, directions))

        self.turnPlayer = self.Players[0]
        self.generateStartingFood()

    def createGrid(self):
        grid = [[GridElementType.Empty] * self.HEIGHTINBLOCKS for _ in range(self.WIDTHINBLOCKS)]
        return grid

    def snakeUpdate(self, snakePosition, oldPosition):
        self.updateGrid(snakePosition, oldPosition, GridElementType.SnakePart)


    def updateGrid(self, newPos, oldPos, type):
        for pos in newPos:
            self.Grid[pos[0]][pos[1]] = type

        if oldPos != [] and oldPos is not None:
            self.Grid[oldPos[0]][oldPos[1]] = GridElementType.Empty
            if type == GridElementType.Food:
                newFoodList = []
                for food in self.Foods:
                    if food.position != [oldPos]:
                        newFoodList.append(food)
                self.Foods = newFoodList

    def start(self):
        self.timer.start(Board.SPEED, self) #na 150 msec radi tajmer

    def square_width(self):
        return self.contentsRect().width() / Board.WIDTHINBLOCKS

    def square_height(self):
        return self.contentsRect().height() / Board.HEIGHTINBLOCKS

    def keyPressEvent(self, event) -> None: self.Movement.keyPressEvent(self, event)

    def paintEvent(self, event) -> None: self.drawer.paintEvent(self, event)

    #def timerEvent(self, event):
    #    if event.timerId() == self.timer.timerId():
    #        self.Movement.move_snake(self)
    #        self.update()
