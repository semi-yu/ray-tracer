from image.canvas import Color


class Material:
    def __init__(
        self,
        color: Color = Color(1.0, 1.0, 1.0),
        ambient: float = 0.1,
        diffuse: float = 0.9,
        specular: float = 0.9,
        shininess: float = 200.0,
    ):
        self._color = color
        self._ambient = ambient
        self._diffuse = diffuse
        self._specular = specular
        self._shininess = shininess

    def set_color(self, color):
        self._color = color

    def set_ambient(self, ambient):
        self._ambient = ambient

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
