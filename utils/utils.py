import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot_scatter(voxels, figsize=(8, 6)):

  fig = plt.figure(figsize)
  ax = Axes3D(fig)

  x_values = voxels[:, 0]
  y_values = voxels[:, 1]
  z_values = voxels[:, 2]
  ax.scatter(x_values, y_values, z_values)
  plt.show()


def plot_both_scatters(A, B, figsize=(8, 6)):

  fig = plt.figure(figsize)
  ax = Axes3D(fig)

  ax.scatter(A[:, 0], A[:, 1], A[:, 2], c='b')
  ax.scatter(B[:, 0], B[:, 1], B[:, 2], c='r')
  plt.show()
