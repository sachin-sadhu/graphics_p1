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

p_1 = np.array([transformed_points[0][0], transformed_points[1][0], transformed_points[2][0]])
p_2 = np.array([transformed_points[0][1], transformed_points[1][1], transformed_points[2][1]])
p_3 = np.array([transformed_points[0][2], transformed_points[1][2], transformed_points[2][2]])
p_4 = np.array([transformed_points[0][3], transformed_points[1][3], transformed_points[2][3]])
p_5 = np.array([transformed_points[0][4], transformed_points[1][4], transformed_points[2][4]])
p_6 = np.array([transformed_points[0][5], transformed_points[1][5], transformed_points[2][5]])

v1 = p_2 - p_1
v2 = p_5 - p_1
v3 = p_6 - p_1
v4 = p_3 - p_1

v1_v2_dot_product = np.dot(v1, v2)
v1_v3_dot_product = np.dot(v1, v3)
v2_v3_dot_product = np.dot(v2, v3)

scalar_trip = np.dot(v1, np.cross(v2,v4))

if np.isclose(scalar_trip, 0):
    print("The points are coplanar")
else:
    print("The points are not coplanar")