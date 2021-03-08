from ursina import *
import numpy as np
import math

class Player(Entity):
    def __init__(self):
        super().__init__(model = 'quad', texture = './resources/sprites/player_standing_000.png', scale = (0.35 * 0.914, 0.4 * 0.914), position=(0,0))
        self.always_on_top = True
        self.move_speed = 2
        self.x, self.y = 1, 0
        self.texture_dict = {
            'left' : ['./resources/sprites/player_left_000.png', './resources/sprites/player_left_001.png', './resources/sprites/player_left_002.png'],
            'right' : ['./resources/sprites/player_right_000.png', './resources/sprites/player_right_001.png', './resources/sprites/player_right_002.png'],
            'front' : ['./resources/sprites/player_front_000.png', './resources/sprites/player_front_001.png', './resources/sprites/player_front_002.png'],
            'back' : ['./resources/sprites/player_back_000.png', './resources/sprites/player_back_001.png', './resources/sprites/player_back_002.png'],
        }
        self.now_texture = None
        self.t_count = 0
        self.battle = False

    def update(self):
        if not self.battle:
            if held_keys['shift']:
                self.move_speed = 5
            else:
                self.move_speed = 2

            if held_keys['left arrow']:
                self.x -= self.move_speed * time.dt
                self.change_texture('left')
            elif held_keys['right arrow']:
                self.x += self.move_speed * time.dt
                self.change_texture('right')
            elif held_keys['up arrow']:
                self.y += self.move_speed * time.dt
                self.change_texture('back')
            elif held_keys['down arrow']:
                self.y -= self.move_speed * time.dt
                self.change_texture('front')

            camera.x , camera.y = self.x, self.y

    def change_texture(self, value):
        if value == self.now_texture:
            self.t_count += 0.5
            if self.t_count > 2:
                self.t_count = 0
        else:
            self.now_texture = value
            self.t_count = 0
        self.texture = self.texture_dict[value][math.floor(self.t_count)]

if __name__ == '__main__':
    app = Ursina()
    test = Player()
    app.run()