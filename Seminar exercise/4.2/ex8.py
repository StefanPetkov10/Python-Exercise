import math

def circle_calculations(radius):
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    return area, perimeter


def rectangle_calculations(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


def triangle_calculations(height, sideBase, side2, side3):
    perimeter = sideBase + side2 + side3
    area = height * sideBase / 2
    return area, perimeter


print("Изберете фигура:")
print("1. Кръг")
print("2. Правоъгълник")
print("3. Триъгълник")

choice = int(input("Въведете номера на избраната фигура: "))


if choice == 1:
    radius = float(input("Въведете радиус на кръга: "))
    area, perimeter = circle_calculations(radius)
elif choice == 2:
    length = float(input("Въведете дължина на правоъгълника: "))
    width = float(input("Въведете ширина на правоъгълника: "))
    area, perimeter = rectangle_calculations(length, width)
elif choice == 3:
    height = float(input("Въведете височина на триъгълника: "))
    sideBase = float(input("Въведете дължина на главната страна: "))
    side2 = float(input("Въведете дължина на страна 2: "))
    side3 = float(input("Въведете дължина на страна 3: "))
    area, perimeter = triangle_calculations(height, sideBase, side2, side3)
else:
    print("Невалиден избор")


print(f"Лице: {area}")
print(f"Периметър: {perimeter}")
