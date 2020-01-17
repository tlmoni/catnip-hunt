# -*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QGraphicsPixmapItem

from collision import Collision


class Player(QGraphicsPixmapItem):
    """The player class of the game"""

    movement_speed = 4  # pixels/frame
    space = False
    direction = 1
    gravity = 0.5
    jump_velocity = 18
    fall_velocity = 0
    count = 0

    def __init__(self, scene, parent=None):
        QGraphicsPixmapItem.__init__(self, parent)
        self.setPixmap(QPixmap('./pictures/cat.png'))
        self.scene = scene            # Add player's scene
        self.collision = Collision()  # Apply collision detection
        self.collideable = True

    def jump(self):
        """The jump action of the player, executes an upward movement with decreasing velocity."""

        if self.collision.check_over_collision(self.scene, self):
            Player.jump_velocity = 0
            Player.fall_velocity = 0

        elif Player.count < 37:  # velocity - gravity * x = 0, -> x = 36
            self.setY(self.y() - Player.jump_velocity)
            Player.jump_velocity -= Player.gravity  # Decrease velocity with gravity
            Player.count += 1

    def update(self, keys_pressed):
        """Update the game situation from the player's perspective."""

        delta_x = 0  # Change of x-coordinate

        if Qt.Key_Escape in self.scene.keys_pressed:
            self.scene.timer.stop()  # Freeze the game timer
            self.scene.mainmenu.show()
            self.scene.mainmenu.main_menu()
            self.scene.view.close()

        if Qt.Key_Right in self.scene.keys_pressed or Qt.Key_D in self.scene.keys_pressed:
            delta_x += Player.movement_speed  # Change x-coordinate by 1 unit of movement speed towards right

            Player.direction = 1

            if self.x() + 64 + delta_x > self.scene.x:  # Right side limit of the screen for player-object (64*64)
                pass  # Prevents further movement to left when player is at the edge of the screen
            elif self.collision.check_right_collision(self.scene, self):
                pass
            else:
                self.setX(self.x() + delta_x)

        elif Qt.Key_Left in self.scene.keys_pressed or Qt.Key_A in self.scene.keys_pressed:
            delta_x -= Player.movement_speed  # Change x-coordinate by 1 unit of movement speed towards left

            Player.direction = -1

            if self.x() <= 0:  # Left side limit of the screen for player-object (64*64)
                pass           # Prevents further movement to left when player is at the edge of the screen
            elif self.collision.check_left_collision(self.scene, self):
                pass
            else:
                self.setX(self.x() + delta_x)

        if Qt.Key_Space in keys_pressed:
            Player.space = True  # Initiates jump()
            items = self.collidingItems()
            for item in items:
                if item is self.scene.pipe and item is not None:
                    Player.space = False

        if Player.space:
            self.jump()  # Execute jump()

        if self.collision.catnip_collision(self.scene, self):
            self.scene.victory()

        if self.collision.bucket_collision(self.scene, self):
            self.scene.loss()

        if self.collision.enemy_collision(self.scene, self):
            Player.jump_velocity = 0
            Player.fall_velocity = 0
            self.scene.loss()

        if self.y() > self.scene.y:
            self.scene.loss()

        if self.collision.check_under_collision(self.scene, self):
            Player.fall_velocity = 0  # Stops the player from falling when it hits the ground
            Player.count = 0
            Player.jump_velocity = 18
            Player.space = False

            if Player.direction > 0:
                if Qt.Key_Down in self.scene.keys_pressed or Qt.Key_S in self.scene.keys_pressed:
                    self.setPixmap(QPixmap('./pictures/cat_down.png'))
                else:
                    self.setPixmap(QPixmap('./pictures/cat.png'))
            elif Player.direction < 0:
                if Qt.Key_Down in self.scene.keys_pressed or Qt.Key_S in self.scene.keys_pressed:
                    self.setPixmap(QPixmap('./pictures/cat_down_flip.png'))
                else:
                    self.setPixmap(QPixmap('./pictures/cat_flip.png'))

        else:
            if Player.direction > 0:
                self.setPixmap(QPixmap('./pictures/cat_jump.png'))
            elif Player.direction < 0:
                self.setPixmap(QPixmap('./pictures/cat_jump_flip.png'))

            self.setY(self.y() + Player.fall_velocity)
            if Player.fall_velocity < 18:
                Player.fall_velocity += Player.gravity
            else:
                Player.fall_velocity = 18
