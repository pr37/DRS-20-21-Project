from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtWidgets import QFrame
import random

#from Game.main import MainWindow#ja
from Game.Pobeda import MainWindow
from Game.GameObjects.PowerUp import PowerUp, PowerEffects
from Service.Config import Config
from Service.GameVariables import GameVariables
from Game.GameObjects.GridElement import GridElementType

from Movement import Movement, MovementDirection
from Game.GameObjects.Player import Player
from Game.GameObjects.Drawer import Drawer
from Game.GameObjects.Food import Food
from Game.GameObjects.Snake import Snake
from Game.GameObjects.Wall import Wall


class Board(QFrame):
    config = Config()
    SPEED = config.SPEED
    WIDTHINBLOCKS = config.WIDTHINBLOCKS
    HEIGHTINBLOCKS = config.HEIGHTINBLOCKS

    Timer = QBasicTimer()
    Movement = Movement()
    Drawer = Drawer()

    # parent ignorisi, qt stvar
    # numberOfPlayers broj igraca
    # startingSnakesPosition pocetna pozicija zmija , u obliku matrice tj liste listi, gde je npr.
    # startingSnakesPosition[0] lista pozicija zmija prvog igraca (nesto kao [[[5,6],[6,6],[7,6]] , [[x,y]]])
    # to znaci da imaju dve zmije, jedna ima tri dela na poljima 5,6.. i druga koja ima samo glavu na polju x,y
    # PODRAZUMEVA SE DA ZMIJA GLEDA NA GORE
    # startingFoods lista pozicija pocetne hrane (nesto kao [[10,10],[15,17],[20,21]] )
    # znaci imaju tri hrane na tim poljima
    # startingWalls slicno kao za food samo za zid
    def __init__(self, parent, numberOfPlayers, startingSnakesPosition=None, startingFoods=None, startingWalls=None):
        super(Board, self).__init__(parent)
        self.Foods = []
        self.Players = []
        self.Walls = []
        self.PowerUps = []
        self.config = Config()
        self.setFocusPolicy(Qt.StrongFocus)
        self.numberOfPlayers1 = int(numberOfPlayers)
        self.eventHappened = False
        self.Grid = self.createGrid()
        config = Config()
        self.moveTime = config.moveTime
        self.timeLeft = self.moveTime
        self.timer = QBasicTimer()
        self.parent = parent
        self.chanceForDeath = config.chanceForDeath
        self.powerUpSpawnTimer = config.powerUpSpawnTimer
        self.powerUpLiveTimer = config.powerUpLiveTimer
        self.turnCount = 0
        #self.mw = MainWindow()
        self.mw = None

        if self.numberOfPlayers1 == 2:
            dividerX = 0
            dividerY = 4
        elif self.numberOfPlayers1 == 3:
            dividerX = -5
            dividerY = 3
        else :
            dividerX = 0
            dividerY = 1

        if startingSnakesPosition is None:
            for i in range(self.numberOfPlayers1):
                offset = i * 10
                snake1 = [[5 + offset + dividerX, 13 + dividerY], [5 + offset + dividerX, 14 + dividerY], [5 + offset + dividerX, 15 + dividerY]]
                #snake1 = [[5 + offset + divider, 13], [5 + offset + divider, 14], [5 + offset + divider, 15]]
                snake2 = [[9 + offset + dividerX, 13 + dividerY], [9 + offset + dividerX, 14 + dividerY], [9 + offset + dividerX, 15 + dividerY]]
                snake3 = [[13 + offset + dividerX, 13 + dividerY], [13 + offset + dividerX, 14 + dividerY], [13 + offset + dividerX, 15 + dividerY]]
                positions = [snake1, snake2, snake3]
                directions = [MovementDirection.Up, MovementDirection.Up, MovementDirection.Up]
                self.Players.append(Player(self, i, 3, positions, directions))
                dividerY = dividerY * (-2)
                dividerX = dividerX * (-2)
        else:
            for i in range(numberOfPlayers):
                snakes = []
                directions = []
                for j in range(len(startingSnakesPosition[i])):
                    if not startingSnakesPosition[i][j]:
                        continue
                    snakes.append(startingSnakesPosition[i][j])
                    directions.append(MovementDirection.Up)
                if not snakes:
                    continue
                self.Players.append((Player(self, i, len(snakes), snakes, directions)))

        cnt = 0
        if startingWalls is None:
            for x in range(self.HEIGHTINBLOCKS):
                cnt = cnt + 1
                if cnt % 5 == 0:
                    if cnt > 20:
                        self.Walls.append(Wall(self, [x - dividerX - dividerY, x]))
                    else:
                        self.Walls.append(Wall(self, [x, x]))
                if cnt % 10 == 0:
                    self.Walls.append(Wall(self, [x, x - 4]))
        else:
            for wallPos in startingWalls:
                self.Walls.append(Wall(self, wallPos))

        self.turnPlayer = self.Players[0]
        self.turnPlayerIndex = 0

        if startingFoods is None:
            self.generateStartingFood()
        else:
            for foodPos in startingFoods:
                self.Foods.append(Food(self, foodPos))

        self.start()

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

        if self.turnPlayer not in self.Players:
            index = (self.turnPlayerIndex + 1) % len(self.Players)
        else:
            index = (self.Players.index(self.turnPlayer) + 1) % len(self.Players)
        self.turnPlayer = self.Players[index]
        self.turnPlayerIndex = index

        self.timeLeft = self.moveTime
        self.turnCount += 1
        self.updatePowerUp()
        self.update()
        # print("Na redu je igrac " + str(index))

    def updatePowerUp(self):
        died = []
        for powerUp in self.PowerUps:
            if powerUp.update():
                died.append(powerUp)
        for power in died:
            self.gameObjectUpdate([], power.position, power.type)

        if self.turnCount % self.powerUpSpawnTimer == 0:
            self.spawnPowerUp()

    def spawnPowerUp(self):
        while True:
            rndWidth = random.randint(0, self.WIDTHINBLOCKS - 1)
            rndHeight = random.randint(0, self.HEIGHTINBLOCKS - 1)

            position = [rndWidth, rndHeight]
            if self.checkIfEmpty(position):
                break

        self.PowerUps.append(PowerUp(self, position, self.powerUpLiveTimer, self.chanceForDeath))

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
                elif type == GridElementType.PowerUp:
                    newPowerList= []
                    for power in self.PowerUps:
                        if power.position != [position]:
                            newPowerList.append(power)
                    self.PowerUps = newPowerList

    def start(self):
        self.timer.start(Board.SPEED, self)

    def square_width(self):
        return self.contentsRect().width() / Board.WIDTHINBLOCKS

    def square_height(self):
        return self.contentsRect().height() / Board.HEIGHTINBLOCKS

    def keyPressEvent(self, event):
        self.Movement.keyPressEvent(self, event)
        self.eventHappened = True
        # if len(self.Players == 0):
        #     return 1
        # else :
        #     return 0

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

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.timeLeft -= 1
            self.parent.updateLabel(self.timeLeft)
            if self.timeLeft == 0:  # force end the turn
                self.timeLeft = self.moveTime
                print("isteklo vreme")
                self.nextPlayerTurn()

    def updateGameState(self, newGameState):
        if newGameState is not GameVariables:
            return

        self.Grid = newGameState.Grid
        self.Foods = []
        for foodPos in newGameState.foodPositions:
            self.Foods.append(Food(self, foodPos[0]))
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
        self.turnPlayer = self.Players[newGameState.playerTurn]
        self.turnPlayer.turnSnake = self.turnPlayer.Snakes[newGameState.snakeTurn]

    def checkSnakesCaptures(self):
        for player in self.Players:
            for snake in player.Snakes:
                if snake.checkCapture():
                    player.snakeDied(snake)

    def playerLost(self, player):
        self.Players.remove(player)
        if len(self.Players) <= 1:
            self.gameOver()

    # kraaaaj
    def gameOver(self):
        if len(self.Players) == 0:
            pass  # mozda neka situacija kad se ubiju nekako medjusobno pa je nereseno? nzm verovatno je nepotrebno


        print("Pobedio je igrac " + str(self.Players[0].Name) + " !")  # TODO victory prozor
        print("Kraj igre")
        mw = MainWindow()
        mw.WinGame(str(self.Players[0].Name + 1))

    def determinePowerUp(self, position):
        for powerUps in self.PowerUps:
            if powerUps.position == position:
                return powerUps.determineEffect() == PowerEffects.Grow
