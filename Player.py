from ursina import *
import numpy as np
import math
import random
from BattleTab import BattleTab

class Player(Entity):
    def __init__(self):
        super().__init__(model = 'quad', texture = './resources/sprites/player_standing_000.png', scale = (0.35 * 0.514, 0.4 * 0.514), position=(0,0))
        self.always_on_top = True
        self.move_speed = 2
        self.x, self.y = 1, 0
        self.wall = list()
        self.new_tab = None
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
            rand = random.random()
            if held_keys['left arrow']:
                if self.wall_check(self.x - (self.move_speed * time.dt), self.y):
                    self.x -= self.move_speed * time.dt
                    if(rand <= 0.01):
                        self.battle = True
                        self.new_tab = BattleTab()
                else:
                    self.x += 1 * time.dt
                self.change_texture('left')
            elif held_keys['right arrow']:
                if self.wall_check(self.x + (self.move_speed * time.dt), self.y):
                    self.x += self.move_speed * time.dt
                    if(rand <= 0.01):
                        self.battle = True
                        self.new_tab = BattleTab()
                else:
                    self.x -= 1 * time.dt
                self.change_texture('right')
            elif held_keys['up arrow']:
                if self.wall_check(self.x, self.y + (self.move_speed * time.dt)):
                    self.y += self.move_speed * time.dt
                    if(rand <= 0.01):
                        self.battle = True
                        self.new_tab = BattleTab()
                else:
                    self.y -= 1 * time.dt
                self.change_texture('back')
            elif held_keys['down arrow']:
                if self.wall_check(self.x, self.y - (self.move_speed * time.dt)):
                    self.y -= self.move_speed * time.dt
                    if(rand <= 0.01):
                        self.battle = True
                        self.new_tab = BattleTab()
                else:
                    self.y += 1 * time.dt
                self.change_texture('front')

            
            camera.x , camera.y = self.x, self.y

        else:
            if held_keys['q']:
                self.battle = False
                self.new_tab.end_battle()
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

    def wall_check(self, x, y):
        for i in self.wall:
            wall_x = i[0]
            wall_y = i[1]
            if wall_x - 0.18 <= x <= wall_x + 0.18 and wall_y - 0.18 <= y <= wall_y + 0.18:
                return False
            else:
                continue
        return True

if __name__ == '__main__':
    app = Ursina()
    test = Player()
    app.run()