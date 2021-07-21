import numpy as np
import random
import trimesh
from sklearn.preprocessing import MinMaxScaler


def load_random_cuboid(a, b, h, density=1000):
  points = []

  for _ in range(density):
    wall = random.randint(1, 6)
    x = random.random() * a
    y = random.random() * h
    z = random.random() * b

    if wall == 1:
      points.append([x, y, 0])
    elif wall == 2:
      points.append([x, y, b])
    elif wall == 3:
      points.append([x, 0, z])
    elif wall == 4:
      points.append([x, h, z])
    elif wall == 5:
      points.append([0, y, z])
    elif wall == 6:
      points.append([a, y, z])

  return np.array(points)


def load_bunny(density=1000):

  mesh = trimesh.load_mesh('/content/robotics/data/bunny.stl')
  bunny = mesh.sample(density)
  scaler = MinMaxScaler(feature_range=(0, 1))
  bunny = scaler.fit_transform(bunny)

  return np.array(bunny)
