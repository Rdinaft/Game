import pyglet
import random
from pyglet.sprite import Sprite
from resources import left_walls, upper_walls, bottom_walls, right_walls
from window import WINDOW, sprites_per_window_x, sprites_per_window_y


WALL_BATCH = pyglet.graphics.Batch()
PRIMARY_WALL_LIST = []


def create_primary_walls():
    vert_wall = left_walls()[0]
    horiz_wall = upper_walls()[0]
    wall_list = []
    for x in range(int(sprites_per_window_x(horiz_wall))):
        top_wall = Sprite(
            random.choice(upper_walls()),
            x=x * horiz_wall.width + vert_wall.width,
            y=WINDOW.height - horiz_wall.height,
            batch=WALL_BATCH,
        )
        bot_wall = Sprite(
            random.choice(bottom_walls()),
            x=x * horiz_wall.width + vert_wall.width,
            y=0,
            batch=WALL_BATCH,
        )
        wall_list += top_wall, bot_wall
    for y in range(int(sprites_per_window_y(vert_wall))):
        left_wall = Sprite(
            random.choice(left_walls()), x=0, y=y * vert_wall.height, batch=WALL_BATCH
        )
        right_wall = Sprite(
            random.choice(right_walls()),
            x=WINDOW.width - vert_wall.width,
            y=y * vert_wall.height,
            batch=WALL_BATCH,
        )
        wall_list += left_wall, right_wall
    for wall in wall_list:
        PRIMARY_WALL_LIST.append(wall)
