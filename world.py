class World:
    def __init__(self):
        self._light = None
        self._objects = []

    def set_light(self, l):
        self._light = l
        return self

    def add_object(self, o):
        self._objects.append(o)
        return self

    @property
    def objects(self):
        return self._objects

    @property
    def light(self):
        return self._light
