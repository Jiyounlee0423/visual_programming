import matplotlib.pyplot as plt
import matplotlib.patches
from Point import Point

class Rectangle(Point):
    def __init__(self, x, y, w, h, _axes=None):
        super().__init__(x, y, _axes)
        self.w = w
        self.h = h
    
    def draw(self):
        super().draw()
        rect = matplotlib.patches.Rectangle((self.x, self.y), self.w, self.h, 
                                            ec = 'cyan', fc = 'aliceblue', fill=True, 
                                            label = 'Rectangle')
        self.axes.add_patch(rect)
        return self.axes
    
if __name__ == "__main__":
    Rectangle = Rectangle(7, 8, 4, 4)
    Rectangle.draw()
    Rectangle.show()
