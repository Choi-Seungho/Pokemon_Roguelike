from ursina import *
from Monster import Monster
import pickle
import random
from textwrap import dedent

def random_starting_pokemon(pokemon_list, sample_list, entity_list):
    sample = random.sample(sample_list, 3)
    for i in range(3):
        entity_list[i].texture = './resources/picture/small/{0:03d}.png'.format(sample[i])
        tooltip = Monster(pokemon_list[sample[i]-1]).get_tooltip()
        tool = Tooltip(text=tooltip)
        tool.wordwrap = 1
        tool.background = True
        entity_list[i].tooltip = tool

if __name__ == '__main__':
    window.borderless = False
    pokemon_list = list()
    start_pokemon = [1, 4, 7, 10, 13, 16, 19, 21, 23, 25, 27, 29, 32, 35, 37, 39, 41, 43, 46, 48, 
                     50, 52, 54, 56, 58, 60, 63, 66, 69, 72, 74, 77, 79, 81, 83, 84, 86, 88, 90, 90,
                     92, 95, 96, 98, 100, 102, 104, 109, 111, 116, 118, 120, 129, 133, 138, 140, 147]
    start_list = random.sample(start_pokemon, 3)
    print(start_list)
    with open('./resources/pokemon_list.pkl', 'rb') as f:
        for i in range(1, 152):
            pokemon_list.append(pickle.load(f))

    app = Ursina()
    start_entity = [1,1,1]
    start_pos = [5, 0, -5]
    for i in range(3):
        start_entity[i] = Button(parent = scene, model = 'quad', position=(start_pos[i],1.5), highlight_color = color.white)
    
    random_starting_pokemon(pokemon_list, start_list, start_entity)
    app.run()