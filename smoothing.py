from triangle import Triangle

from util.mathematics import Vector, Point

class SmoothTriangle(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point, n1: Vector, n2: Vector, n3: Vector):
        super().__init__(p1, p2, p3)

        self._n1 = n1
        self._n2 = n2
        self._n3 = n3

    def local_normal_at(self, point: Point, hit):
        return hit.u * self.n2 + \
               hit.v * self.n3 + \
               (1 - hit.u - hit.v) * self.n1

    @property
    def n1(self):
        return self._n1
    
    @property
    def n2(self):
        return self._n2
    
    @property
    def n3(self):
        return self._n3
