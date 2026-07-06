from util.mathematics import Vector, Point

class SmoothTriangle:
    def __init__(self, p1: Point, p2: Point, p3: Point, n1: Vector, n2: Vector, n3: Vector):
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3
        self._n1 = n1
        self._n2 = n2
        self._n3 = n3
    
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
    def n1(self):
        return self._n1
    
    @property
    def n2(self):
        return self._n2
    
    @property
    def n3(self):
        return self._n3
