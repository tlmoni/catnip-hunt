# -*- coding: utf-8 -*-

from PyQt5.QtGui import QBrush, QColor, QPalette, QPixmap
from PyQt5.QtWidgets import QLabel, QPushButton, QWidget


class End(QWidget):
    """Popup screen that informs the player about the victory and offers a replay option."""

    def __init__(self, mainmenu, background, parent=None):
        QWidget.__init__(self, parent)
        self.mainmenu = mainmenu
        self.background = background
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QColor(255, 255, 255, 160)))
        self.setPalette(self.palette)

        self.setFixedSize(1610, 930)  # Menu window size, centered

        self.init_menu()

    def init_menu(self):
        """Set up the victory menu layout"""
        title_image = QLabel(self)
        title_image.setPixmap(QPixmap(self.background).scaled(579, 207))
        title_image.move(515, 120)

        self.replay = QPushButton('REPLAY!', self)
        self.replay.move(649, 400)
        self.replay.setFixedSize(312, 144)
        self.replay.setStyleSheet('''
                                  background-image: url(./pictures/console_button.png);
                                  border: none;
                                  ''')
        self.replay.clicked.connect(self.start_game)

        self.quit = QPushButton('', self)
        self.quit.setFixedSize(192, 192)
        self.quit.move(709, 600)
        self.quit.setStyleSheet('''
                                background-image: url(./pictures/white_flag_menu.png);
                                border: none;
                                ''')
        self.quit.clicked.connect(self.menu)

    def start_game(self):
        self.mainmenu.scene.player.setPos(self.mainmenu.scene.start_x, self.mainmenu.scene.start_y)  # Reset position
        if self.mainmenu.scene.mega is not None:
            self.mainmenu.scene.mega.setPos(0, self.mainmenu.scene.start_y + 64)
            self.mainmenu.scene.player.setPos(self.mainmenu.scene.start_x, self.mainmenu.scene.start_y)
        self.mainmenu.scene.timer.start(12, self.mainmenu.scene)  # Restart the game timer
        self.close()

    def menu(self):
        self.mainmenu.show()
        self.mainmenu.main_menu()
        self.mainmenu.scene.view.close()
