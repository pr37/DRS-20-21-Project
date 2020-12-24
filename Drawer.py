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

    def draw_square(painter, x, y, w, h, playerCurrent, isHead):  # crta kockicu zmijice
        if not isHead:
            if playerCurrent == 0:
                # color = Drawer.config.snakeColor1
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("diamond.png"))
            elif playerCurrent == 1:
                # color = Drawer.config.snakeColor2
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("gold.png"))
            elif playerCurrent == 2:
                # color = Drawer.config.snakeColor3
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("sapphire.png"))
            else:
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("emerald.png"))
            # painter.fillRect(x + 1, y + 1, w - 2,
            #                h - 2, color)
        else:
            Drawer.draw_head(painter, x, y, w, h)
