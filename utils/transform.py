import numpy as np
from math import *
import random
from pyquaternion import Quaternion


def rotate_by_euler_angles(euler_angles):

  [a, b, g] = euler_angles

  R = np.array([[cos(a) * cos(b),
                 cos(a) * sin(b) * sin(g) - sin(a) * cos(g),
                 cos(a) * sin(b) * cos(g) + sin(a) * sin(g)],
                [sin(a) * cos(b),
                 sin(a) * sin(b) * sin(g) + cos(a) * cos(g),
                 sin(a) * sin(b) * cos(g) - cos(a) * sin(g)],
                [-sin(b),
                 cos(b) * sin(g),
                 cos(b) * cos(g)]])
  return R


def rotate_by_axis_and_angle(axis, theta):

  [ux, uy, uz] = axis
  c = cos(theta)
  s = sin(theta)

  R = np.array([[c + ux*ux*(1-c), ux*uy*(1-c) - uz*s, ux*uz*(1-c) + uy*s],
                [uy*ux*(1-c) + uz*s, c + uy*uy*(1-c), uy*uz*(1-c) - ux*s],
                [uz*ux*(1-c) - uy*s, uz*uy*(1-c) + ux*s, c + uz*uz*(1-c)]])
  return R


def rotate_by_quaternion(axis, theta):

  [a, b, c, d] = Quaternion(axis=axis, angle=theta)
  # axis = axis / np.sqrt(np.dot(axis, axis))
  # a = cos(theta / 2.)
  # [b, c, d] = -axis * sin(theta / 2.)

  R = np.array([[a*a+b*b-c*c-d*d, 2 * (b*c-a*d), 2 * (b*d+a*c)],
                [2 * (b*c+a*d), a*a+c*c-b*b-d*d, 2 * (c*d-a*b)],
                [2 * (b*d-a*c), 2 * (c*d+a*b), a*a+d*d-b*b-c*c]])
  return R


def rotation_matrix(euler_angles=None, axis=None, theta=0):

  if euler_angles is not None and axis is None:
    R = rotate_by_euler_angles(euler_angles)

  elif axis is not None and euler_angles is None:
    R = rotate_by_axis_and_angle(axis, theta)

  return R


def translation_vector([x, y, z]):
  t = np.array([x, y, z])
  return t.reshape(3, 1)


def transformation_matrix([x, y, z, a, b, g]):

  R = rotation_matrix(a, b, g)
  t = translation_vector(x, y, z)
  T = np.column_stack((R, t))
  T = np.vstack((T, [0, 0, 0, 1]))
  return T


def randomize_rotation(degree_range=180):

  a = radians(random.random() * degree_range)
  b = radians(random.random() * degree_range)
  g = radians(random.random() * degree_range)

  return rotation_matrix(euler_angles=[a, b, g])


def randomize_translation(range=1):

  x = random.random() * range
  y = random.random() * range
  z = random.random() * range

  return translation_vector([x, y, z])


def randomize_transformation(range=1, degree_range=180):

  R = randomize_rotation(degree_range=degree_range)
  t = randomize_translation(range=range)
  T = np.column_stack((R, t))
  T = np.vstack((T, [0, 0, 0, 1]))
  return T
