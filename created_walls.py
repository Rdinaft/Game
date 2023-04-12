import pyglet
import random
from resources import bottom_walls, upper_walls, left_walls, right_walls
from window import WINDOW


CREATED_WALLS_BATCH = pyglet.graphics.Batch()
CREATED_WALLS = []


def create_secondary_walls(x, y, image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    CREATED_WALLS.append(
        pyglet.sprite.Sprite(image, x=x, y=y, batch=CREATED_WALLS_BATCH)
    )


def place_new_walls(min_amount, max_amount):
    walls_sprites = bottom_walls() + upper_walls() + left_walls() + right_walls()
    for wall in range(min_amount, max_amount):
        create_secondary_walls(
            random.randint(0, WINDOW.width),
            random.randint(0, WINDOW.height),
            random.choice(walls_sprites),
        )
