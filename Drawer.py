from PyQt5.QtGui import *
from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import *
from Config import Config
import random

class Drawer:
    WIDTHINBLOCKS = 60
    HEIGHTINBLOCKS = 40
    config = Config()

    @staticmethod
    def paintEvent(board, event):
        painter = QPainter(board)
        rect = board.contentsRect()  # povrsina izmedju margina widgeta
        boardtop = rect.bottom() - Drawer.HEIGHTINBLOCKS * board.square_height()

        for food in board.Foods:
            Drawer.draw_food(painter, rect.left() + food.position[0][0] * board.square_width(),
                             boardtop + food.position[0][1] * board.square_height(), board.square_width(),
                             board.square_height())

        # Drawer.draw_food(painter,100,100,22,22)

        for players in board.Players:  # pls fix this mess
            i = 0
            for snake in board.Players[i].Snakes:
                for pos in snake.snakePosition:
                    if snake.snakePosition[0] == pos:
                        isHead = True
                    else:
                        isHead = False
                    Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
                                       boardtop + pos[1] * board.square_height(), board.square_width(),
                                       board.square_height(), board.Players[i].Name, isHead)

        for snake in board.Players[1].Snakes:
            for pos in snake.snakePosition:
                if snake.snakePosition[0] == pos:
                    isHead = True
                else:
                    isHead = False
                Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
                                   boardtop + pos[1] * board.square_height(), board.square_width(),
                                   board.square_height(), board.Players[1].Name, isHead)
        if len(board.Players) == 3:
            for snake in board.Players[2].Snakes:
                for pos in snake.snakePosition:
                    if snake.snakePosition[0] == pos:
                        isHead = True
                    else:
                        isHead = False
                    Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
                                       boardtop + pos[1] * board.square_height(), board.square_width(),
                                       board.square_height(), board.Players[2].Name, isHead)

        if len(board.Players) == 4:
            for snake in board.Players[3].Snakes:
                for pos in snake.snakePosition:
                    if snake.snakePosition[0] == pos:
                        isHead = True
                    else:
                        isHead = False
                    Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
                                       boardtop + pos[1] * board.square_height(), board.square_width(),
                                       board.square_height(), board.Players[3].Name, isHead)

    def draw_square(self, painter, x, y, w, h, isHead):  # crta kockicu zmijice
        color = QColor(0x302213)
        painter.fillRect(x + 1, y + 1, w - 2,
                         h - 2, color)
