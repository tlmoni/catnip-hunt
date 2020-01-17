# -*- coding: utf-8 -*-

from PyQt5.QtGui import QPixmap

from item import Item
from player import Player


class LevelLoader:
    """Reads the input level file and applies the described level structure based on the file."""

    def __init__(self, scene):
        self.scene = scene

    def load_game(self, input):
        """Method for reading the input file as a game level and adding the interpreted items to the graphics scene."""
        x = 0
        y = 0
        player = None
        catnip = None
        mega_noonoo = None
        pipe = None
        current_line = ''

        try:
            file = open(input, 'r')
            while True:

                current_line = file.readline()  # Read the next line in the file

                if current_line == '':  # End of the file
                    if mega_noonoo:
                        self.scene.add_mega(mega_noonoo)
                    if player is None:
                        file.close()
                        raise Exception('Missing player in level file!')
                    if catnip is None:
                        file.close()
                        raise Exception('Missing goal in level file!')

                    self.scene.add_player(player)
                    start_x = player.x()  # X-coordinate of the starting point
                    start_y = player.y()  # Y-coordinate of the starting point
                    if pipe:
                        self.scene.add_pipe(pipe)
                    file.close()
                    return x, y, start_x, start_y  # Return width, height and the coordinate values

                else:
                    current_line = current_line.strip().lower()  # Strip and lower the line

                if current_line == '':  # Empty line (i.e. \n)
                    pass

                elif current_line == '/map':  # Map chunk of the file starts

                    while True:
                        current_line = file.readline()

                        if current_line.startswith('/'):
                            break

                        elif current_line == '':
                            break

                        else:
                            current_line = current_line.strip()

                            if current_line == '':
                                pass
                            else:
                                current_line = current_line.split('-')  # Split the line for graphics item analysing
                                x = 0
                                for item in current_line:

                                    if item == 'P':  # Player
                                        player = Player(self.scene)
                                        player.setPos(x, y)

                                    elif item == 'X':  # Goal (catnip), X marks the spot
                                        catnip = Item(True, 0, False, False)
                                        catnip.setPos(x-32, y-64)
                                        catnip.setPixmap(QPixmap('./pictures/catnip.png'))
                                        catnip.setScale(2)
                                        self.scene.add_catnip(catnip)

                                    elif item == 'E':  # Enemy
                                        enemy = Item(True, -2, False, True)
                                        enemy.setPos(x, y)
                                        enemy.setPixmap(QPixmap('./pictures/noonoo_square.png'))
                                        self.scene.enemies.append(enemy)
                                        self.scene.addItem(enemy)

                                    elif item == 'F':  # Flying enemy
                                        enemy = Item(True, -2, True, True)
                                        enemy.setPos(x, y)
                                        enemy.setPixmap(QPixmap('./pictures/noonoo_flying.png'))
                                        self.scene.enemies.append(enemy)
                                        self.scene.addItem(enemy)

                                    elif item == 'M':
                                        mega_noonoo = Item(True, 2, False, True)
                                        mega_noonoo.setPos(x, y)
                                        mega_noonoo.setPixmap(QPixmap('./pictures/mega_noonoo.png'))
                                        mega_noonoo.setScale(6)

                                    elif item == 'B':  # Bucket element
                                        bucket = Item(True, 0, False, False)
                                        bucket.setPos(x, y)
                                        bucket.setPixmap(QPixmap('./pictures/bucket_square.png'))
                                        self.scene.buckets.append(bucket)
                                        self.scene.addItem(bucket)

                                    elif item == 'C':  # Crate element
                                        crate = Item(True, 0, False, False)
                                        crate.setPos(x, y)
                                        crate.setPixmap(QPixmap('./pictures/crate.png'))
                                        self.scene.addItem(crate)

                                    elif item == 'c':  # Cloud element
                                        cloud = Item(False, 0, False, False)
                                        cloud.setPos(x, y)
                                        cloud.setPixmap(QPixmap('./pictures/cloud.png'))
                                        self.scene.addItem(cloud)

                                    elif item == 'p':  # Pipe element
                                        pipe = Item(False, 0, False, False)
                                        pipe.setPos(x, y)
                                        pipe.setPixmap(QPixmap('./pictures/pipe.png'))

                                    elif item == 'g':  # Ground element
                                        ground = Item(True, 0, False, False)
                                        ground.setPos(x, y)
                                        ground.setPixmap(QPixmap('./pictures/ground.png'))
                                        self.scene.addItem(ground)

                                    elif item == 'f':  # Floor element
                                        floor = Item(True, 0, False, False)
                                        floor.setPos(x, y)
                                        floor.setPixmap(QPixmap('./pictures/floor_decorated.png'))
                                        self.scene.addItem(floor)

                                    x += 64
                        y += 64

        except OSError:
            file.close()
            raise Exception('Reading the data failed!')
