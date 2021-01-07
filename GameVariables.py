
class GameVariables:
    def __init__(self):
        self.numOfPlayers = 0  #TODO stavi posle na 0 i povezi sa UI da kupi odatle
        self.player1Snakes = []
        self.player2Snakes = []
        self.player3Snakes = []
        self.player4Snakes = []
        self.foodPositions = []
        self.playerTurn = 0
        self.snakeTurn = 0


class MutableEventWrapper:
    def __init__(self):
        self.eventHappened = False

    def startEvent(self):
        self.eventHappened = True

    def cancelEvent(self):
        self.eventHappened = False


