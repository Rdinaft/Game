import pyglet
from pyglet.sprite import Sprite
from pyglet.window import key
from collision_check import are_objects_collided, calculate_objects_interposition
from resources import cat_set_image
from constants import CAT_CHARACTER_SIZE_MULTIPLIER, WALKING_SPEED, SPEEDUP_MODIFICATOR
from window import WINDOW
from walls import PRIMARY_WALL_LIST
from created_walls import CREATED_WALLS


class Player(Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img=cat_set_image(), *args, **kwargs)
        self.key_handler = key.KeyStateHandler()

    def update(self, dt):
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        self.can_move_up = True
        speed_modificator = 1


        for wall in PRIMARY_WALL_LIST + CREATED_WALLS:
            if are_objects_collided(self, wall):
                print(calculate_objects_interposition(self, wall))
                if calculate_objects_interposition(self, wall) == "left":
                    self.can_move_left = False
                elif calculate_objects_interposition(self, wall) == "right":
                    self.can_move_right = False
                elif calculate_objects_interposition(self, wall) == "up":
                    self.can_move_up = False
                elif calculate_objects_interposition(self, wall) == "down":
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


def cat_character():
    cat_batch = pyglet.graphics.Batch()
    cat = Player(x=WINDOW.width // 2, y=WINDOW.height // 2, batch=cat_batch)
    cat.scale = CAT_CHARACTER_SIZE_MULTIPLIER
    WINDOW.push_handlers(cat.key_handler)
    return cat, cat_batch
