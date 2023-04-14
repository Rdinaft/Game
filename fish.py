import pyglet
import random
from resources import fish_food
from window import WINDOW
from collision_check import are_objects_collided


def score_count(eater, food):
    score = 0
    if are_objects_collided(eater, food):
        place_fish()
        score += 1
    return score


def score_label(score):
    return pyglet.text.Label(text="Score: " + str(score), x=10, y=575)


def place_fish():
    fish_batch = pyglet.graphics.Batch()
    fish = pyglet.sprite.Sprite(
        fish_food(),
        x=random.randint(0, WINDOW.width),
        y=random.randint(0, WINDOW.height),
        batch=fish_batch,
    )
    return fish, fish_batch
