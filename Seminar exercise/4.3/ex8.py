import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

D = b * b - 4 * a * c

if D > 0:
    x1 = float((-b + math.sqrt(D)) / (2 * a))
    x2 = float((-b - math.sqrt(D)) / (2 * a))
    print("x1 = ", x1)
    print("x2 = ", x2)
elif D == 0:
    x = float(-b / (2 * a))
    print("x = ", x)
else:
    print("No roots")