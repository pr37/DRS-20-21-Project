from PyQt5.QtCore import QSize, QDir, Qt, QRectF
from PyQt5.QtGui import QBrush, QFont, QPalette, QFontDatabase, QImage, QPixmap
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QPushButton, QLabel


class AboutScene(QGraphicsScene):
    def __init__(self, parent, width, height):
        super().__init__(parent)
        self.width = width
        self.height = height
        self.setSceneRect(QRectF(0, 0, self.width - 2, self.height - 2))

        self.label = QLabel()
        self.pixmap = QPixmap('Images/snake_background.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width - 2, self.height - 2)
        self.addWidget(self.label)

        self.mainLabel = QLabel("CONTROLS")
        self.mainLabel.resize(200, 100)
        self.mainLabel.setStyleSheet("color: white; font-size:32px; font:bold; background:transparent")
        self.mainLabel.move(214, 0)
        self.addWidget(self.mainLabel)

        self.labelKeys = QLabel()
        self.labelKeys.setStyleSheet("background:transparent")
        self.pixmapKeys = QPixmap('Images/w_key.png')
        self.labelKeys.setPixmap(self.pixmapKeys)
        self.labelKeys.resize(width - 500, 50)
        self.labelKeys.move(30, 90)
        self.addWidget(self.labelKeys)

        self.forwardLabel = QLabel("Up")
        self.forwardLabel.resize(width - 300, 50)
        self.forwardLabel.setStyleSheet("color: white; font-size:22px; font:bold; background:transparent")
        self.forwardLabel.move(100,90)
        self.addWidget(self.forwardLabel)

        self.labelKeys = QLabel()
        self.labelKeys.setStyleSheet("background:transparent")
        self.pixmapKeys = QPixmap('Images/s_key.png')
        self.labelKeys.setPixmap(self.pixmapKeys)
        self.labelKeys.resize(width - 500, 50)
        self.labelKeys.move(30, 150)
        self.addWidget(self.labelKeys)

        self.forwardLabel = QLabel("Down")
        self.forwardLabel.resize(width - 300, 50)
        self.forwardLabel.setStyleSheet("color: white; font-size:22px; font:bold; background:transparent")
        self.forwardLabel.move(100, 150)
        self.addWidget(self.forwardLabel)

        self.labelKeys = QLabel()
        self.labelKeys.setStyleSheet("background:transparent")
        self.pixmapKeys = QPixmap('Images/a_key.png')
        self.labelKeys.setPixmap(self.pixmapKeys)
        self.labelKeys.resize(width - 500, 50)
        self.labelKeys.move(30, 210)
        self.addWidget(self.labelKeys)

        self.forwardLabel = QLabel("Left")
        self.forwardLabel.resize(width - 300, 50)
        self.forwardLabel.setStyleSheet("color: white; font-size:22px; font:bold; background:transparent")
        self.forwardLabel.move(100, 210)
        self.addWidget(self.forwardLabel)

        self.labelKeys = QLabel()
        self.labelKeys.setStyleSheet("background:transparent")
        self.pixmapKeys = QPixmap('Images/d_key.png')
        self.labelKeys.setPixmap(self.pixmapKeys)
        self.labelKeys.resize(width - 500, 50)
        self.labelKeys.move(30, 270)
        self.addWidget(self.labelKeys)

        self.forwardLabel = QLabel("Right")
        self.forwardLabel.resize(width - 300, 50)
        self.forwardLabel.setStyleSheet("color: white; font-size:22px; font:bold; background:transparent")
        self.forwardLabel.move(100, 270)
        self.addWidget(self.forwardLabel)

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