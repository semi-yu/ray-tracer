from entities.ray import Ray
from intersect import intersect
from group import Group

from util.transformation import Transformation

def includes(a, b):
    if isinstance(a, Group):
        return any(includes(child, b) for child in a.shapes)
    elif isinstance(a, Csg):
        return includes(a.left, b) or includes(a.right, b)
    else:
        return a == b


def intersection_allowed(operation, has_left_hit, in_left, in_right):
    if operation == "union":
        return (has_left_hit and not in_right) or (not has_left_hit and not in_left)
    elif operation == "intersection":
        return (has_left_hit and in_right) or (not has_left_hit and in_left)
    elif operation == "difference":
        return (has_left_hit and not in_right) or (not has_left_hit and in_left)
    
    return False

def filter_intersections(csg, intersections):
    in_left, in_right = False, False

    result = []

    for intersection in intersections:
        has_left_hit = includes(csg.left, intersection.object)

        if intersection_allowed(csg.operation, has_left_hit, in_left, in_right):
            result.append(intersection)
        
        if has_left_hit: in_left = not in_left
        else: in_right = not in_right
    
    return result

class Csg:
    def __init__(self, operation: str, left, right):
        self._operation = operation
        self._parent = None
        self._left = left
        self._right = right

        self._left.set_parent(self)
        self._right.set_parent(self)

        self._transformation = Transformation()

    def set_transform(self, transform: Transformation):
        self._transformation = transform
        return self

    def local_intersect(self, ray: Ray):
        left_xs = intersect(self.left, ray)
        right_xs = intersect(self.right, ray)

        result = left_xs + right_xs
        result.sort(key = lambda e: e.t)

        return filter_intersections(self, result)

    @property
    def operation(self):
        return self._operation
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right

    @property
    def transform(self):
        return self._transformation
    
    @property
    def parent(self):
        return self._parent

