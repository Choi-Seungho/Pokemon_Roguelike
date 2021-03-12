from ursina import *
import numpy as np
import math
import random
from BattleTab import BattleTab
from Monster import Monster
import pickle

class Player(Entity):
    def __init__(self, user_pokemon):
        super().__init__(model = 'quad', texture = './resources/sprites/player_standing_000.png', scale = (0.35 * 0.514, 0.4 * 0.514), position=(0,0))
        self.always_on_top = True
        self.move_speed = 2
        self.x, self.y = 1, 0
        self.wall = list()
        self.new_tab = None
        self.user_pokemon = user_pokemon
        self.texture_dict = {
            'left' : ['./resources/sprites/player_left_000.png', './resources/sprites/player_left_001.png', './resources/sprites/player_left_002.png'],
            'right' : ['./resources/sprites/player_right_000.png', './resources/sprites/player_right_001.png', './resources/sprites/player_right_002.png'],
            'front' : ['./resources/sprites/player_front_000.png', './resources/sprites/player_front_001.png', './resources/sprites/player_front_002.png'],
            'back' : ['./resources/sprites/player_back_000.png', './resources/sprites/player_back_001.png', './resources/sprites/player_back_002.png'],
        }
        self.now_texture = None
        self.t_count = 0
        self.battle = False
        self.first_stage = [1, 4, 7, 10, 13, 16, 19, 21, 23, 25, 27, 29, 32, 35, 37, 39, 41, 43, 46, 48, 
                            50, 52, 54, 56, 58, 60, 63, 66, 69, 72, 74, 77, 79, 81, 83, 84, 86, 88, 90, 90,
                            92, 95, 96, 98, 100, 102, 104, 109, 111, 116, 118, 120, 129, 133, 138, 140, 147]
        self.pokemon_list = list()
        with open('./resources/pokemon_list.pkl', 'rb') as f:
            for i in range(1, 152):
                self.pokemon_list.append(pickle.load(f))

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
                        enemy = Monster(position=(0,0))
                        enemy.visible = False
                        enemy.set_pokemon(self.pokemon_list[random.sample(self.first_stage, 1)[0]-1])
                        self.new_tab = BattleTab(self.user_pokemon, enemy)
                else:
                    self.x += 1 * time.dt
                self.change_texture('left')
            elif held_keys['right arrow']:
                if self.wall_check(self.x + (self.move_speed * time.dt), self.y):
                    self.x += self.move_speed * time.dt
                    if(rand <= 0.01):
                        self.battle = True
                        enemy = Monster(position=(0,0))
                        enemy.visible = False
                        enemy.set_pokemon(self.pokemon_list[random.sample(self.first_stage, 1)[0]-1])
                        self.new_tab = BattleTab(self.user_pokemon, enemy)
                else:
                    self.x -= 1 * time.dt
                self.change_texture('right')
            elif held_keys['up arrow']:
                if self.wall_check(self.x, self.y + (self.move_speed * time.dt)):
                    self.y += self.move_speed * time.dt
                    if(rand <= 0.01):
                        self.battle = True
                        enemy = Monster(position=(0,0))
                        enemy.visible = False
                        enemy.set_pokemon(self.pokemon_list[random.sample(self.first_stage, 1)[0]-1])
                        self.new_tab = BattleTab(self.user_pokemon, enemy)
                else:
                    self.y -= 1 * time.dt
                self.change_texture('back')
            elif held_keys['down arrow']:
                if self.wall_check(self.x, self.y - (self.move_speed * time.dt)):
                    self.y -= self.move_speed * time.dt
                    if(rand <= 0.01):
                        self.battle = True
                        enemy = Monster(position=(0,0))
                        enemy.visible = False
                        enemy.set_pokemon(self.pokemon_list[random.sample(self.first_stage, 1)[0]-1])
                        self.new_tab = BattleTab(self.user_pokemon, enemy)
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