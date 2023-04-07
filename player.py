import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key
from resources import cat_character_image, primary_wall_list
from collision_check import are_objects_collided, calculate_objects_interposition
from constants import CAT_CHARACTER_SIZE_MULTIPLIER, WALKING_SPEED, SPEEDUP_MODIFICATOR
from window import WINDOW


class Player(Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=cat_character_image, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()


    def update(self, dt):
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        self.can_move_up = True
        speed_modificator = 1

        for wall in primary_wall_list:
            if are_objects_collided(self, wall):
                if calculate_objects_interposition(self, wall) == 'left':
                    self.can_move_left = False
                if calculate_objects_interposition(self, wall) == 'right':
                    self.can_move_right = False
                if calculate_objects_interposition(self, wall) == 'up':
                    self.can_move_up = False
                if calculate_objects_interposition(self, wall) == 'down':
                    self.can_move_down = False 
        
        if self.key_handler[key.SPACE]:
            speed_modificator = SPEEDUP_MODIFICATOR
        if self.key_handler[key.A] and self.can_move_left:
            self.x -= WALKING_SPEED * dt * speed_modificator
        if self.key_handler[key.D] and self.can_move_right:
            self.x += WALKING_SPEED * dt * speed_modificator
        if self.key_handler[key.S] and self.can_move_down:
            self.y -= WALKING_SPEED * dt * speed_modificator
        if self.key_handler[key.W] and self.can_move_up:
            self.y += WALKING_SPEED * dt * speed_modificator

CAT_BATCH = pyglet.graphics.Batch()
CAT_CHARACTER = Player(x=WINDOW.width // 2, y=WINDOW.height // 2, batch=CAT_BATCH)
CAT_CHARACTER.scale = CAT_CHARACTER_SIZE_MULTIPLIER
WINDOW.push_handlers(CAT_CHARACTER.key_handler)
