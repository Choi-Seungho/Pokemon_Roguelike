from ursina import *
from ursina.prefabs.health_bar import HealthBar
import numpy as np

class BattleTab(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, model = 'quad', 
                        position = (0, 0), scale = (.255 * 3.5, .143 * 3.5), 
                        texture = './resources/sprites/tab.png')
        self.always_on_top = False
        self.user = Animation(parent = camera.ui, name='./resources/picture/back/056.gif', position = (-.22, -.125), scale = (.25, .25))
        self.enemy = Animation(parent = camera.ui, name='./resources/picture/front/003.gif', position = (.22, .05), scale = (.25, .25))
        self.user.always_on_top = True
        self.enemy.always_on_top = True

    def end_battle(self):
        destroy(self.user)
        destroy(self.enemy)
        destroy(self)

if __name__ == '__main__':
    import sys
    window.borderless = False
    app = Ursina()
    sys.setrecursionlimit(20000)

    mt = BattleTab()

    app.run()