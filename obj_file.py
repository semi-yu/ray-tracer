from util.mathematics import Vector, Point

from triangle import Triangle, SmoothTriangle
from group import Group

class Parser:
    def __init__(self):
        self._vertices = [None]
        self._ignored = 0

        self._group = [Group()]
        self._default_group = self._group[0]

        self._normals = [None]

        self._name = {}

    def __getitem__(self, key: int = None):
        if key is None: return self._default_group
        return self._group[key]
    
    def add_normals(self, normal: Vector):
        self._normals.append(normal)

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
    
    @property
    def normals(self):
        return self._normals
    
def read_obj(path: str) -> list[str]:
    with open(path, "r") as f:
        content = f.read()

    return content.split('\n')

def parse_obj(content) -> tuple[list, int]:
    def fan_triangulation(
            vertices: list[Point],
            textures,
            normals: list[Vector],
            is_textured = False,
            is_smoothen = False):

        triangles = []

        for i in range(1, len(converted) - 1):
            if is_smoothen:
                t = SmoothTriangle(
                    vertices[0], vertices[i], vertices[i + 1],
                    normals[0], normals[i], normals[i + 1])
            else:
                t = Triangle(vertices[0], vertices[i], vertices[i + 1])

            triangles.append(t)
        
        return triangles

    def parse_f(record):
        result = [None, None, None]
        tokens = record.split('/')

        for i, token in enumerate(tokens):
            result[i] = None if token == "" else int(token)

        return tuple(result)     

    data = Parser()

    for line in content:
        if line == '': continue
        separated = line.split()
        preface = separated[0]

        if preface == "v":
            x, y, z = map(float, separated[1:])
            data.add_vertices(Point(x, y, z))

        elif preface == "f":
            converted = [parse_f(record) for record in separated[1:]]

            is_textured = converted[0][1] is not None
            is_smoothen = converted[0][2] is not None

            print(is_textured)

            vertices = [data.vertices[v] for v, _, _ in converted]
            textures = [] # [data.textures[t] for _, t, _ in converted] if is_textured else []
            normals = [data.normals[n] for _, _, n in converted] if is_smoothen else []

            shapes = fan_triangulation(vertices, textures, normals, is_textured, is_smoothen)
   
            for s in shapes: data.add_child(s)
        
        elif preface == "g":
            group_name = separated[1]
            data.add_group(group_name)

        elif preface == "vn":
            x, y, z = map(float, separated[1:])
            data.add_normals(Vector(x, y, z))
        
        else:
            data.inc_ignored()
            continue

    return data

def obj_to_group(obj):
    g = Group()

    for subg in obj.group[1:]:
        g.add_child(subg)

    return g
