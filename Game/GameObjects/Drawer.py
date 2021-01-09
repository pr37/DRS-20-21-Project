from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Service.Config import Config


# def draw_square(painter, x, y, w, h, player):  # crta kockicu zmijice
#   #color = QColor(0x302213)  # TODO zakucaj boje u config
#   painter.fillRect(x + 1, y + 1, w - 2,
#                    h - 2, color)


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

        for wall in board.Walls:
            Drawer.draw_wall(painter, rect.left() + wall.position[0][0] * board.square_width(),
                             boardtop + wall.position[0][1] * board.square_height(), board.square_width(),
                             board.square_height())

        # Drawer.draw_food(painter,100,100,22,22)

        for player in board.Players:  # pls fix this mess
            for snake in player.Snakes:
                for pos in snake.snakePosition:
                    if snake.snakePosition[0] == pos:
                        isHead = True
                    else:
                        isHead = False

                    if player.turnSnake == snake and board.turnPlayer == player:
                        isSelectedHead = True
                    else:
                        isSelectedHead = False
                    Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
                                       boardtop + pos[1] * board.square_height(), board.square_width(),
                                       board.square_height(), player.Name, isHead, isSelectedHead)
        #
        # for snake in board.Players[1].Snakes:
        #     for pos in snake.snakePosition:
        #         if snake.snakePosition[0] == pos:
        #             isHead = True
        #         else:
        #             isHead = False
        #
        #         if board.Players[1].turnSnake == snake and board.turnPlayer == board.Players[1]:
        #             isSelectedHead = True
        #         else:
        #             isSelectedHead = False
        #         Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
        #                            boardtop + pos[1] * board.square_height(), board.square_width(),
        #                            board.square_height(), board.Players[1].Name, isHead, isSelectedHead)
        # if len(board.Players) == 3:
        #     for snake in board.Players[2].Snakes:
        #         for pos in snake.snakePosition:
        #             if snake.snakePosition[0] == pos:
        #                 isHead = True
        #             else:
        #                 isHead = False
        #
        #             if board.Players[2].turnSnake == snake and board.turnPlayer == board.Players[2]:
        #                 isSelectedHead = True
        #             else:
        #                 isSelectedHead = False
        #             Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
        #                                boardtop + pos[1] * board.square_height(), board.square_width(),
        #                                board.square_height(), board.Players[2].Name, isHead, isSelectedHead)
        #
        # if len(board.Players) == 4:
        #     for snake in board.Players[3].Snakes:
        #         for pos in snake.snakePosition:
        #             if snake.snakePosition[0] == pos:
        #                 isHead = True
        #             else:
        #                 isHead = False
        #
        #             if board.Players[3].turnSnake == snake and board.turnPlayer == board.Players[3]:
        #                 isSelectedHead = True
        #             else:
        #                 isSelectedHead = False
        #             Drawer.draw_square(painter, rect.left() + pos[0] * board.square_width(),
        #                                boardtop + pos[1] * board.square_height(), board.square_width(),
        #                                board.square_height(), board.Players[3].Name, isHead, isSelectedHead)

    def draw_square(painter, x, y, w, h, playerCurrent, isHead, isSelected):  # crta kockicu zmijice
        if not isHead:
            if playerCurrent == 0:
                # color = Drawer.config.snakeColor1
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\diamond.png"))
            elif playerCurrent == 1:
                # color = Drawer.config.snakeColor2
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\gold.png"))
            elif playerCurrent == 2:
                # color = Drawer.config.snakeColor3
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\sapphire.png"))
            else:
                painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\emerald.png"))
            # painter.fillRect(x + 1, y + 1, w - 2,
            #                h - 2, color)
        elif not isSelected:
            Drawer.draw_head(painter, x, y, w, h)
        else:
            Drawer.draw_head_selected(painter, x, y, w, h)

    def draw_head(painter, x, y, w, h):
        painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\snakeheadUnselected.png"))

    def draw_wall(painter, x, y, w, h):
        painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\wall.png"))

    def draw_head_selected(painter, x, y, w, h):
        painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\snakeHead.png"))

    def draw_food(painter, x, y, w, h):
        painter.drawImage(QRect(x + 1, y + 1, w, h), QImage("Images\\food.png"))
