import math
def distance_between_points(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

A = [5, 1]
B = [-2, 18]
distance = distance_between_points(A, B)
print(distance)