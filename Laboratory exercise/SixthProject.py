# from MyModule import print_hello
#
# print_hello()
# #-------------
# # def main():
# #     print_hello()
# #
# # if __name__ == "__main__":
# #     main()

#--------------------------------------

#prilojenie za izhiclesnie na liceto na geometrichni figuri -
#pravougulnik kvadrat triugulnik romb i trapec. Stranite i visochinite se vuvejdat kato vhodni danni

# from Area import square, rectangle, triangle, rhombus, trapezoid
#
# a = int(input("a: "))
# b = int(input("b: "))
# h = int(input("h: "))
#
# print("Square: ", square(a))
# print("Rectangle: ", rectangle(a, b))
# print("Triangle: ", triangle(a, h))
# print("Rhombus: ", rhombus(a, h))
# print("Trapezoid: ", trapezoid(a, b, h))

#--------------------------------------

#prilojenie za realizirane na kalkulator za operaciite sybirane izvajdane umnojenie i delenie.
#Chislata se vuvejdat kato vhodni danni

# from Calculate import addition, subtraction, multiplication, division
#
# input = input("input: ").split(' ')
#
# num1 = int(input[0])
# sign = input[1]
# num2 = int(input[2])
#
# if sign == '+':
#     print("Addition: ", addition(num1, num2))
# elif sign == '-':
#     print("Subtraction: ", subtraction(num1, num2))
# elif sign == '*':
#     print("Multiplication: ", multiplication(num1, num2))
# elif sign == '/':
#     print("Division: ", division(num1, num2))
# else:
#     print("Invalid sign")

#----------------------------------------------------

#3 modula. Purwi recepta - kalkulira kolko e cenata, vtorata funkciq da convert kum string
#vtori modul - proverqva dali e nalichen i vtorata funkciq update
#treti modul - osnowen - imame recepta, nalicni produkti v hladilnika

# from WeCheckIfWeHave import check_if_we_have
# from MakeRecipe import make_salat
#
# availability = {'tomato': 3,
#                 'cocumber': 4,
#                 'cheese': 2,
#                 'meat': 2,
#                 'bread': 1}
#
# price = {'tomato': 5.2,
#             'cucumber': 3.0,
#             'cheese': 4.3,
#             'meat': 10.5,
#             'bread': 1.8}
#
#
# recipe = input("Enter a recipe: ")
#
# check_if_we_have(recipe, availability, price)
# if recipe == "Salat":
#     make_salat(availability)
#

#----------------------------------------------------

# modul, funkciq za sreden uspeh, vtorata za priswuqwane na tochki

from AverageGrade import average_grade, finalResult

gradesList = []
grades = input("Enter your grades: ").split(' ')

for grade in grades:
    gradesList.append(int(grade))

print("{:.2f}".format(average_grade(gradesList)))
print(average_grade(gradesList).__round__(2))
print(finalResult(average_grade(gradesList)))