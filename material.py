from pattern import Pattern

from image.canvas import Color


class Material:
    def __init__(
        self,
        color: Color = Color(1.0, 1.0, 1.0),
        ambient: float = 0.1,
        diffuse: float = 0.9,
        specular: float = 0.9,
        shininess: float = 200.0,
        reflective: float = 0.0,
        transparency: float = 0.0,
        reflective_index: float = 1.0,
        pattern: Pattern = None,
    ):
        self._color = color
        self._ambient = ambient
        self._diffuse = diffuse
        self._specular = specular
        self._shininess = shininess
        self._reflective = reflective
        self._transparency = transparency
        self._reflective_index = reflective_index

        self._pattern = pattern

    def set_color(self, color):
        self._color = color
        return self

    def set_ambient(self, ambient):
        self._ambient = ambient
        return self
    
    def set_diffuse(self, diffuse):
        self._diffuse = diffuse
        return self
    
    def set_specular(self, specular):
        self._specular = specular
        return self

    def set_pattern(self, pattern):
        self._pattern = pattern
        return self
    
    def set_transparency(self, transparency):
        self._transparency = transparency
        return self 

    def set_reflective_index(self, reflective_index):
        self._reflective_index = reflective_index
        return self

    @property
    def color(self):
        return self._color

    @property
    def ambient(self):
        return self._ambient

    @property
    def diffuse(self):
        return self._diffuse

    @property
    def specular(self):
        return self._specular

    @property
    def shininess(self):
        return self._shininess

    @property
    def pattern(self):
        return self._pattern
    
    @property
    def reflective(self):
        return self._reflective

    @property
    def transparency(self):
        return self._transparency

    @property
    def reflective_index(self):
        return self._reflective_index
