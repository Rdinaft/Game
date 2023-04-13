import pyglet
import random
from resources import fish_food
from window import WINDOW
from collision_check import are_objects_collided


def create_counter():
    score = 0
    main_batch = pyglet.graphics.Batch()
    score_label = pyglet.text.Label(text="Score: " + str(score), x=10, y=575, batch=main_batch)
    return main_batch, score_label


def place_fish():
    fish_batch = pyglet.graphics.Batch()
    fish = pyglet.sprite.Sprite(fish_food(), x=random.randint(0, WINDOW.width), y=random.randint(0, WINDOW.height), batch=fish_batch)
    return fish, fish_batch


def eat_fish(eater, food):
    if are_objects_collided(eater, food):
        print(are_objects_collided(eater, food))
        place_fish()
