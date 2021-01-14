#gparap 06-11-2016
from rpg_character.character import *

class CHero(CCharacter):
    def __init__(self, name, hit_points, strength, intelligence):
        CCharacter.__init__(self, name, hit_points)
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity  = 10
        self.magic      = 10
        self.experience = 10
        self.level      = 10
