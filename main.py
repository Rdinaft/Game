import pyglet
from constants import TICKRATE
from player import main_character
from resources import wall_batch, main_batch, wall_list
from window import window
from walls import create_walls


create_walls(wall_list)

def update(dt):
    main_character.update(dt)

@window.event
def on_draw():
    window.clear()
    wall_batch.draw()
    main_batch.draw()

    
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, TICKRATE)
    pyglet.app.run()
