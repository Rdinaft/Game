import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key
from resources import main_character_image, one_wall
from collision_check import are_objects_collided, calculate_objects_interposition
from constants import MAIN_CHARACTER_SCALE, WALKING_SPEED
from window import WINDOW


class Player(Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=main_character_image, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()


    def update(self, dt):
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        self.can_move_up = True
        speed_modificator = 1

        if are_objects_collided(self, one_wall()):
            if calculate_objects_interposition(self, one_wall()) == 'left':
                print('left')
                self.can_move_left = False
            if calculate_objects_interposition(self, one_wall()) == 'right':
                print('right')
                self.can_move_right = False
            if calculate_objects_interposition(self, one_wall()) == 'up':
                print('up')
                self.can_move_up = False
            if calculate_objects_interposition(self, one_wall()) == 'down':
                print('down')
                self.can_move_down = False 
        
        if self.key_handler[key.SPACE]:
            speed_modificator = 2.5
        if self.key_handler[key.A] and self.can_move_left:
            self.x -= WALKING_SPEED * dt * speed_modificator
        if self.key_handler[key.D] and self.can_move_right:
            self.x += WALKING_SPEED * dt * speed_modificator
        if self.key_handler[key.S] and self.can_move_down:
            self.y -= WALKING_SPEED * dt * speed_modificator
        if self.key_handler[key.W] and self.can_move_up:
            self.y += WALKING_SPEED * dt * speed_modificator

MAIN_BATCH = pyglet.graphics.Batch()
MAIN_CHARACTER = Player(x=WINDOW.width // 2, y=WINDOW.height // 2, batch=MAIN_BATCH)
MAIN_CHARACTER.scale = MAIN_CHARACTER_SCALE
WINDOW.push_handlers(MAIN_CHARACTER.key_handler)
