import numpy as np
import math

def matrix2array(T):
    '''
    Returns 6-elem array referring to 4x4 transformation matrix
    '''
    beta = -math.asin(T[2][0])
    alpha = math.asin(T[2][1] / math.cos(beta))
    gamma = math.acos(T[0][0] / math.cos(beta))
    x = T[0][3]
    y = T[1][3]
    z = T[2][3]
    return np.array([x, y, z, alpha, beta, gamma])
