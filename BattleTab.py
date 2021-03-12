from ursina import *
from ursina.prefabs.health_bar import HealthBar
import numpy as np
import pickle

class BattleTab(Entity):
    def __init__(self, user_pokemon, enemy_pokemon):
        self.background_e = Entity(parent = camera.ui, model = 'quad', 
                        position = (0, 0), scale = (10, 10), color=color.white)
        super().__init__(parent = camera.ui, model = 'quad', 
                        position = (0, 0), scale = (.255 * 3, .143 * 3), 
                        texture = './resources/sprites/tab.png')
        self.always_on_top = False
        self.user_pokemon = user_pokemon
        self.enemy_pokemon = enemy_pokemon
        self.pokemon_list = list()
        with open('./resources/pokemon_list.pkl', 'rb') as f:
            for i in range(1, 152):
                self.pokemon_list.append(pickle.load(f))

        self.user = Animation(parent = camera.ui, name='./resources/picture/back/{}'.format(self.user_pokemon[0].img_gif), position = (-.21, -.126), scale = (.25 / 2, .25 / 2))
        self.enemy = Animation(parent = camera.ui, name='./resources/picture/front/{}'.format(self.enemy_pokemon.img_gif), position = (.21, -.01), scale = (.25 / 2, .25 / 2))
        self.user.always_on_top = True
        self.enemy.always_on_top = True

    def end_battle(self):
        destroy(self.user)
        destroy(self.enemy)
        destroy(self.background_e)
        destroy(self)

if __name__ == '__main__':
    import sys
    window.borderless = False
    app = Ursina()
    sys.setrecursionlimit(20000)

    mt = BattleTab()

    app.run()