import pyglet
import random
from pyglet.sprite import Sprite
from resources import walls_top, walls_left, walls_right, walls_bot
from window import window, sprites_per_window_x, sprites_per_window_y


wall_batch = pyglet.graphics.Batch()

def create_walls(walls):
    vert_wall = walls_left[0]
    horiz_wall = walls_top[0]
    for x in range(int(sprites_per_window_x(horiz_wall))):
        top_walls = Sprite(random.choice(walls_top), x = x * horiz_wall.width + vert_wall.width, y = window.height - horiz_wall.height, batch = wall_batch)
        bot_walls = Sprite(random.choice(walls_bot), x = x * horiz_wall.width + vert_wall.width, y = 0, batch = wall_batch)
        walls += top_walls, bot_walls
    for y in range(int(sprites_per_window_y(vert_wall))):
        left_walls = Sprite(random.choice(walls_left), x = 0, y = y * vert_wall.height, batch = wall_batch)
        right_walls = Sprite(random.choice(walls_right), x = window.width - vert_wall.width, y = y * vert_wall.height, batch = wall_batch)
        walls += left_walls, right_walls
