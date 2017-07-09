"""
Your object will be instantiated and called as such:
sf = ShapeFactory()
shape = sf.getShape(shapeType)
shape.draw()
"""
class Shape(object):
    # def __init__():
    #
    def draw(self):
        raise NotImplementedError('This method should have implemented.')

class Rectangle(Shape):
    # Write your code here
    def __init__(self):
        super(Rectangle,self).__init__()
    def draw(self):
        print '  ----'
        print ' |    |'
        print ' |    |'
        print '  ----'

class Triangle(Shape):
    # Write your code here
    def __init__(self):
        super(Triangle, self).__init__()


    def draw(self):
        print '   /\ '
        print '  /  \ '
        print ' /____\ '


class Square(Shape):
    # Write your code here
    def __init__(self):
        super(Square, self).__init__()


    def draw(self):
        print '  ----'
        print ' |    |'
        print '  ----'


class ShapeFactory:
    # @param {string} shapeType a string
    # @return {Shape} Get object of type Shape
    def getShape(self, shapeType):
        # Write your code here
        if shapeType == 'Rectangle':
            return Rectangle()
        elif shapeType == 'Triangle':
            return Triangle()
        elif shapeType == 'Square':
            return Square()
        else:
            return None

if __name__ == "__main__":
    sf = ShapeFactory()
    shape = sf.getShape('Rectangle')
    shape.draw()
    shape = sf.getShape('Triangle')
    shape.draw()