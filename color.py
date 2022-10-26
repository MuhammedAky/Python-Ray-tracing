from vector import Vector

class Color(Vector):

    @classmethod
    def from_hex(cls, hecolor = "#000000"):
        x = int(hecolor[1:3], 16) / 255.0
        y = int(hecolor[3:5], 16) / 255.0
        z = int(hecolor[5:7], 16) / 255.0

        return cls(x,y,z)