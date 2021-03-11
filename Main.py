from ursina import *
from Monster import Monster
from Player import Player
from Map import Map
import pickle
import random
from textwrap import dedent

class Reroll(Button):
    def __init__(self, pokemon_list, start_pokemon, entity_list):
        super().__init__(parent = scene, model = 'quad', position=(0,-2), color = color.white, highlight_color = color.lime)
        self.pokemon_list = pokemon_list
        self.entity_list = entity_list
        self.start_pokemon = start_pokemon
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                sample = random.sample(self.start_pokemon, 3)
                for i in range(3):
                    self.entity_list[i].set_pokemon(self.pokemon_list[sample[i]-1])
                    tooltip = self.entity_list[i].get_tooltip()
                    tool = Tooltip(text=tooltip)
                    tool.wordwrap = 1
                    tool.background = True
                    self.entity_list[i].tooltip = tool
                    start_entity[i].check = None

def random_starting_pokemon(pokemon_list, start_pokemon, entity_list):
    sample = random.sample(start_pokemon, 3)
    for i in range(3):
        entity_list[i].set_pokemon(pokemon_list[sample[i]-1])
        tooltip = entity_list[i].get_tooltip()
        tool = Tooltip(text=tooltip)
        tool.wordwrap = 1
        tool.background = False
        entity_list[i].tooltip = tool

def selcet_pokemon():
    for i in range(3):
        if start_entity[i].check:
            user_pokemon.append(Monster(position=(0,0)))
            user_pokemon[0].visible = False
            user_pokemon[0].set_pokemon(pokemon_list[start_entity[i].num -1])
            break
    for i in range(3):
        destroy(start_entity[i])
    destroy(reroll)
    Map_size=20
    user = Player(user_pokemon)
    
    stage=Map(input_size=Map_size, p=user)
    stage.set_MapLine()
    user.wall = stage.wall
    user.x = stage.entity[0][1].x
    user.y = stage.entity[0][1].y
    camera.x, camera.y = user.x, user.y

start_entity = [1,1,1]
user_pokemon = list()
pokemon_list = list()
start_pokemon = [1, 4, 7, 10, 13, 16, 19, 21, 23, 25, 27, 29, 32, 35, 37, 39, 41, 43, 46, 48, 
                 50, 52, 54, 56, 58, 60, 63, 66, 69, 72, 74, 77, 79, 81, 83, 84, 86, 88, 90, 90,
                 92, 95, 96, 98, 100, 102, 104, 109, 111, 116, 118, 120, 129, 133, 138, 140, 147]
Text.default_font = './resources/D2Coding-Ver1.3.2-20180524.ttf'
Text.background = False
with open('./resources/pokemon_list.pkl', 'rb') as f:
    for i in range(1, 152):
        pokemon_list.append(pickle.load(f))

start_entity = [1,1,1]
start_pos = [5, 0, -5]
for i in range(3):
    start_entity[i] = Monster(position=(start_pos[i],1.5))
    start_entity[i].on_click = selcet_pokemon
reroll = Reroll(pokemon_list, start_pokemon, start_entity)



if __name__ == '__main__':
    window.borderless = False
    
    app = Ursina()
    random_starting_pokemon(pokemon_list, start_pokemon, start_entity)
    app.run()