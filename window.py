import pyglet
import random
from resources import left_walls, upper_walls
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME


def sprites_per_window_x(sprite):
    return WINDOW_WIDTH // sprite.width


def sprites_per_window_y(sprite):
    return WINDOW_HEIGHT // sprite.height


WINDOW = pyglet.window.Window(
    width=sprites_per_window_x(upper_walls()[0]) * upper_walls()[0].width
    + left_walls()[0].width * 2,
    height=sprites_per_window_y(left_walls()[0]) * left_walls()[0].height,
)

WINDOW.set_caption(random.choice(GAME_NAME))

WINDOW.set_icon(pyglet.resource.image("cat_lick1.png"))
