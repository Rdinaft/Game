import pyglet
from pyglet.window import key


class Graphic:
    pyglet.resource.path = ['game/resources']
    pyglet.resource.reindex()
    main_batch = pyglet.graphics.Batch()
    wall_batch = pyglet.graphics.Batch()
    main_character_image = pyglet.resource.image('cat1.png')
    wall_left = pyglet.resource.image('walls_left.png')
    wall_right = pyglet.resource.image('walls_right.png')
    wall_top = pyglet.resource.image('walls_top.png')
    wall_bot = pyglet.resource.image('walls_bot.png')
    wall_list = []

class Window:
    window = pyglet.window.Window(width=841, height=572)
    window.set_caption('Tales')
    window.set_icon(pyglet.resource.image('cat1.png'))

class PhysicalObjects(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super(PhysicalObjects, self).__init__(*args, **kwargs)
'''    def distancesq(self,target):
        return (self.x-target.x)**2 + (self.y-target.y)**2
    def check_collision(self):
        for i in game_objects:
            if self.distancesq(i) < (self.width/2 + i.width/2)**2: 
                return True'''

class Walls(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        times_x = Window.window.width // Graphic.wall_top.width
        times_y = Window.window.height // Graphic.wall_left.height
        
        for x in range(int(times_x)):
            Graphic.wall_list.append(PhysicalObjects(Graphic.wall_top, x= 15 + x * Graphic.wall_top.width, y= Window.window.height-30, batch=Graphic.wall_batch))
            Graphic.wall_list.append(PhysicalObjects(Graphic.wall_bot, x= 15 + x * Graphic.wall_bot.width, y= 10, batch=Graphic.wall_batch))
        for y in range(int(times_y)):
            Graphic.wall_list.append(PhysicalObjects(Graphic.wall_left, x= 10, y= 10 + y * Graphic.wall_left.height, batch=Graphic.wall_batch))
            Graphic.wall_list.append(PhysicalObjects(Graphic.wall_right, x= Window.window.width - 10, y= 10 + y * Graphic.wall_right.height, batch=Graphic.wall_batch))

class Player(PhysicalObjects):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=Graphic.main_character_image, *args, **kwargs)
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

main_character = Player(x=Window.window.width//2, y=Window.window.height//2, batch=Graphic.main_batch)
main_character.scale = 2
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
    pyglet.clock.schedule_interval(update, 1/60.0)
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
# 5. Сделать анимацию персонажу
        # ходьбы
        # простоя
# 6. 
#