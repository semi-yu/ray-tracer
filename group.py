from util.transformation import Transformation

from entities.ray import Ray

from intersect import intersect, Intersection

class Group:
    def __init__(self):
        self._transform = Transformation()
        self._shapes = []

        self._parent = None

    def set_parent(self, group):
        self._parent = group
        return self

    def add_child(self, child):
        self._shapes.append(child)
        child.set_parent(self)
        return self
    
    def __getitem__(self, key: int):
        return self._shapes[key]
    
    def __len__(self):
        return len(self._shapes)

    def __contains__(self, member):
        return member in self._shapes
    
    def set_transform(self, transform: Transformation):
        self._transform = transform
        return self
    
    def local_intersect(self, ray: Ray) -> list[Intersection]:
        result = set()

        for shape in self._shapes:
            for it in intersect(shape, ray):
                result.add((it.t, it.object))

        result = [Intersection(t, ob) for t, ob in result]
        result.sort(key=lambda s: s.t)

        return result

    @property
    def transform(self):
        return self._transform

    @property
    def shapes(self):
        return self._shapes

    @property
    def parent(self):
        return self._parent