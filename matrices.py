import numpy as np
import math

translation = np.array([
    [1,0,0,2],
    [0,1,0,0],
    [0,0,1,1],
    [0,0,0,1]
])

scaling = np.array([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,0.9,0],
    [0,0,0,1]
])

cos_value = math.cos(0.2)
sin_value = math.sin(0.2)

rotation = np.array([
    [pow(cos_value,2), -sin_value, cos_value * sin_value, 0],
    [cos_value * sin_value, cos_value, pow(sin_value,2), 0],
    [-sin_value, 0, cos_value, 0],
    [0, 0, 0, 1],
])

overall_transformation = np.matmul(rotation, np.matmul(scaling,translation))

points = np.array([
    [0, -1.5, -1, 1, 1.5, 0, -3, -2, 2, 3],
    [1, 0.5, -1, -1, 0.5, 2, 1, -2, -2, 1],
    [1, 1, 1, 1, 1, -1, -1, -1, -1, -1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
])

transformed_points = np.matmul(overall_transformation, points)

print(transformed_points)
