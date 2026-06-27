from util.transformation import Transformation

class Group:
    def __init__(self):
        self._transformation = Transformation()
        self._shapes = []
    
    @property
    def transformation(self):
        return self._transformation

    @property
    def shapes(self):
        return self._shapes
