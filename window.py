import pyglet
from resources import walls_top, walls_left
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


def sprites_per_window_x(sprite):
    return WINDOW_WIDTH // sprite.width

def sprites_per_window_y(sprite):
    return WINDOW_HEIGHT // sprite.height

window = pyglet.window.Window(width = sprites_per_window_x(walls_top[0]) * walls_top[0].width + walls_left[0].width * 2, height = sprites_per_window_y(walls_left[0]) * walls_left[0].height)

window.set_caption('Cat Tale')

window.set_icon(pyglet.resource.image('cat1.png'))
