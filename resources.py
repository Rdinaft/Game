import pyglet
from constants import RESOURCES_PATH


pyglet.resource.path = RESOURCES_PATH
pyglet.resource.reindex()


def img_source(image):
    return pyglet.resource.image(image)


def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


def anchoring_list(images_list):
    for image in images_list:
        return center_image(image)


def cat_set_image():
    cat_image = img_source("cat1.png")
    center_image(cat_image)
    return cat_image


def upper_walls():
    return [
        img_source("w1.png"),
        img_source("w2.png"),
        img_source("w3.png"),
        img_source("w4.png"),
        img_source("w5.png"),
        img_source("w6.png"),
    ]


def bottom_walls():
    return [
        img_source("wb1.png"),
        img_source("wb2.png"),
        img_source("wb3.png"),
        img_source("wb4.png"),
        img_source("wb5.png"),
        img_source("wb6.png"),
    ]


def left_walls():
    return [
        img_source("wl1.png"),
        img_source("wl2.png"),
        img_source("wl3.png"),
        img_source("wl4.png"),
    ]


def right_walls():
    return [
        img_source("wr1.png"),
        img_source("wr2.png"),
        img_source("wr3.png"),
        img_source("wr4.png"),
    ]


def floor():
    floor = img_source("floor.png")
    center_image(floor)
    return floor

def fish_food():
    fish = img_source("fish.png")
    center_image(fish)
    return fish