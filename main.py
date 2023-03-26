import pyglet
from pyglet import shapes
from pyglet.window import key

window = pyglet.window.Window(width=900, height=500)
window.set_caption('Tales')
pyglet.resource.path = ['game/resources']
pyglet.resource.reindex()
window.set_icon(pyglet.resource.image('cat1.png'))
main_batch = pyglet.graphics.Batch()
main_character_image = pyglet.resource.image('cat1.png')
wall_left = shapes.Line(10, 10, 10, window.height-10, width=5, batch=main_batch)
wall_right = shapes.Line(window.width-10, 10, window.width-10, window.height-10, width=5, batch=main_batch)
wall_top = shapes.Line(10, window.height-10, window.width-10, window.height-10, width=5, batch=main_batch)
wall_bot = shapes.Line(10, 10, window.width-10, 10, width=5, batch=main_batch)

class PhysicalObjects(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObjects, self).__init__(*args, **kwargs)


class Player(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=main_character_image, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
    def update(self, dt):
        walk = 5
        if self.key_handler[key.A]:
            self.x -= walk
        if self.key_handler[key.D]:
            self.x += walk
        if self.key_handler[key.S]:
            self.y -= walk
        if self.key_handler[key.W]:
            self.y += walk    

main_character = Player(x=window.width//2, y=window.height//2, batch=main_batch)

window.push_handlers(main_character.key_handler)

def update(dt):
    main_character.update(dt)

@window.event
def on_draw():
    window.clear()
    main_batch.draw()

    
    
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)
    pyglet.app.run()

# 1. Вывести окно --done
        # Добавить название --done
        # Сделать иконку --done
# 2. Вывести персонажа в центре --done
# 3. Получить управление над персонажем --done
# 4. Сделать комнату
#
#
#