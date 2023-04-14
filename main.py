import pyglet
from constants import TICKRATE
from resources import anchoring_list
from player import cat_character
from window import WINDOW
from walls import create_primary_walls, WALL_BATCH, PRIMARY_WALL_LIST
from floor import FLOOR_BATCH, create_floor
from created_walls import CREATED_WALLS_BATCH, place_new_walls
from fish import place_fish, score_count, score_label


def update(dt):
    cat.update(dt)


@WINDOW.event
def on_draw():
    WINDOW.clear()
    FLOOR_BATCH.draw()
    cat_batch.draw()
    WALL_BATCH.draw()
    CREATED_WALLS_BATCH.draw()
    fish_batch.draw()
    score_label(score_count(cat, fish)).draw()


if __name__ == "__main__":
    create_primary_walls()
    place_new_walls(10, 20)
    anchoring_list(PRIMARY_WALL_LIST)
    fish, fish_batch = place_fish()
    cat, cat_batch = cat_character()
    all_floor = create_floor()
    pyglet.clock.schedule_interval(update, TICKRATE)
    pyglet.app.run()
