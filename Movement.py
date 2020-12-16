from PyQt5.QtCore import QBasicTimer, Qt

class Movement():
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40

    @staticmethod
    def keyPressEvent(self, event):  # levo1 desno2 dole3 gore4
        key = event.key()
        if key == Qt.Key_Left:
            if self.direction != 2:  # ako je isao desno ne moze levo
                self.direction = 1
        elif key == Qt.Key_Right:
            if self.direction != 1:
                self.direction = 2
        elif key == Qt.Key_Down:
            if self.direction != 4:
                self.direction = 3
        elif key == Qt.Key_Up:
            if self.direction != 3:
                self.direction = 4