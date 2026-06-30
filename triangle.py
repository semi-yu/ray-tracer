from shape import Shape

from util.mathematics import Point

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()
    
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

        self._e1 = self._p2 - self._p1
        self._e2 = self._p3 - self._p1

        self._normal = self._e2.cross(self._e1).normalize()


    @property
    def p1(self):
        return self._p1
 
    @property
    def p2(self):
        return self._p2

    @property
    def p3(self):
        return self._p3

    @property
    def e1(self):
        return self._e1
    
    @property
    def e2(self):
        return self._e2
    
    @property
    def normal(self):
        return self._normal
