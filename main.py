import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QApplication([])
    widget = QtWidgets.QWidget()
    widget.resize(300, 200)
    widget.setWindowTitle("Snake")
    widget.show()
    sys.exit(app.exec_())