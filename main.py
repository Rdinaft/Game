import pyglet
from constants import TICKRATE
from resources import anchoring_list
from player import CAT_CHARACTER, CAT_BATCH
from window import WINDOW
from walls import create_primary_walls, WALL_BATCH, PRIMARY_WALL_LIST
from floor import FLOOR_BATCH, create_floor
from created_walls import CREATED_WALLS_BATCH, place_new_walls


create_primary_walls()
place_new_walls(10, 20)
anchoring_list(PRIMARY_WALL_LIST)
create_floor()


def update(dt):
    CAT_CHARACTER.update(dt)


@WINDOW.event
def on_draw():
    WINDOW.clear()
    FLOOR_BATCH.draw()
    WALL_BATCH.draw()
    CREATED_WALLS_BATCH.draw()
    CAT_BATCH.draw()


if __name__ == "__main__":
    pyglet.clock.schedule_interval(update, TICKRATE)
    pyglet.app.run()
