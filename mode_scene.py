from PyQt5.QtCore import QSize, QDir, Qt
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel, QComboBox


class ModeScene(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.parent = parent

        self.label = QLabel()
        self.pixmap = QPixmap('snake_background.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width - 2, self.height - 2)
        self.addWidget(self.label)

        self.mainLabel = QLabel("SELECT MODE")
        self.mainLabel.resize(230, 100)
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold; background:transparent")
        self.mainLabel.move(180, 0)
        self.addWidget(self.mainLabel)

        """
        self.twoPlayerBtn = QPushButton("2 Players")
        self.twoPlayerBtn.setStyleSheet("QPushButton{"
                                       "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                       "}"
                                       "QPushButton:hover{"
                                       "background-color: #3F7FBF"
                                       "}")
        self.twoPlayerBtn.resize(100, 50)
        self.twoPlayerBtn.move(250, 100)
        self.addWidget(self.twoPlayerBtn)

        self.threePlayerBtn = QPushButton("3 Players")
        self.threePlayerBtn.setStyleSheet("QPushButton{"
                                          "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                          "}"
                                          "QPushButton:hover{"
                                          "background-color: #3F7FBF"
                                          "}")
        self.threePlayerBtn.resize(100, 50)
        self.threePlayerBtn.move(250, 165)
        self.addWidget(self.threePlayerBtn)

        self.fourPlayerBtn = QPushButton("4 Players")
        self.fourPlayerBtn.setStyleSheet("QPushButton{"
                                         "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                         "}"
                                         "QPushButton:hover{"
                                         "background-color: #3F7FBF"
                                         "}")
        self.fourPlayerBtn.resize(100, 50)
        self.fourPlayerBtn.move(250, 230)
        self.addWidget(self.fourPlayerBtn)
        """
        # drop down menu
        self.mainLabel = QLabel("Number of players:")
        self.mainLabel.resize(230, 100)
        self.mainLabel.setStyleSheet("color: white; font-size:16px; font:bold; background:transparent")
        self.mainLabel.move(220, 70)
        self.addWidget(self.mainLabel)

        # moze li align center?
        self.playerComboBox = QComboBox()
        self.playerComboBox.addItem("2")
        self.playerComboBox.addItem("3")
        self.playerComboBox.addItem("4")
        self.playerComboBox.setStyleSheet("QComboBox{"
                                         "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white; font-size:16px"                                         
                                         "}"
                                         "QComboBox:hover{"
                                         "background-color: #3F7FBF"
                                         "}")
        self.playerComboBox.resize(100, 50)
        self.playerComboBox.move(250, 150)
        self.addWidget(self.playerComboBox)

        self.playButton = QPushButton("Play")
        self.playButton.setStyleSheet("QPushButton{"
                                     "color: white; background-color: transparent; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                     "}"
                                     "QPushButton:hover{"
                                     "background-color: #3F7FBF"
                                     "}")
        self.playButton.resize(100, 50)
        self.playButton.move(250, 265)
        self.addWidget(self.playButton)


        self.returnBtn = QPushButton("Return")
        self.returnBtn.setStyleSheet("QPushButton{"
                                     "color: white; background-color: #3F7FBF; font:bold; border-style: outset; border-width: 2px; border-color: white"
                                     "}"
                                     "QPushButton:hover{"
                                     "background-color: #C14242"
                                     "}")
        self.returnBtn.resize(100, 50)
        self.returnBtn.move(250, 330)
        self.addWidget(self.returnBtn)