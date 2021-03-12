from ursina import *
import pickle
import random
from textwrap import dedent

class Monster(Button):
    def __init__(self, position):
        super().__init__(parent = scene, model = 'quad', position=position, highlight_color = color.white)
        self.check = None
        self.stats = list()
        self.next = 0
        self.level = 1
        self.exp = 0

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
        self.img_gif = '{0:03d}.gif'.format(self.num)
        self.texture = './resources/picture/small/'+self.img
        self.total = self.hp + self.attack + self.defense + self.sp_atk + self.sp_def + self.speed
        self.next = self.num

    def get_tooltip(self):
        return dedent('{name}\nHP:{hp}\nAttack:{atk}\nDefense:{defe}\nSP.Atk:{sp_atk}\nSP.Def:{sp_def}\nSpeed:{speed}\nTotal:{total}'.format(name=self.name, hp=self.hp, atk=self.attack, defe=self.defense, sp_atk=self.sp_atk, sp_def=self.sp_def, speed=self.speed, total=self.total))

    def update_stats(self):
        self.stats[0] = (self.hp * 2 + 31) * (self.level / 100) + 10 + self.level
        self.stats[1] = (self.attack * 2 + 31) * (self.level / 100) + 10 + self.level
        self.stats[2] = (self.defense * 2 + 31) * (self.level / 100) + 10 + self.level
        self.stats[3] = (self.sp_atk * 2 + 31) * (self.level / 100) + 10 + self.level
        self.stats[4] = (self.sp_def * 2 + 31) * (self.level / 100) + 10 + self.level
        self.stats[5] = (self.speed * 2 + 31) * (self.level / 100) + 10 + self.level

    def check_evloution(self):
        if self.num == 1 and self.level >= 16:
            self.next = 2
        elif self.num == 2 and self.level >= 32:
            self.next = 3
        elif self.num == 4 and self.level >= 16:
            self.next = 5
        elif self.num == 5 and self.level >= 36:
            self.next = 6
        elif self.num == 7 and self.level >= 16:
            self.next = 8
        elif self.num == 8 and self.level >= 36:
            self.next = 9
        elif self.num == 10 and self.level >= 7:
            self.next = 11
        elif self.num == 11 and self.level >= 10:
            self.next = 12
        elif self.num == 13 and self.level >= 7:
            self.next = 14
        elif self.num == 14 and self.level >= 10:
            self.next = 15
        elif self.num == 16 and self.level >= 18:
            self.next = 17
        elif self.num == 17 and self.level >= 36:
            self.next = 18
        elif self.num == 19 and self.level >= 20:
            self.next = 20
        elif self.num == 21 and self.level >= 20:
            self.next = 22
        elif self.num == 23 and self.level >= 22:
            self.next = 24
        elif self.num == 25 and self.level >= 30:
            self.next = 26
        elif self.num == 27 and self.level >= 22:
            self.next = 28
        elif self.num == 29 and self.level >= 16:
            self.next = 30
        elif self.num == 30 and self.level >= 30:
            self.next = 31
        elif self.num == 32 and self.level >= 16:
            self.next = 33
        elif self.num == 33 and self.level >= 30:
            self.next = 34
        elif self.num == 35 and self.level >= 30:
            self.next = 36
        elif self.num == 37 and self.level >= 30:
            self.next = 38
        elif self.num == 39 and self.level >= 30:
            self.next = 40
        elif self.num == 41 and self.level >= 22:
            self.next = 42
        elif self.num == 43 and self.level >= 21:
            self.next = 44
        elif self.num == 44 and self.level >= 32:
            self.next = 45
        elif self.num == 46 and self.level >= 24:
            self.next = 47
        elif self.num == 48 and self.level >= 31:
            self.next = 49
        elif self.num == 50 and self.level >= 26:
            self.next = 51
        elif self.num == 52 and self.level >= 28:
            self.next = 53
        elif self.num == 54 and self.level >= 33:
            self.next = 55
        elif self.num == 56 and self.level >= 28:
            self.next = 57
        elif self.num == 58 and self.level >= 30:
            self.next = 59
        elif self.num == 60 and self.level >= 25:
            self.next = 61
        elif self.num == 61 and self.level >= 36:
            self.next = 62
        elif self.num == 63 and self.level >= 16:
            self.next = 64
        elif self.num == 64 and self.level >= 30:
            self.next = 65
        elif self.num == 66 and self.level >= 28:
            self.next = 67
        elif self.num == 67 and self.level >= 36:
            self.next = 68
        elif self.num == 69 and self.level >= 21:
            self.next = 70
        elif self.num == 70 and self.level >= 30:
            self.next = 71
        elif self.num == 72 and self.level >= 30:
            self.next = 73
        elif self.num == 74 and self.level >= 25:
            self.next = 75
        elif self.num == 75 and self.level >= 36:
            self.next = 76
        elif self.num == 77 and self.level >= 40:
            self.next = 78
        elif self.num == 79 and self.level >= 37:
            self.next = 80
        elif self.num == 81 and self.level >= 30:
            self.next = 82
        elif self.num == 84 and self.level >= 31:
            self.next = 85
        elif self.num == 86 and self.level >= 34:
            self.next = 87
        elif self.num == 88 and self.level >= 38:
            self.next = 89
        elif self.num == 90 and self.level >= 28:
            self.next = 91
        elif self.num == 92 and self.level >= 25:
            self.next = 93
        elif self.num == 93 and self.level >= 36:
            self.next = 94
        elif self.num == 96 and self.level >= 26:
            self.next = 97
        elif self.num == 98 and self.level >= 28:
            self.next = 99
        elif self.num == 100 and self.level >= 30:
            self.next = 101
        elif self.num == 102 and self.level >= 30:
            self.next = 103
        elif self.num == 104 and self.level >= 28:
            self.next = 105
        elif self.num == 109 and self.level >= 35:
            self.next = 110
        elif self.num == 111 and self.level >= 42:
            self.next = 112
        elif self.num == 116 and self.level >= 32:
            self.next = 117
        elif self.num == 118 and self.level >= 33:
            self.next = 119
        elif self.num == 120 and self.level >= 32:
            self.next = 121
        elif self.num == 129 and self.level >= 20:
            self.next = 130
        elif self.num == 133 and self.level >= 20:
            self.next = random.randrange(135,137)
        elif self.num == 138 and self.level >= 40:
            self.next = 139
        elif self.num == 140 and self.level >= 40:
            self.next = 141
        elif self.num == 147 and self.level >= 30:
            self.next = 148
        elif self.num == 148 and self.level >= 55:
            self.next = 149

    def input(self, key):
         if self.hovered:
            if key == 'left mouse down':
                self.check = self.num


if __name__ == '__main__':
    with open('./resources/pokemon_list.pkl', 'rb') as f:
        for i in range(1, 152):
            test = Monster(pickle.load(f))
            print(test.name)