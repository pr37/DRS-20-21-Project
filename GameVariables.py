
class GameVariables:
    def __init__(self):
        self.numOfPlayers = 2  #TODO stavi posle na 0 i povezi sa UI da kupi odatle
        self.playersSnakesPositions = [] #sve ih gurni u jednu
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


