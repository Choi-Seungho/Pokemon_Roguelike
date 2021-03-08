from ursina import *
from Player import Player

class Tile(Button):
    def __init__(self, model, texture, p, scale, position, highlight_color=color.lime):
        super().__init__(parent = scene, model = model,texture = texture, color=color.white, scale = scale, position = position, highlight_color = highlight_color)
        self.p = p
    
    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                self.p.x, self.p.y = self.x, self.y
