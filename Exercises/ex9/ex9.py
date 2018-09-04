import math


class Parallelogram():
    '''A class to represent a parallelogram'''

    def __init__(self, base, side, theta):
        '''(Parallelogram, float, float, float) -> NoneType
        Set up a new Parallelogram with a give base, height and angle.
        REQ: base > 0
        REQ: side > 0
        REQ: 0 < theta < 180
        '''
        self._base = base
        self._side = side
        self._theta = theta

    def area(self):
        '''(Parallelogram) -> float
        Returns the area of a parallelogram given the base length, side length
        and the interior angle of two adjacent sides (in degrees).
        '''
        # convert angle to radians
        rad_theta = math.radians(self._theta)

        # calculate the area
        area = self._base * self._side * math.sin(rad_theta)
        return area

    def bst(self):
        '''(Parallelogram) -> float
        Returns the base length, side length, and interior angle of
        two adjacent sides (in degrees) of the parallelogram arranged in a list
        '''
        # arrange the given parameters into a list
        bst_list = [self._base, self._side, self._theta]
        return bst_list

    def __str__(self):
        '''(Parallelogram) -> str
        Returns a string sentence stating the area of the parallelogram.
        '''
        shape_name = type(self).__name__  # Get the name of the class

        statement = "I am a " + shape_name + " with area " + str(self.area())
        return statement


class Rectangle(Parallelogram):
    '''A class to represent a rectangle'''

    def __init__(self, base, side):
        '''(Rectangle, float, float) -> NoneType
        Set up a new Parallelogram with a give base, height and angle.
        REQ: base > 0
        REQ: side > 0
        '''
        Parallelogram.__init__(self, base, side, 90.0)


class Rhombus(Parallelogram):
    '''A class to represent a rhombus'''

    def __init__(self, base, theta):
        '''(Rhombus, float, float) -> NoneType
        Set up a new Rhombus with a give base, height and angle.
        REQ: base > 0
        REQ: 0 < theta < 180
        '''
        Parallelogram.__init__(self, base, base, theta)


class Square(Rectangle, Rhombus):
    '''A class to represent a square'''

    def __init__(self, base):
        '''(Square, float) -> NoneType
        Set up a new Parallelogram with a give base, height and angle.
        REQ: base > 0
        REQ: side > 0
        '''
        Rectangle.__init__(self, base, base)

if (__name__ == "__main__"):
    parallel = Parallelogram(4.0, 5.0, 30.0)
    rectangle = Rectangle(3, 5)
    square = Square(4)
    rhombus = Rhombus(4, 30.0)
