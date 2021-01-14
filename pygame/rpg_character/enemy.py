#gparap 06-11-2016
from rpg_character.character import *

class CEnemy(CCharacter):
    def __init__(self, name, hit_points, strength):
        CCharacter.__init__(self, name, hit_points)
        self.strength = strength
