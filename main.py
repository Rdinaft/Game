import pyglet
import random
from constants import *
from pyglet.sprite import Sprite
from pyglet.window import key


def create_starting_window():
    global main_character_image, main_batch, wall_list, wall_batch
    pyglet.resource.path = ['game/resources']
    pyglet.resource.reindex()
    main_batch = pyglet.graphics.Batch()
    wall_batch = pyglet.graphics.Batch()

    def img_source(image):
        img = pyglet.resource.image('' + image)
        return img
    
    main_character_image = img_source('cat1.png')
    main_character_image.anchor_x = main_character_image.width // 2
    main_character_image.anchor_y = main_character_image.height // 2
        
    walls_top = [img_source('w1.png'), img_source('w2.png'), img_source('w3.png'), img_source('w4.png'), img_source('w5.png'), img_source('w6.png')]
    walls_bot = [img_source('wb1.png'), img_source('wb2.png'), img_source('wb3.png'), img_source('wb4.png'), img_source('wb5.png'), img_source('wb6.png')]
    walls_left = [img_source('wl1.png'), img_source('wl2.png'), img_source('wl3.png'), img_source('wl4.png')]
    walls_right = [img_source('wr1.png'), img_source('wr2.png'), img_source('wr3.png'), img_source('wr4.png')]
    wall_list = []
    
    sprite_times_x = (WINDOW_WIDTH - 30) // walls_top[0].width
    sprite_times_y = (WINDOW_HEIGHT - 30) // walls_left[0].height

    def create_window():
        global window
        window = pyglet.window.Window(width = sprite_times_x * walls_top[0].width - walls_left[0].width + 30, height = sprite_times_y * walls_left[0].height - walls_top[0].height // 2 + 30)
        window.set_caption('Cat Tale')
        window.set_icon(pyglet.resource.image('cat1.png'))
    
    def create_walls():
        for x in range(int(sprite_times_x)):
            wall_list.append(Sprite(random.choice(walls_top), x = 15 + x * walls_top[0].width, y = window.height - 30, batch = wall_batch))
            wall_list.append(Sprite(random.choice(walls_bot), x = 15 + x * walls_bot[0].width, y = 10, batch = wall_batch))
        for y in range(int(sprite_times_y)):
            wall_list.append(Sprite(random.choice(walls_left), x = 10, y = 10 + y * walls_left[0].height, batch = wall_batch))
            wall_list.append(Sprite(random.choice(walls_right), x = window.width - 10, y = 10 + y * walls_right[0].height, batch = wall_batch))

    create_window()
    create_walls()

class Player(Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img = main_character_image, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
    def update(self, dt):
        walking_speed = 200
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        self.can_move_up = True
        
        def are_objects_collided(obj1, obj2):
            for obj in obj2:
                obj.anchor_x = obj.width // 2
                obj.anchor_y = obj.height // 2
                if (obj1.x - obj.x) ** 2 + (obj1.y - obj.y) ** 2 < (obj1.width // 2 + obj.width // 2) ** 2: 
                    if obj1.x - obj1.width // 2 < obj.x + obj.width // 2:
                        obj1.can_move_left = False
                    if obj1.x + obj1.width // 2 < obj.x - obj.width // 2:
                        obj1.can_move_right = False
                    if obj1.y + obj1.height // 2 > obj.y - obj.height // 2:
                        obj1.can_move_up = False
                    if obj1.y - obj1.height // 2 < obj.y + obj.height // 2:
                        obj1.can_move_down = False
        
        are_objects_collided(self, wall_list)
        if self.key_handler[key.SPACE]:
            walking_speed = walking_speed * 2.5
        if self.key_handler[key.A] and self.can_move_left:
            self.x -= walking_speed * dt
        if self.key_handler[key.D] and self.can_move_right:
            self.x += walking_speed * dt
        if self.key_handler[key.S] and self.can_move_down:
            self.y -= walking_speed * dt
        if self.key_handler[key.W] and self.can_move_up:
            self.y += walking_speed * dt 

create_starting_window()
main_character = Player(x = window.width // 2, y = window.height // 2, batch = main_batch)
main_character.scale = MAIN_CHARACTER_SCALE
window.push_handlers(main_character.key_handler)

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

# 1. Вывести окно --done
        # Добавить название --done
        # Сделать иконку --done
        # Разбить на квадраты
# 2. Вывести персонажа в центре --done
# 3. Получить управление над персонажем --done
# 4. Сделать комнату 
        # с коллизией 
        # с текстурами стен --done
        # с текстурой пола