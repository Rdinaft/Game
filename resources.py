import pyglet
from constants import RESOURCES_PATH


def reindex_resources_path():
    pyglet.resource.path = RESOURCES_PATH
    pyglet.resource.reindex()

def img_source(image):
    img = pyglet.resource.image('' + image)
    return img

def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2

def anchoring_list(list_name):
    for i in list_name:
        return center_image(i)

reindex_resources_path()

cat_character_image = img_source('cat1.png')
center_image(cat_character_image)
    
walls_top = [img_source('w1.png'), img_source('w2.png'), img_source('w3.png'), img_source('w4.png'), img_source('w5.png'), img_source('w6.png')]
walls_bot = [img_source('wb1.png'), img_source('wb2.png'), img_source('wb3.png'), img_source('wb4.png'), img_source('wb5.png'), img_source('wb6.png')]
walls_left = [img_source('wl1.png'), img_source('wl2.png'), img_source('wl3.png'), img_source('wl4.png')]
walls_right = [img_source('wr1.png'), img_source('wr2.png'), img_source('wr3.png'), img_source('wr4.png')]

primary_wall_list = []

floor = img_source('floor.png')
center_image(floor)

all_floor = []
