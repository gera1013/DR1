import numpy as np
from gl import color, mathVectorSubstraction, mathDotProduct, mathFrobenius


WHITE = color(1, 1, 1)

class Material(object):
    # inicialización
    def __init__(self, diffuse = WHITE):
        # color del pixel
        self.diffuse = diffuse


class Intersect(object):
    def __init__(self, distance):
        self.distance = distance


class Sphere(object):

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        # Regresa falso o verdadero si hace interseccion con una esfera

        L = mathVectorSubstraction(self.center, orig)
        tca = mathDotProduct(L, dir)
        magnitude_L = mathFrobenius(L)

        d = (magnitude_L**2 - tca**2) ** 0.5
        
        if d > self.radius:
            return None

        # thc es la distancia de P1 al punto perpendicular al centro
        thc = (self.radius**2 - d**2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        
        if t0 < 0:
            t0 = t1

        if t0 < 0: # t0 tiene el valor de t1
            return None

        return Intersect(distance = t0)
