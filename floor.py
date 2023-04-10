import pyglet
from resources import FLOOR, WALLS_BOT, WALLS_LEFT
from pyglet.sprite import Sprite
from window import sprites_per_window_x, sprites_per_window_y
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


FLOOR_BATCH = pyglet.graphics.Batch()
ALL_FLOOR = []


def create_floor():
    if (
        float((WINDOW_WIDTH - FLOOR.width // 2) / FLOOR.width).is_integer()
        or float((WINDOW_HEIGHT - FLOOR.height // 2) / FLOOR.height).is_integer()
    ):
        tolerance = 1
    else:
        tolerance = 0

    for y in range(int(sprites_per_window_y(FLOOR) + tolerance)):
        for x in range(int(sprites_per_window_x(FLOOR) + tolerance)):
            ALL_FLOOR.append(
                Sprite(
                    img=FLOOR,
                    x=x * FLOOR.width + FLOOR.width // 2 + WALLS_LEFT[0].width,
                    y=y * FLOOR.height + FLOOR.height // 2 + WALLS_BOT[0].height,
                    batch=FLOOR_BATCH,
                )
            )
