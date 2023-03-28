import pyglet
import math
from pyglet.gl import *
from pyglet.window import key

'''манипуляции с окном'''
window = pyglet.window.Window(width=841, height=572)
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
wall_list = []

class PhysicalObjects(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObjects, self).__init__(*args, **kwargs)
'''    def distance(point_1=(0, 0), point_2=(0, 0)):
        return math.sqrt((point_1[0] - point_2[0]) ** 2 +(point_1[1] - point_2[1]) ** 2)
    def collides_with(self, other_object):
        collision_distance = self.image.width/2 + other_object.image.width/2
        actual_distance = PhysicalObjects.distance(self.position, other_object.position)

        return (actual_distance <= collision_distance)'''

class Walls(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        #super(Walls, self).__init__(wall_list, *args, **kwargs)
        times_x = window.width // wall_top.width
        times_y = window.height // wall_left.height
        
        for x in range(int(times_x)):
            wall_list.append(PhysicalObjects(wall_top, x= 15 + x * wall_top.width, y= window.height-30, batch=wall_batch))
            wall_list.append(PhysicalObjects(wall_bot, x= 15 + x * wall_bot.width, y= 10, batch=wall_batch))

        for y in range(int(times_y)):
            wall_list.append(PhysicalObjects(wall_left, x= 10, y= 10 + y * wall_left.height, batch=wall_batch))
            wall_list.append(PhysicalObjects(wall_right, x= window.width - 10, y= 10 + y * wall_right.height, batch=wall_batch))

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

walls = Walls()
#walls.scale = 2
#game_objects = [main_character] + walls

#Walls.wall_list.scale = 2

window.push_handlers(main_character.key_handler)

def update(dt):
    main_character.update(dt)
    #walls.update()

    '''for i in range(len(game_objects)):
        for j in range(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
    if obj_1.collides_with(obj_2):
        obj_1.handle_collision_with(obj_2)
        obj_2.handle_collision_with(obj_1)'''
    #for wall in wall_list:
        #wall.update()

@window.event
def on_draw():
    window.clear()
    wall_batch.draw()
    main_batch.draw()
    
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)  # на 120 уже не ускоряется, но немного фризит
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