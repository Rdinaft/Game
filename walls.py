import pyglet
import random
from pyglet.sprite import Sprite
from resources import WALLS_LEFT, WALLS_TOP, WALLS_BOT, WALLS_RIGHT
from window import WINDOW, sprites_per_window_x, sprites_per_window_y


WALL_BATCH = pyglet.graphics.Batch()
PRIMARY_WALL_LIST = []


def create_primary_walls():
    vert_wall = WALLS_LEFT[0]
    horiz_wall = WALLS_TOP[0]
    wall_list = []
    for x in range(int(sprites_per_window_x(horiz_wall))):
        top_walls = Sprite(
            random.choice(WALLS_TOP),
            x=x * horiz_wall.width + vert_wall.width,
            y=WINDOW.height - horiz_wall.height,
            batch=WALL_BATCH,
        )
        bot_walls = Sprite(
            random.choice(WALLS_BOT),
            x=x * horiz_wall.width + vert_wall.width,
            y=0,
            batch=WALL_BATCH,
        )
        wall_list += top_walls, bot_walls
    for y in range(int(sprites_per_window_y(vert_wall))):
        left_walls = Sprite(
            random.choice(WALLS_LEFT), x=0, y=y * vert_wall.height, batch=WALL_BATCH
        )
        right_walls = Sprite(
            random.choice(WALLS_RIGHT),
            x=WINDOW.width - vert_wall.width,
            y=y * vert_wall.height,
            batch=WALL_BATCH,
        )
        wall_list += left_walls, right_walls
    for wall in wall_list:
        PRIMARY_WALL_LIST.append(wall)
