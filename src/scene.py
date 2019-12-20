#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from level_loader import LevelLoader
from collision import Collision
from victory import Victory
from loss import Loss

__author__ = 'Toni Ojala'


SCREEN_WIDTH = 1600  # pixels
SCREEN_HEIGHT = 896  # pixels
FRAME_TIME = 12      # ms/frame, adjusted to get a smooth refresh rate


class Scene(QGraphicsScene):
    """Graphics scene of the game, holding all the graphic objects and functions as the core frame."""

    def __init__(self, mainmenu, level, parent=None):
        QGraphicsScene.__init__(self, parent)

        self.keys_pressed = set()   # Set of keys pressed
        self.timer = QBasicTimer()  # Using a timer to set refresh rate
        self.collision = Collision()
        self.level_loader = LevelLoader(self)

        self.mainmenu = mainmenu  # Link the scene to the main menu
        self.view = None
        self.level = level
        self.player = None
        self.catnip = None
        self.mega = None
        self.pipe = None
        self.enemies = []
        self.buckets = []
        self.x = 0
        self.y = 0
        self.start_x = 0
        self.start_y = 0
        self.animation_timer = 0

        self.set_up()

    def set_up(self):
        """Set up the scene"""
        self.x, self.y, self.start_x, self.start_y = self.level_loader.load_game(self.level)
        self.setBackgroundBrush(QBrush(QColor(227, 0, 77)))  # Set background for the scene

        self.view = QGraphicsView(self)
        self.view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Toggle scroll bar off
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)    # Toggle scroll bar off
        self.view.setWindowTitle('Catnip Hunt')
        self.view.setWindowIcon(QIcon('./pictures/cat.png'))

        self.view.move(160, 60)
        self.view.centerOn(self.player.pos())

        self.view.setFixedSize(SCREEN_WIDTH + 2, SCREEN_HEIGHT + 2)  # Window zoom size
        self.setSceneRect(0, 0, self.x, self.y)                      # Scene size

    def keyPressEvent(self, event):
        self.keys_pressed.add(event.key())

    def keyReleaseEvent(self, event):
        self.keys_pressed.remove(event.key())

    def timerEvent(self, event):
        self.scene_update()  # Update scene
        self.update()        # Update game

    def scene_update(self):
        self.mega_update()
        self.enemy_update()
        self.player.update(self.keys_pressed)  # Update player location
        self.view.centerOn(self.player.pos())  # Center camera

    def mega_update(self):  # Update Mega Noonoo location and image (animation)
        if self.mega is not None:
            self.mega.setX(self.mega.x() + self.mega.movement)
            if self.animation_timer == 100:
                self.mega.setPixmap(QPixmap('./pictures/mega_noonoo.png'))
            elif self.animation_timer >= 50:
                self.mega.setPixmap(QPixmap('./pictures/mega_noonoo_flap.png'))

    def enemy_update(self):  # Update enemy locations and images (animation)
        for enemy in self.enemies:
            self.enemy_image_animation(enemy)

            if self.collision.enemy_movement_collision(self, enemy):
                enemy.movement = enemy.movement * -1
                self.enemy_image_animation(enemy)
            enemy.setX(enemy.x() + enemy.movement)
        self.animation_timer += 1

    def enemy_image_animation(self, enemy):
        if enemy.movement > 0:
            if enemy.flying:
                if self.animation_timer == 100:
                    enemy.setPixmap(QPixmap('./pictures/noonoo_flying_flip.png'))
                    self.animation_timer = 0
                elif self.animation_timer >= 50:
                    enemy.setPixmap(QPixmap('./pictures/noonoo_flying_flap_flip.png'))
                else:
                    enemy.setPixmap(QPixmap('./pictures/noonoo_flying_flip.png'))
            else:
                enemy.setPixmap(QPixmap('./pictures/noonoo_square_flip.png'))

        elif enemy.movement < 0:
            if enemy.flying:
                if self.animation_timer == 100:
                    enemy.setPixmap(QPixmap('./pictures/noonoo_flying.png'))
                    self.animation_timer = 0
                elif self.animation_timer >= 50:
                    enemy.setPixmap(QPixmap('./pictures/noonoo_flying_flap.png'))
                else:
                    enemy.setPixmap(QPixmap('./pictures/noonoo_flying.png'))
            else:
                enemy.setPixmap(QPixmap('./pictures/noonoo_square.png'))

    def add_player(self, player):
        self.player = player
        self.addItem(self.player)

    def add_catnip(self, catnip):
        self.catnip = catnip
        self.addItem(self.catnip)

    def add_mega(self, mega):
        self.mega = mega
        self.addItem(self.mega)

    def add_pipe(self, pipe):
        self.pipe = pipe
        self.addItem(self.pipe)

    def loss(self):
        self.timer.stop()                   # Freeze the game timer
        pos = self.view.mapToScene(0, -16)  # Get the position of the proxy widget
        loss = Loss(self.mainmenu)
        loss.move(pos.toPoint())            # Set the position of the widget
        self.addWidget(loss, Qt.Widget)

    def victory(self):
        self.timer.stop()
        pos = self.view.mapToScene(0, -16)
        victory = Victory(self.mainmenu)
        victory.move(pos.toPoint())
        self.addWidget(victory, Qt.Widget)
