import pyglet

from pyglet.gl import *
from pyglet.window import key

'''манипуляции с окном'''
window = pyglet.window.Window(width=900, height=600)
window.set_caption('Tales')
pyglet.resource.path = ['game/resources']
pyglet.resource.reindex()
window.set_icon(pyglet.resource.image('cat1.png'))

'''создание "коллекций" с визуальными объектами'''
main_batch = pyglet.graphics.Batch()
wall_batch = pyglet.graphics.Batch()

'''визуализация персонажа'''
main_character_image = pyglet.resource.image('cat1.png')
#walking_frames = [pyglet.resource.image('walk1.png'), pyglet.resource.image('walk2.png')]
#walking_animation = pyglet.image.Animation.from_image_sequence(walking_frames, duration=0.1, loop=True)

'''визуализация стен'''
wall_left = pyglet.resource.image('walls_left.png')
wall_right = pyglet.resource.image('walls_right.png')
wall_top = pyglet.resource.image('walls_top.png')
wall_bot = pyglet.resource.image('walls_bot.png')
#walls = [wall_left, wall_right, wall_top, wall_bot]
'''left_wall = pyglet.shapes.Line(10, 10, 10, window.height-10, width=5, batch=wall_batch)
right_wall = pyglet.shapes.Line(window.width-10, 10, window.width-10, window.height-10, width=5, batch=wall_batch)
top_wall = pyglet.shapes.Line(10, window.height-10, window.width-10, window.height-10, width=5, batch=wall_batch)
bot_wall = pyglet.shapes.Line(10, 10, window.width-10, 10, width=5, batch=wall_batch)'''


class PhysicalObjects(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObjects, self).__init__(*args, **kwargs)


class Walls(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        self.wall_left = pyglet.sprite.Sprite(img=wall_left, x=10, y=10, batch=wall_batch)
        '''while self.wall_left.y <= window.height:
            self.wall_left.y +=69 
            self.wall_left'''
        
        #self.wall_left = pyglet.sprite.Sprite(img=wall_left, x=10, y=10, batch=wall_batch)
        #self.wall_left1 = pyglet.sprite.Sprite(img=wall_left, x=10, y=wall_left.y+69, batch=wall_batch)
        #self.wall_right = pyglet.sprite.Sprite(img=wall_right, *args, **kwargs)
        #self.wall_top = pyglet.sprite.Sprite(img=wall_top, *args, **kwargs)
        #self.wall_bot = pyglet.sprite.Sprite(img=wall_bot, *args, **kwargs)



class Player(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=main_character_image, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
    def update(self, dt):
        walk = 200
        if self.key_handler[key.A]:
            self.x -= walk * dt
        if self.key_handler[key.D]:
            self.x += walk * dt
        if self.key_handler[key.S]:
            self.y -= walk * dt
        if self.key_handler[key.W]:
            self.y += walk * dt 

main_character = Player(x=window.width//2, y=window.height//2, batch=main_batch)
main_character.scale = 2.2
wall = Walls(x=0, y=0)

window.push_handlers(main_character.key_handler)

def update(dt):
    main_character.update(dt)

@window.event
def on_draw():
    window.clear()
    wall_batch.draw()
    main_batch.draw()
    
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/60.0)  # на 120 уже не ускоряется, но немного фризит
    pyglet.app.run()

# 1. Вывести окно --done
        # Добавить название --done
        # Сделать иконку --done
        # Разбить на квадраты
# 2. Вывести персонажа в центре --done
# 3. Получить управление над персонажем --done
        # добавить коллизию
# 4. Сделать комнату 
        # с коллизией 
        # с текстурами стен
        # с текстурой пола
# 5. Сделать анимацию персонажу
        # ходьбы
        # простоя
# 6. 
#