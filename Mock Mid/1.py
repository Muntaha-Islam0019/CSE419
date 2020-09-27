import math

BC = int(input())

radius = (BC / math.sqrt(2)) / 2

area_of_circle = math.pi * (radius ** 2)
area_of_square = 4 * (radius ** 2) * math.cos(45) * math.sin(45)

print(area_of_circle)
print(area_of_square)
