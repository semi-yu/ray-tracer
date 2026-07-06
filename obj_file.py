from util.mathematics import Point

from triangle import Triangle
from group import Group

class Parser:
    def __init__(self):
        self._vertices = [None]
        self._ignored = 0

        self._group = [Group()]
        self._default_group = self._group[0]

        self._name = {}

    def __getitem__(self, key: int = None):
        if key is None: return self._default_group
        return self._group[key]

    def add_vertices(self, point: Point):
        self._vertices.append(point)

    def add_group(self, name: str):
        self._name[name] = len(self._group)
        self._group.append(Group())
    
    def add_child(self, shape):
        self._group[-1].add_child(shape)

    def inc_ignored(self):
        self._ignored += 1

    @property
    def ignored(self):
        return self._ignored
    
    @property
    def vertices(self):
        return self._vertices
    
    @property
    def group(self):
        return self._group
    
    @property
    def shapes(self):
        return self._default_group.shapes
    
    @property
    def default_group(self):
        return self._default_group
    
def read_obj(path: str) -> list[str]:
    with open(path, "r") as f:
        content = f.read()

    return content.split('\n')

def parse_obj(content) -> tuple[list, int]:
    def fan_triangulation(vertices):
        triangles = []

        for i in range(1, len(vertices) - 1):
            t = Triangle(vertices[0], vertices[i], vertices[i + 1])
            triangles.append(t)
        
        return triangles

    data = Parser()

    for line in content:
        if line == '': continue

        preface = line[0]

        if preface == "v":
            x, y, z = map(float, line.split()[1:])
            data.add_vertices(Point(x, y, z))

        elif preface == "f":
            indices = list(map(int, line.split()[1:]))

            vertices = [data.vertices[i] for i in indices]
            shapes = fan_triangulation(vertices)
   
            for s in shapes: data.add_child(s)
        
        elif preface == "g":
            group_name = line.split(' ')[1]
            data.add_group(group_name)
        
        else:
            data.inc_ignored()
            continue

    return data

def obj_to_group(obj):
    g = Group()

    for subg in obj.group[1:]:
        g.add_child(subg)

    return g
