
# a = input("a: ")
# b = input("b: ")
# h = input("h:")
#
# area = round(0.5 * (float(a) + float(b)) * float(h), 3)
# print("Area of the trapezoid:", area)

# ---------------------

# parametur i lice na krug
# R = input("R: ")
# pi = 3.14
# S = round(pi * float(R) ** 2, 2)
# P = round(2 * pi * float(R), 2)

# print("S: ", S)
# print("P: ", P)

# ----------------------

# hours = input("hours: ")
# price = input("price: ")
#
# if int(hours) > 40:
#     salary = round((float(hours) - 40) * float(price) * 1.5 + 40 * float(price), 2)
# else :
#     salary = round(float(hours) * float(price), 2)
# print("salary: ", salary)

# ----------------------

# year = input("year: ")
# if int(year) % 4 == 0:
#     print("Visokosna")
# else:
#     print("Ne e visokosna")

# ----------------------

# year1 = input("year1: ")
# year2 = input("year2: ")
# if int(year1)  > int(year2):
#     year1, year2 = year2, year1
# for i in range(int(year1), int(year2) + 1):
#     if i % 4 == 0:
#         print(i)

# ----------------------

# name = input("Name: ")
# age = input("Age: ")
# town = input("Town: ")
#
# print(f"Hello, my name is {name} and my age are {age}. I am from {town}")
# print(f"Hello, my name is {} and my age are {}. I am from {}".format(name, age, town))

# ----------------------

# txt = "Hello, my name is {} and my age are {}. I am from {}"
# print(txt.format(name = input("Name"), age = input("Age: "),town = input("Town: "))) error

# ----------------------

# number = input("number: ")
# if int(number) % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# ----------------------

number1 = input("number1: ")
number2 = input("number2: ")
if int(number1)  > int(number2):
    year1, year2 = number2, number1
for i in range(int(number1), int(number2) + 1):
    if i % 2 == 0:
        print(f"{i} Even")
    else :
        print(f"{i} Odd")

