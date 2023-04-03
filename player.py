from pyglet.sprite import Sprite
from pyglet.window import key
from resources import main_character_image, wall_list, main_batch
from collision_check import are_objects_collided, calculate_objects_interposition
from constants import MAIN_CHARACTER_SCALE, WALKING_SPEED
from window import window


class Player(Sprite):
    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(img = main_character_image, *args, **kwargs)
        self.key_handler = key.KeyStateHandler()
    def update(self, dt):
        self.can_move_left = True
        self.can_move_right = True
        self.can_move_down = True
        self.can_move_up = True
        haste = 1

        if are_objects_collided(self, wall_list):
            calculate_objects_interposition(self, wall_list)

        if self.key_handler[key.SPACE]:
            haste = 2.5
        if self.key_handler[key.A] and self.can_move_left:
            self.x -= WALKING_SPEED * dt * haste
        if self.key_handler[key.D] and self.can_move_right:
            self.x += WALKING_SPEED * dt * haste
        if self.key_handler[key.S] and self.can_move_down:
            self.y -= WALKING_SPEED * dt * haste
        if self.key_handler[key.W] and self.can_move_up:
            self.y += WALKING_SPEED * dt * haste

main_character = Player(x = window.width // 2, y = window.height // 2, batch = main_batch)
main_character.scale = MAIN_CHARACTER_SCALE
window.push_handlers(main_character.key_handler)
