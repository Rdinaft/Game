import pyglet
from resources import walls_top, walls_left
from constants import WINDOW_WIDTH, WINDOW_HEIGHT


sprite_times_x = WINDOW_WIDTH // walls_top[0].width
sprite_times_y = WINDOW_HEIGHT // walls_left[0].height
window = pyglet.window.Window(width = sprite_times_x * walls_top[0].width + walls_left[0].width * 2, height = sprite_times_y * walls_left[0].height)

window.set_caption('Cat Tale')

window.set_icon(pyglet.resource.image('cat1.png'))