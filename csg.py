

def intersection_allowed(operation, has_left_hit, in_left, in_right):
    if operation == "union":
        return (has_left_hit and not in_right) or (not has_left_hit and not in_left)
    
    return False

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

