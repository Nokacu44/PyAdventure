
class Class():
    def __init__(self,hp,dp,ap,dx_weapon,sx_weapon,head,chest,legs) -> None:
        self.hp,self.dp,self.ap = hp,dp,ap
        self,dx_weapon,self.sx_weapon = dx_weapon,sx_weapon
        self.head,self.chest,self.legs = head,chest,legs

WARRIOR = Class(10,6,8,"sex","boh")