# -*- coding: utf-8 -*-
class StripFoundation(object):

    def __init__(self, resistance_soil, vertical_force, height_foundation):
        self.resistance_soil = float(resistance_soil)
        self.vertical_force = float(vertical_force)
        self.height_foundation = height_foundation

    def width(self):
        width = self.vertical_force/(self.resistance_soil-2.0*self.height_foundation)
        return 'Требуемая ширина подошвы = %.2f м.' % width

A = StripFoundation(10, 0.871, 1.6)
print A.width()