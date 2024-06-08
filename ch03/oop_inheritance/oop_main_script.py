import matplotlib.pyplot as plt
import matplotlib
import Circle
import Point
import Rectangle

def test_external_axes():
    fig, axes = plt.subplots(figsize=(10,10))
    line = Point.Point(5,5,axes)
    axes = line.draw()
    circle = Circle.Circle(10,10,2,axes)
    circle.draw()
    rectangle = Rectangle.Rectangle(6,6,2,2,axes)
    rectangle.draw()
    plt.title("Point&Circle&Rectangle")
    plt.legend()
    plt.show()

def test_internal_axes():
    line = Point.Point(5,5)
    axes = line.draw()
    circle = Circle.Circle(10,10,2,axes)
    circle.draw()
    circle.show()
    rectangle = Rectangle.Rectangle(6,6,2,2,axes)
    rectangle.draw()
    rectangle.show()
    

if __name__ == "__main__":
    print(matplotlib.__version__)
    test_external_axes()
    #test_internal_axes()
