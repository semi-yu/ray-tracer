from util.transformation import Transformation


class Group:
    def __init__(self):
        self._transformation = Transformation()
        self._shapes = []

    def add_child(self, child):
        self._shapes.append(child)
        child.set_parent(self)
    
    def __len__(self):
        return len(self._shapes)

    def __contains__(self, member):
        return member in self._shapes

    @property
    def transformation(self):
        return self._transformation

    @property
    def shapes(self):
        return self._shapes
