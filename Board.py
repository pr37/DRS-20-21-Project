from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QPainter, QColor, QKeyEvent
from PyQt5.QtWidgets import QFrame
import random

from Config import Config
from GameVariables import GameVariables
from GridElement import GridElementType

from Movement import Movement, MovementDirection
from Player import Player
from Drawer import Drawer
from Food import Food
from Snake import Snake
from Wall import Wall


class Board(QFrame):
    SPEED = 150
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40
    Timer = QBasicTimer()
    Movement = Movement()
    Drawer = Drawer()

    def __init__(self, parent, numberOfPlayers):
        super(Board, self).__init__(parent)
        self.Foods = []
        self.Players = []
        self.Walls = []
        self.config = Config()
        self.setFocusPolicy(Qt.StrongFocus)
        self.numberOfPlayers = numberOfPlayers
        self.eventHappened = False
        self.Grid = self.createGrid()

        for i in range(numberOfPlayers):
            offset = i * 10
            snake1 = [[5 + offset, 13], [5 + offset, 14], [5 + offset, 15]]
            snake2 = [[9 + offset, 13], [9 + offset, 14], [9 + offset, 15]]
            snake3 = [[13 + offset, 13], [13 + offset, 14], [13 + offset, 15]]
            positions = [snake1, snake2, snake3]
            directions = [MovementDirection.Up, MovementDirection.Up, MovementDirection.Up]
            self.Players.append(Player(self, i, 3, positions, directions))

        # hardcoded starting walls
        for x in range(self.HEIGHTINBLOCKS):
            self.Walls.append(Wall(self, [x, x]))

        self.turnPlayer = self.Players[0]
        self.turnPlayerIndex = 0
        self.generateStartingFood()

    def createGrid(self):
        grid = [[GridElementType.Empty] * self.HEIGHTINBLOCKS for _ in range(self.WIDTHINBLOCKS)]
        return grid

    def snakeUpdate(self, snakePosition, oldPosition):
        self.updateGrid(snakePosition, oldPosition, GridElementType.SnakePart)

    # def foodUpdate(self, foodPosition, oldPosition):
    #     self.updateGrid(foodPosition, oldPosition, GridElementType.Food)

    def gameObjectUpdate(self, position, oldPosition, type):
        self.updateGrid(position, oldPosition, type)

    def generateStartingFood(self):
        for _ in range(self.config.startingFoodCount):
            self.spawnFood()

    def nextPlayerTurn(self):
        for food in self.Foods:
            food.move()

        self.spawnFood()

        index = (self.Players.index(self.turnPlayer) + 1) % len(self.Players)
        self.turnPlayer = self.Players[index]
        self.turnPlayerIndex = index

        self.update()
        # print("Na redu je igrac " + str(index))

    def updateGrid(self, newPos, oldPos, type):
        for pos in newPos:
            self.Grid[pos[0]][pos[1]] = type

        if oldPos != [] and oldPos is not None:
            for position in oldPos:
                self.Grid[position[0]][position[1]] = GridElementType.Empty
                if type == GridElementType.Food:
                    newFoodList = []
                    for food in self.Foods:
                        if food.position != [position]:
                            newFoodList.append(food)
                    self.Foods = newFoodList

    def start(self):
        self.timer.start(Board.SPEED, self)  # na 150 msec radi tajmer

    def square_width(self):
        return self.contentsRect().width() / Board.WIDTHINBLOCKS

    def square_height(self):
        return self.contentsRect().height() / Board.HEIGHTINBLOCKS

    def keyPressEvent(self, event):
        self.Movement.keyPressEvent(self, event)
        self.eventHappened = True

    def paintEvent(self, event):
        self.Drawer.paintEvent(self, event)
        self.eventHappened = False  # pazi za hranu

    def spawnFood(self):
        while True:
            rndWidth = random.randint(0, self.WIDTHINBLOCKS - 1)
            rndHeight = random.randint(0, self.HEIGHTINBLOCKS - 1)

            position = [rndWidth, rndHeight]
            if self.checkIfEmpty(position):
                break

        self.Foods.append(Food(self, position))

    def checkIfEmpty(self, position):
        # check if theres a snake there
        # for player in self.Players:  DA NE BIH IMAO OVO SAM DODAO GRID
        #     for snake in player.Snakes:
        #         for snakePart in snake.snakePosition:
        #             if position == snakePart:
        #                 return False
        return self.Grid[position[0]][position[1]] == GridElementType.Empty

    # def timerEvent(self, event):
    #    if event.timerId() == self.timer.timerId():
    #        self.Movement.move_snake(self)
    #        self.update()

    def updateGameState(self, newGameState):
        if newGameState is not GameVariables:
            return

        self.Grid = newGameState.Grid
        self.Foods = []
        for foodPos in newGameState.foodPositions:
            self.Foods.append(Food(self, foodPos))

        self.turnPlayer = self.Players[newGameState.playerTurn]
        self.turnPlayer.turnSnake = self.turnPlayer.Snakes[newGameState.snakeTurn]

        self.Players[0].Snakes = []
        for snake in newGameState.player1Snakes:
            pos = snake[0]
            direction = snake[1]
            self.Players[0].Snakes.append(Snake(self, pos, direction))

        self.Players[1].Snakes = []
        for snake in newGameState.player2Snakes:
            pos = snake[0]
            direction = snake[1]
            self.Players[1].Snakes.append(Snake(self, pos, direction))

        i = len(self.Players)
        if i >= 3:
            self.Players[2].Snakes = []
            for snake in newGameState.player3Snakes:
                pos = snake[0]
                direction = snake[1]
                self.Players[2].Snakes.append(Snake(self, pos, direction))

        if i >= 4:
            self.Players[3].Snakes = []
            for snake in newGameState.player4Snakes:
                pos = snake[0]
                direction = snake[1]
                self.Players[3].Snakes.append(Snake(self, pos, direction))

    def checkSnakesCaptures(self):
        for player in self.Players:
            for snake in player.Snakes:
                if snake.checkCapture():
                    player.snakeDied(snake)
