#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from instructions import Instructions
from scene import Scene

"""Main module of the game that holds the MainMenu class and the main script to launch the program."""

__author__ = 'Toni Ojala'


class MainMenu(QWidget):
    """Main menu of the game that holds options: play (level choice) and quit."""

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.title = 'Catnip Hunt'
        self.setWindowIcon(QIcon('./pictures/cat.png'))

        self.instructions = Instructions(self)
        self.scene = None

        self.mainmenu_items = []
        self.mapmenu_items = []

        self.setWindowTitle(self.title)
        self.setFixedSize(860, 640)  # Menu window size, centered

        self.init_mainmenu()
        self.init_mapmenu()

        # Set the window background
        self.palette = QPalette()
        self.pixmap = QPixmap('./pictures/menu_cat.png').scaled(860, 640)
        self.palette.setBrush(QPalette.Background, QBrush(self.pixmap))
        self.setPalette(self.palette)

    def init_mainmenu(self):
        """Set up the main menu layout"""

        self.play = QPushButton('PLAY!', self)
        self.play.setFixedSize(312, 144)
        self.play.adjustSize()
        self.play.setStyleSheet('''
                                background-image: url(./pictures/console_button.png);
                                border: none;
                                ''')
        self.play.move(520, 180)
        self.play.clicked.connect(self.map_menu)
        self.mainmenu_items.append(self.play)

        self.quit = QPushButton('', self)
        self.quit.setFixedSize(192, 192)
        self.quit.setStyleSheet('''
                                background-image: url(./pictures/quit.png);
                                border: none;
                                ''')
        self.quit.move(575, 400)
        self.quit.clicked.connect(self.close)
        self.mainmenu_items.append(self.quit)

        self.show()

    def init_mapmenu(self):
        """Set up the map menu layout"""

        self.level1 = QPushButton('', self)
        self.level1.setFixedSize(192, 192)
        self.level1.setStyleSheet('''
                                  color: black;
                                  background-image: url(./pictures/level1.png);
                                  border: none;
                                  ''')
        self.level1.move(80, 60)
        self.level1.clicked.connect(self.start_level1)
        self.mapmenu_items.append(self.level1)

        self.level2 = QPushButton('', self)
        self.level2.setFixedSize(192, 192)
        self.level2.setStyleSheet('''
                                  color: black;
                                  background-image: url(./pictures/level2.png);
                                  border: none;
                                  ''')
        self.level2.move(330, 70)
        self.level2.clicked.connect(self.start_level2)
        self.mapmenu_items.append(self.level2)

        self.level3 = QPushButton('', self)
        self.level3.setFixedSize(192, 192)
        self.level3.setStyleSheet('''
                                  color: black;
                                  background-image: url(./pictures/level3.png);
                                  border: none;
                                  ''')
        self.level3.move(580, 70)
        self.level3.clicked.connect(self.start_level3)
        self.mapmenu_items.append(self.level3)

        self.level_n = QPushButton('', self)
        self.level_n.setFixedSize(192, 192)
        self.level_n.setStyleSheet('''
                                   color: black;
                                   background-image: url(./pictures/level_n.png);
                                   border: none;
                                   ''')
        self.level_n.move(80, 330)
        self.level_n.clicked.connect(self.start_level_n)
        self.mapmenu_items.append(self.level_n)

        self.cancel = QPushButton('Cancel', self)
        self.cancel.setFixedSize(256, 128)
        self.cancel.setStyleSheet('''
                                  background-image: url(./pictures/cancel.png);
                                  border: none;
                                  ''')
        self.cancel.move(578, 470)
        self.cancel.clicked.connect(self.main_menu)
        self.mapmenu_items.append(self.cancel)

    def start_level1(self):
        self.instructions.show()
        self.scene = Scene(self, './levels/level1.txt')

    def start_level2(self):
        self.instructions.show()
        self.scene = Scene(self, './levels/level2.txt')

    def start_level3(self):
        self.instructions.show()
        self.scene = Scene(self, './levels/level3.txt')

    def start_level_n(self):
        self.instructions.show()
        self.scene = Scene(self, './levels/level_n.txt')

    def map_menu(self):
        """Change the menu layout from main menu to map menu"""

        # Set the window background
        self.palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, 800)
        gradient.setColorAt(0.0, QColor(227, 0, 77))
        gradient.setColorAt(1.0, QColor(255, 255, 255))
        self.palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(self.palette)

        for item in self.mapmenu_items:
            item.show()
        for item in self.mainmenu_items:
            item.hide()

    def main_menu(self):
        """Change the menu layout from map menu to main menu"""

        #  Set the window background
        self.palette = QPalette()
        self.pixmap = QPixmap('./pictures/menu_cat.png').scaled(860, 640)
        self.palette.setBrush(QPalette.Background, QBrush(self.pixmap))
        self.setPalette(self.palette)

        for item in self.mainmenu_items:
            item.show()
        for item in self.mapmenu_items:
            item.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    execute = MainMenu()
    sys.exit(app.exec())
