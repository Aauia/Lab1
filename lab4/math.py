import math

# Example 1
angle_degrees = int(input())
angle_radians = math.radians(angle_degrees)

print(angle_radians)

# Example 2
height = float(input())
base1 = float(input())
base2 = float(input())

area_triangle = 0.5 * (base1 + base2) * height

print(area_triangle)

# Example 3
from math import tan, pi

num_sides = int(input())
side_length = float(input())
polygon_area = num_sides * (side_length ** 2) / (4 * tan(pi / num_sides))

print(polygon_area)

# Example 4
base = float(input())
height = float(input())
area_rectangle = base * height

print(area_rectangle)
