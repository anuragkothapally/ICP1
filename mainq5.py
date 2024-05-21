import math
radius = 30
_area_of_circle_ = math.pi * radius ** 2
print(f"Area of the circle with radius {radius} meters: {_area_of_circle_:.2f} square meters")
_circum_of_circle_ = 2 * math.pi * radius
print(f"Circumference of the circle with radius {radius} meters: {_circum_of_circle_:.2f} meters")
radius = float(input("Enter the radius of the circle (in meters): "))
area = math.pi * radius ** 2
print(f"Area of the circle with radius {radius} meters: {area:.2f} square meters")
