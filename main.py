import pyglet
from constants import TICKRATE
from player import CAT_CHARACTER, CAT_BATCH
from resources import primary_wall_list, anchoring_list
from window import WINDOW
from walls import create_primary_walls, WALL_BATCH
from floor import FLOOR_BATCH, create_floor


create_primary_walls()
anchoring_list(primary_wall_list)
create_floor()

def update(dt):
    CAT_CHARACTER.update(dt)

@WINDOW.event
def on_draw():
    WINDOW.clear()
    FLOOR_BATCH.draw()
    WALL_BATCH.draw()
    CAT_BATCH.draw()

    
if __name__ == '__main__':   
    pyglet.clock.schedule_interval(update, TICKRATE)
    pyglet.app.run()
