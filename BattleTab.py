from ursina import *
from ursina.prefabs.health_bar import HealthBar
import numpy as np
import pickle

class BattleTab(Entity):
    def __init__(self, user_pokemon):
        self.background_e = Entity(parent = camera.ui, model = 'quad', 
                        position = (0, 0), scale = (10, 10), color=color.white)
        super().__init__(parent = camera.ui, model = 'quad', 
                        position = (0, 0), scale = (.255 * 3, .143 * 3), 
                        texture = './resources/sprites/tab.png')
        self.always_on_top = False
        self.user_pokemon = user_pokemon
        self.pokemon_list = list()
        self.start_pokemon = [1, 4, 7, 10, 13, 16, 19, 21, 23, 25, 27, 29, 32, 35, 37, 39, 41, 43, 46, 48, 
                 50, 52, 54, 56, 58, 60, 63, 66, 69, 72, 74, 77, 79, 81, 83, 84, 86, 88, 90, 90,
                 92, 95, 96, 98, 100, 102, 104, 109, 111, 116, 118, 120, 129, 133, 138, 140, 147]
        with open('./resources/pokemon_list.pkl', 'rb') as f:
            for i in range(1, 152):
                self.pokemon_list.append(pickle.load(f))

        self.user = Animation(parent = camera.ui, name='./resources/picture/back/{}'.format(self.user_pokemon[0].img_gif), position = (-.21, -.126), scale = (.25 / 2, .25 / 2))
        self.enemy = Animation(parent = camera.ui, name='./resources/picture/front/{0:03d}.gif'.format(random.sample(self.start_pokemon, 1)[0]), position = (.21, -.01), scale = (.25 / 2, .25 / 2))
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