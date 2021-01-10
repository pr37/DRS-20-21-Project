from PyQt5.QtGui import QPainter, QColor


class Config:
    def __init__(self):
        # super(Config, self).__init__(parent)
        self.MAXSnakesPerPlayer = 3
        self.snakeColor1 = QColor(0x203b27)
        self.snakeColor2 = QColor(0x2e2abd)
        self.snakeColor3 = QColor(0x2bb5b5)
        self.snakeColor4 = QColor(0xe83023)
        self.startingFoodCount = 5
        self.SPEED = 1000
        self.WIDTHINBLOCKS = 60
        self.HEIGHTINBLOCKS = 40
        self.moveTime = 30 #in seconds
        self.chanceForDeath = 10
        self.powerUpSpawnTimer = 2 #in turns
        self.powerUpLiveTimer = 2
