import math

from shape import Shape

from entities.ray import Ray
from intersect import UVIntersection
from util.mathematics import Vector, Point

class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()
    
        self._p1 = p1
        self._p2 = p2
        self._p3 = p3

        self._e1 = self._p2 - self._p1
        self._e2 = self._p3 - self._p1

        self._normal = self._e2.cross(self._e1).normalize()

    def local_normal_at(self, point: Point, hit: UVIntersection = None) -> Vector:
        return self._normal
    
    def local_intersect(self, ray: Ray) -> list[UVIntersection]:
        direct_cross = ray.direction.cross(self._e2)

        determinant = self._e1.dot(direct_cross)
        if math.isclose(abs(determinant), 0.0): return []

        f = 1.0 / determinant

        p1_to_origin = ray.origin - self.p1
        u = f * p1_to_origin.dot(direct_cross)
        if u < 0 or u > 1: return []

        edge_cross = p1_to_origin.cross(self.e1)
        v = f * ray.direction.dot(edge_cross)
        if v < 0 or  (u + v) > 1: return []

        t = f * self.e2.dot(edge_cross)
        return [UVIntersection(t, self, u, v)]

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

class SmoothTriangle(Triangle):
    def __init__(self, p1: Point, p2: Point, p3: Point, n1: Vector, n2: Vector, n3: Vector):
        super().__init__(p1, p2, p3)

        self._n1 = n1
        self._n2 = n2
        self._n3 = n3

    def local_normal_at(self, point: Point, hit: UVIntersection):
        print(hit, self.n1, self.n2, self.n3)
        if hit.u is None or hit.v is None: return self._normal

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
