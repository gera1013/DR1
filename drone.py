from gl import RayTracer, color
from sphere import Sphere, Material
import random

snow = Material(diffuse = color(1, 1, 1))
buttons = Material(diffuse = color(0, 0, 0))
eyes = Material(diffuse = color(0.8, 0.8, 0.8))
mouth = Material(diffuse = color(134 / 255, 124 / 255, 128 / 255))
carrot = Material(diffuse = color(239 / 255, 114 / 255, 21 / 255))

width = 600
height = 700
r = RayTracer(width, height)

# fondo nevado
r.glBackground(175 / 255, 207 / 255, 230 / 255)

# body
r.scene.append(Sphere([0, -1.4,  -7], 1.2, snow))
r.scene.append(Sphere([0, 0.2, -7], 1, snow))
r.scene.append(Sphere([0, 1.6, -7], 0.8, snow))

# buttons
r.scene.append(Sphere([0, -1.4,  -6], 0.27, buttons))
r.scene.append(Sphere([0, -0.6,  -6], 0.2, buttons))
r.scene.append(Sphere([0, 0.2, -6], 0.2, buttons))

# nose 
r.scene.append(Sphere([0, 1.4, -6], 0.15, carrot))

# eyes
r.scene.append(Sphere([0.2, 1.64, -5.9], 0.07, buttons))
r.scene.append(Sphere([-0.2, 1.64, -5.9], 0.07, buttons))
r.scene.append(Sphere([0.2, 1.7, -6], 0.1, eyes))
r.scene.append(Sphere([-0.2, 1.7, -6], 0.1, eyes))

# mouth
r.scene.append(Sphere([0.1, 1.1, -6], 0.07, mouth))
r.scene.append(Sphere([-0.1, 1.1, -6], 0.07, mouth))
r.scene.append(Sphere([0.3, 1.2, -6], 0.07, mouth))
r.scene.append(Sphere([-0.3, 1.2, -6], 0.07, mouth))

r.glRayTracingRender()

r.glFinish('snowman.bmp')