# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QIcon, QPalette, QPixmap
from PyQt5.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget


class Instructions(QWidget):
    """Instructs the player visually with pictures and text, how to play the game."""

    play_time = 0

    def __init__(self, mainmenu, parent=None):
        QWidget.__init__(self, parent)
        self.mainmenu = mainmenu
        self.title = 'Instructions'
        self.setWindowIcon(QIcon('./pictures/noonoo.png'))

        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QColor(255, 255, 255)))
        self.setPalette(self.palette)

        self.setWindowTitle(self.title)
        self.setFixedSize(860, 900)  # Menu window size, centered

        self.init_menu()

    def init_menu(self):
        self.play = QPushButton('Got it!', self)
        self.play.setStyleSheet('''
                                background-image: url(./pictures/paw.png);
                                border: none;
                                ''')
        self.play.setFixedSize(128, 128)
        self.play.clicked.connect(self.start_game)

        grid_layout = QGridLayout(self)  # Use a grid layout for the instructions

        # Add the image labels for instructions

        arrow_label = QLabel(self)
        arrow_label.setPixmap(QPixmap('./pictures/arrows.png').scaled(104, 52))
        grid_layout.addWidget(arrow_label, 0, 1, Qt.AlignCenter)

        space_label = QLabel(self)
        space_label.setPixmap(QPixmap('./pictures/space.png').scaled(104, 52))
        grid_layout.addWidget(space_label, 1, 1, Qt.AlignCenter)

        catnip_label = QLabel(self)
        catnip_label.setPixmap(QPixmap('./pictures/catnip.png').scaled(100, 100))
        grid_layout.addWidget(catnip_label, 2, 1, Qt.AlignCenter)

        enemy_label = QLabel(self)
        enemy_label.setPixmap(QPixmap('./pictures/noonoo.png'))
        grid_layout.addWidget(enemy_label, 3, 1, Qt.AlignCenter)

        bucket_label = QLabel(self)
        bucket_label.setPixmap(QPixmap('./pictures/bucket.png'))
        grid_layout.addWidget(bucket_label, 4, 1, Qt.AlignCenter)

        esc_label = QLabel(self)
        esc_label.setPixmap(QPixmap('./pictures/esc.png'))
        grid_layout.addWidget(esc_label, 5, 1, Qt.AlignCenter)

        # Add the descriptions associated with the images for instructions

        arrow_desc = QLabel('Move the character with arrow buttons or A/D', self)
        grid_layout.addWidget(arrow_desc, 0, 2)

        space_desc = QLabel('Jump with space', self)
        grid_layout.addWidget(space_desc, 1, 2)

        catnip_desc = QLabel('This is your goal, find it!', self)
        grid_layout.addWidget(catnip_desc, 2, 2)

        enemy_desc = QLabel('Avoid hitting these from the sides and bottom!', self)
        grid_layout.addWidget(enemy_desc, 3, 2)

        bucket_desc = QLabel('Avoid falling into these!', self)
        grid_layout.addWidget(bucket_desc, 4, 2)

        esc_desc = QLabel('Press Esc to return to main menu at any time', self)
        grid_layout.addWidget(esc_desc, 5, 2)

        grid_layout.addWidget(self.play, 6, 2)

        grid_layout.addWidget(QLabel(''), 6, 0)
        grid_layout.addWidget(QLabel(''), 6, 3)

        self.setLayout(grid_layout)

    def start_game(self):
        self.close()
        self.mainmenu.hide()
        self.mainmenu.scene.view.show()  # Show the scene
        self.mainmenu.scene.timer.start(12, self.mainmenu.scene)
