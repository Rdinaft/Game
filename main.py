import pyglet
from constants import TICKRATE
from player import MAIN_CHARACTER, MAIN_BATCH
from resources import wall_list, anchoring_list
from window import WINDOW
from walls import create_walls, WALL_BATCH
from floor import FLOOR_BATCH, create_floor


create_walls(wall_list)
anchoring_list(wall_list)
create_floor()

def update(dt):
    MAIN_CHARACTER.update(dt)

@WINDOW.event
def on_draw():
    WINDOW.clear()
    FLOOR_BATCH.draw()
    WALL_BATCH.draw()
    MAIN_BATCH.draw()

    
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, TICKRATE)
    pyglet.app.run()
