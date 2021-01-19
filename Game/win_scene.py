from PyQt5.QtCore import QSize, QDir, Qt, QRectF
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel
#from Game.main import MainWindow

class WinScene(QGraphicsScene):
    def __init__(self, parent, width, height, txt):
        super().__init__(parent)
        self.txt = txt
        self.width = width
        self.height = height
        self.setSceneRect(QRectF(0, 0, self.width - 2, self.height - 2))

        self.label = QLabel()
        self.pixmap = QPixmap('snake_background.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width - 2, self.height - 2)
        self.addWidget(self.label)

        self.mainLabel = QLabel("CONGRATS")
        self.mainLabel.resize(200, 100) #veca velicina
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold; background:transparent")
        self.mainLabel.move(214, 0)
        self.addWidget(self.mainLabel)

        self.winLabel = QLabel("Plr with num " + self.txt + " is a winner")
        self.winLabel.resize(600, 150)  # veca velicina
        self.winLabel.setStyleSheet("color: white; font-size:32px; font:bold; background:transparent")
        self.winLabel.move(60, 5)
        self.addWidget(self.winLabel)

        self.exitBtn = QPushButton("Exit")
        self.exitBtn.setStyleSheet("QPushButton{"
                                   "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                   "}"
                                   "QPushButton:hover{"
                                   "background-color: #C14242"
                                   "}")
        self.exitBtn.resize(100, 50)
        self.exitBtn.move(250, 230)
        self.addWidget(self.exitBtn)


