import matplotlib.pyplot as plt

class MObject:
    def __init__(self,_axes = None):
        self.figure = None
        self.axes = None
        if self.axes == None:
            if _axes == None:
                self.figure, self.axes = plt.subplots(figsize=(4,4))
            else:
                self.axes = _axes
        else:
            if _axes == None:
                pass
            else:
                self.axes = _axes

    def draw(self):
        pass

    def __call__(self):
        return self.draw()
    
    def show(self):
        plt.show()