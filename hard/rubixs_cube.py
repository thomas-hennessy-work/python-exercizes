from abc import abstractmethod

class Rubixs_cube():
    # Values
    # 0 = white
    # 1 = orange
    # 2 = blue
    # 3 = yellow
    # 4 = green
    # 5 = red

    # Positions
    # TL = 0   TC = 1   TR = 2
    # ML = 3   MC = 4   MR = 5
    # BL = 6   BC = 7   BR = 8

    def __init__(self, front, back, left, right, up, down):
        self.sides = [front, back, left, right, up, down]


    def spin(self, side, times):
        
