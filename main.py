import pyglet
import random
from pyglet.window import key

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

class Graphic:
    pyglet.resource.path = ['game/resources']
    pyglet.resource.reindex()
    main_batch = pyglet.graphics.Batch()
    wall_batch = pyglet.graphics.Batch()
    main_character_image = pyglet.resource.image('cat1.png')
    main_character_image.anchor_x = main_character_image.width // 2
    main_character_image.anchor_y = main_character_image.height // 2
    
    def img_source(image):
        img = pyglet.resource.image('' + image)
        return img
    walls_top = [img_source('w1.png'), img_source('w2.png'), img_source('w3.png'), img_source('w4.png'), img_source('w5.png'), img_source('w6.png')]
    walls_bot = [img_source('wb1.png'), img_source('wb2.png'), img_source('wb3.png'), img_source('wb4.png'), img_source('wb5.png'), img_source('wb6.png')]
    walls_left = [img_source('wl1.png'), img_source('wl2.png'), img_source('wl3.png'), img_source('wl4.png')]
    walls_right = [img_source('wr1.png'), img_source('wr2.png'), img_source('wr3.png'), img_source('wr4.png')]
    wall_list = []

class Window:
    global times_x, times_y
    # для корректного построения стен без дыр с отступами по краям с примерным размером окна 900х600
    times_x = (WINDOW_WIDTH - 30) // Graphic.walls_top[0].width
    times_y = (WINDOW_HEIGHT - 30) // Graphic.walls_left[0].height
    window = pyglet.window.Window(width=times_x * Graphic.walls_top[0].width - Graphic.walls_left[0].width + 30, height=times_y * Graphic.walls_left[0].height - Graphic.walls_top[0].height // 2 + 30)
    window.set_caption('Tales')
    window.set_icon(pyglet.resource.image('cat1.png'))

class PhysicalObjects(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObjects, self).__init__(*args, **kwargs)

class Walls(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        for x in range(int(times_x)):
            Graphic.wall_list.append(PhysicalObjects(random.choice(Graphic.walls_top), x= 15 + x * Graphic.walls_top[0].width, y= Window.window.height-30, batch=Graphic.wall_batch))
            Graphic.wall_list.append(PhysicalObjects(random.choice(Graphic.walls_bot), x= 15 + x * Graphic.walls_bot[0].width, y= 10, batch=Graphic.wall_batch))
        for y in range(int(times_y)):
            Graphic.wall_list.append(PhysicalObjects(random.choice(Graphic.walls_left), x= 10, y= 10 + y * Graphic.walls_left[0].height, batch=Graphic.wall_batch))
            Graphic.wall_list.append(PhysicalObjects(random.choice(Graphic.walls_right), x= Window.window.width - 10, y= 10 + y * Graphic.walls_right[0].height, batch=Graphic.wall_batch))

class Player(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=Graphic.main_character_image, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
    def update(self, dt):
        walk = 200
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        self.can_move_up = True
        for wall in Graphic.wall_list:
            wall.anchor_x = wall.width // 2
            wall.anchor_y = wall.height // 2
            if (self.x-wall.x)**2 + (self.y-wall.y)**2 < (self.width//2 + wall.width//2)**2: 
                if self.x - self.width//2 < wall.x + wall.width//2:
                    self.can_move_left = False
                if self.x + self.width//2 < wall.x - wall.width//2:
                    self.can_move_right = False
                if self.y + self.height//2 > wall.y - wall.height//2:
                    self.can_move_up = False
                if self.y - self.height//2 < wall.y + wall.height//2:
                    self.can_move_down = False
        if self.key_handler[key.SPACE]:
            walk = 200 * 2.5
        if self.key_handler[key.A] and self.can_move_left == True:
            self.x -= walk * dt
        if self.key_handler[key.D] and self.can_move_right == True:
            self.x += walk * dt
        if self.key_handler[key.S] and self.can_move_down == True:
            self.y -= walk * dt
        if self.key_handler[key.W] and self.can_move_up == True:
            self.y += walk * dt 

main_character = Player(x=Window.window.width//2, y=Window.window.height//2, batch=Graphic.main_batch)
main_character.scale = 1.5
walls = Walls()

Window.window.push_handlers(main_character.key_handler)

def update(dt):
    main_character.update(dt)

@Window.window.event
def on_draw():
    Window.window.clear()
    Graphic.wall_batch.draw()
    Graphic.main_batch.draw()
    
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
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
        # с текстурами стен --done
        # с текстурой пола