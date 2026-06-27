from util.transformation import Transformation

from entities.ray import Ray

from intersect import intersect, Intersection

class Group:
    def __init__(self):
        self._transformation = Transformation()
        self._shapes = []

    def add_child(self, child):
        self._shapes.append(child)
        child.set_parent(self)
        return self
    
    def __len__(self):
        return len(self._shapes)

    def __contains__(self, member):
        return member in self._shapes
    
    def local_intersect(self, ray: Ray) -> list[Intersection]:
        result = set()

        for shape in self._shapes:
            for it in intersect(shape, ray):
                result.add((it.t, it.object))

        result = [Intersection(t, ob) for t, ob in result]
        result.sort(key=lambda s: s.t)

        return result

    @property
    def transformation(self):
        return self._transformation

    @property
    def shapes(self):
        return self._shapes
