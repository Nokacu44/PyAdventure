from enum import Enum

class Item():
    def __init__(self,name,cost,rarity) -> None:
        self.cost,self.rarity,self.name = cost,rarity,name

    def __repr__(self) -> str:
        return self.name

class Type(Enum):
    SLASH = 0
    STRIKE = 1
    RANGE  = 2
    MAGIC = 3

class Weapon(Item):
    def __init__(self, name, cost, rarity,damage,damage_type,block) -> None:
        super().__init__(name, cost, rarity)
        self.damage,self.block,self.type = damage,block,damage_type

SWORD = Weapon("Sword",5,1,7,Type.SLASH,1)