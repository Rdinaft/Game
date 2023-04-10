import pyglet
import random
from resources import WALLS_LEFT, WALLS_TOP
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, GAME_NAME


def sprites_per_window_x(sprite):
    return WINDOW_WIDTH // sprite.width


def sprites_per_window_y(sprite):
    return WINDOW_HEIGHT // sprite.height


WINDOW = pyglet.window.Window(
    width=sprites_per_window_x(WALLS_TOP[0]) * WALLS_TOP[0].width
    + WALLS_LEFT[0].width * 2,
    height=sprites_per_window_y(WALLS_LEFT[0]) * WALLS_LEFT[0].height,
)

WINDOW.set_caption(random.choice(GAME_NAME))

WINDOW.set_icon(pyglet.resource.image("cat_lick1.png"))
