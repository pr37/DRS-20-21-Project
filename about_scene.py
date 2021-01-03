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
        self.pixmap = QPixmap('Images/img.png')
        self.label.setPixmap(self.pixmap)
        self.label.resize(self.width - 2, self.height - 2)
        self.addWidget(self.label)

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