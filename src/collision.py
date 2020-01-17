# -*- coding: utf-8 -*-

from PyQt5.Qt import QTransform
from PyQt5.QtCore import QPointF


class Collision:
    """
    Collision detection class
    Main features:
    - Collision detection with any object in all 4 directions
    - Collision detection with important objects
    """

    def __init__(self):
        self.transform = QTransform()

    def catnip_collision(self, scene, player):
        """Check if the player collides with catnip aka the goal"""
        if player.collidesWithItem(scene.catnip):
            return True
        return False

    def enemy_collision(self, scene, player):
        """Check if the player collides with an enemy"""
        item_top_left = scene.itemAt(player.pos() + QPointF(10, 3), self.transform)       # Left top corner
        item_bottom_left = scene.itemAt(player.pos() + QPointF(10, 59), self.transform)   # Left bottom corner
        item_top_right = scene.itemAt(player.pos() + QPointF(52, 3), self.transform)      # Right top corner
        item_bottom_right = scene.itemAt(player.pos() + QPointF(52, 59), self.transform)  # Right bottom corner

        # Check if the player collides with a normal enemy
        if item_top_left in scene.enemies or item_bottom_left in scene.enemies or item_top_right in scene.enemies or item_bottom_right in scene.enemies:
            return True
        # Check if the player collides with the mega Noonoo
        elif scene.mega:
            if item_top_left is scene.mega or item_bottom_left is scene.mega or item_top_right is scene.mega or item_bottom_right is scene.mega:
                return True
        return False

    def bucket_collision(self, scene, player):
        """Check if the player collides with a bucket under it"""
        item_under = scene.itemAt(player.pos() + QPointF(32, 65), self.transform)

        if item_under in scene.buckets:
            return True
        return False

    def check_left_collision(self, scene, player):
        """Check if the player collides with an item towards left of it"""
        item_top_left = scene.itemAt(player.pos() + QPointF(12, 0), self.transform)      # Left top corner
        item_bottom_left = scene.itemAt(player.pos() + QPointF(12, 63), self.transform)  # Left bottom corner

        try:
            if item_top_left:
                if item_top_left.collideable:
                    difference = item_top_left.x() - player.x()
                    if difference > -4:  # If difference is less than movement per frame, move character to the edge.
                        player.setPos(player.pos() + QPointF(-difference, 0))
                    return True

            elif item_bottom_left:
                if item_bottom_left.collideable:
                    difference = item_bottom_left.x() - player.x()
                    if difference > -4:  # If difference is less than movement per frame, move character to the edge.
                        player.setPos(player.pos() + QPointF(difference, 0))
                    return True

            else:
                player.setPos(player.pos())
                return False

        except AttributeError:
            return False

    def check_right_collision(self, scene, player):
        """Check if the player collides with an item towards right of it"""
        item_top_right = scene.itemAt(player.pos() + QPointF(50, 0), self.transform)      # Right top corner
        item_bottom_right = scene.itemAt(player.pos() + QPointF(50, 63), self.transform)  # Right bottom corner

        try:
            if item_top_right:
                if item_top_right.collideable:
                    difference = item_top_right.x() - player.x()
                    if difference < -4:  # If difference is less than movement per frame, move character to the edge.
                        player.setPos(player.pos() + QPointF(-difference, 0))
                    return True

            elif item_bottom_right:
                if item_bottom_right.collideable:
                    difference = item_bottom_right.x() - player.x()
                    if difference < -4:  # If difference is less than movement per frame, move character to the edge.
                        player.setPos(player.pos() + QPointF(-difference, 0))
                    return True

            else:
                player.setPos(player.pos())
                return False

        except AttributeError:
            return False

    def check_under_collision(self, scene, player):
        """Check if the player collides with an item under it"""
        item_under_left = scene.itemAt(player.pos() + QPointF(16, 64 + player.fall_velocity), self.transform)
        item_under_right = scene.itemAt(player.pos() + QPointF(46, 64 + player.fall_velocity), self.transform)
        dx = 0

        try:
            if item_under_left is scene.pipe or item_under_right is scene.pipe:
                if player.y() + 64 >= scene.pipe.y():
                    player.setY(scene.pipe.y() - 64)
                    player.jump_velocity = 0
                    return True
                return False

            if item_under_right in scene.enemies:
                if item_under_right.movement > 0:
                    if not self.check_right_collision(scene, player):
                        player.setX(player.x() + item_under_right.movement)
                if item_under_right.movement < 0:
                    if not self.check_left_collision(scene, player):
                        player.setX(player.x() + item_under_right.movement)

            elif item_under_left in scene.enemies:
                if item_under_left.movement > 0:
                    if not self.check_right_collision(scene, player):
                        player.setX(player.x() + item_under_left.movement)
                if item_under_left.movement < 0:
                    if not self.check_left_collision(scene, player):
                        player.setX(player.x() + item_under_left.movement)

            if item_under_right is scene.mega and scene.mega is not None:
                if not self.check_right_collision(scene, player):
                    dx = scene.mega.movement

            elif item_under_left is scene.mega and scene.mega is not None:
                if not self.check_left_collision(scene, player):
                    dx = scene.mega.movement

            player.setX(player.x() + dx)

            if item_under_right:
                if item_under_right.collideable:
                    player.setY(item_under_right.y() - 64)
                    player.jump_velocity = 0
                    return True

            elif item_under_left:
                if item_under_left.collideable:
                    player.setY(item_under_left.y() - 64)
                    player.jump_velocity = 0
                    return True

            else:
                return False

        except AttributeError:
            return False

    def check_over_collision(self, scene, player):
        """Check if the player collides with an item on top of it"""
        item_over_left = scene.itemAt(player.pos() + QPointF(16, - player.jump_velocity), self.transform)
        item_over_right = scene.itemAt(player.pos() + QPointF(46, - player.jump_velocity), self.transform)

        try:
            if item_over_right:
                if item_over_right.collideable:
                    player.jump_velocity = 0
                    player.setY(item_over_right.y() + 64)
                    return True

            elif item_over_left:
                if item_over_left.collideable:
                    player.jump_velocity = 0
                    player.setY(item_over_left.y() + 64)
                    return True

            else:
                return False

        except AttributeError:
            return False

    def enemy_movement_collision(self, scene, enemy):
        """Check if an enemy collides with something on the left or right"""
        item_left = scene.itemAt(enemy.pos() + QPointF(-1, 32), self.transform)   # Left top corner
        item_right = scene.itemAt(enemy.pos() + QPointF(65, 32), self.transform)  # Right top corner

        if item_left:
            if item_left.collideable:
                return True
        if item_right:
            if item_right.collideable:
                return True
        return False
