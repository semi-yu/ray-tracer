
class Csg:
    def __init__(self, operation: str, left, right):
        self._operation = operation
        self._left = left
        self._right = right

        self._left.set_parent(self)
        self._right.set_parent(self)

    @property
    def operation(self):
        return self._operation
    
    @property
    def left(self):
        return self._left
    
    @property
    def right(self):
        return self._right
