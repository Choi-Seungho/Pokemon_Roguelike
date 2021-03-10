from ursina import *
import pickle
from textwrap import dedent

class Monster(Button):
    def __init__(self, position):
        super().__init__(parent = scene, model = 'quad', position=position, highlight_color = color.white)
        self.check = None

    def set_pokemon(self, pokemon: dict):
        self.num = pokemon['num']
        self.name = pokemon['name']
        self.type = pokemon['type']
        self.hp = pokemon['hp']
        self.attack = pokemon['attack']
        self.defense = pokemon['defense']
        self.sp_atk = pokemon['sp.atk']
        self.sp_def = pokemon['sp.def']
        self.speed = pokemon['speed']
        self.dict = pokemon
        self.img = '{0:03d}.png'.format(self.num)
        self.texture = './resources/picture/small/'+self.img
        self.total = self.hp + self.attack + self.defense + self.sp_atk + self.sp_def + self.speed

    def get_tooltip(self):
        return dedent('{name}\nHP:{hp}\nAttack:{atk}\nDefense:{defe}\nSP.Atk:{sp_atk}\nSP.Def:{sp_def}\nSpeed:{speed}\nTotal:{total}'.format(name=self.name, hp=self.hp, atk=self.attack, defe=self.defense, sp_atk=self.sp_atk, sp_def=self.sp_def, speed=self.speed, total=self.total))

    def input(self, key):
         if self.hovered:
            if key == 'left mouse down':
                self.check = self.num


if __name__ == '__main__':
    with open('./resources/pokemon_list.pkl', 'rb') as f:
        for i in range(1, 152):
            test = Monster(pickle.load(f))
            print(test.name)