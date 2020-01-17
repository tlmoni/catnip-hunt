# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGraphicsPixmapItem


class Item(QGraphicsPixmapItem):
    """Class for graphics items in the game, holding the most important parameters"""
    def __init__(self, collideable, movement, flying, friction, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.collideable = collideable
        self.movement = movement
        self.flying = flying
        self.friction = friction
