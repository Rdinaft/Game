import pyglet
import random
from resources import WALLS_BOT, WALLS_LEFT, WALLS_RIGHT, WALLS_TOP
from window import WINDOW


CREATED_WALLS_BATCH = pyglet.graphics.Batch()
CREATED_WALLS = []

WALLS_SPRITES = WALLS_BOT + WALLS_LEFT + WALLS_RIGHT + WALLS_TOP


def create_secondary_walls(x, y, image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    CREATED_WALLS.append(pyglet.sprite.Sprite(image, x=x, y=y, batch=CREATED_WALLS_BATCH))


def place_new_walls(min_amount, max_amount):
    for wall in range(min_amount, max_amount):
        create_secondary_walls(random.randint(0, WINDOW.width), random.randint(0, WINDOW.height), random.choice(WALLS_SPRITES))
