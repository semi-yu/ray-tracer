import numpy as np


class Environment:
    def __init__(self, gravity: np.array, drag: np.array):
        self._gravity = gravity
        self._drag = drag

    @property
    def gravity(self):
        return self._gravity

    @property
    def drag(self):
        return self._drag


class Projectile:
    def __init__(self, velocity: np.array, position: np.array):
        self._velocity = velocity
        self._position = position

    @property
    def velocity(self):
        return self._velocity

    @property
    def position(self):
        return self._position


def tick(env, proj):
    vel = proj.velocity + env.gravity + env.drag
    pos = proj.position + proj.velocity

    return Projectile(vel, pos)
