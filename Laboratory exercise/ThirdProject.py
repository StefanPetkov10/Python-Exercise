#programa, koqto wywejvdame cqlo chislo, a programata formira dwa korteja systoqshti se ot
# pyrwiq kortej e ot 1 do N
# vtoriq na obratno

# number = input("number: ")
# list1 = []
# list2 = []
# for i in range(1, int(number) + 1):
#     list1.append(i)
#     list2.append(int(number) - i + 1)
# print(list1)
# print(tuple(list2))
#  ---------
# n = input("n: ")
# tuple1 = ()
#
# for i in range(0, len(n)):
#     tuple1 = tuple1 + (n[i],)
#
# print(tuple1)
# print(tuple1[::-1])

#--------------------------------

#suzdawa se chislov spisuk, zapulva se s random chisla, mejdu vsqka dvoika dobavqme novo chislo ot sbora mejdu tqh

# import random
# list1 = []
# for i in range(0, 10):
#     list1.append(random.randint(0, 100))
# print(list1)
# list2 = []
# for i in range(0, len(list1) - 1):
#     list2.append(list1[i] + list1[i + 1])
# print(list2)
#
# #--------------------------------
#
# #programa, koqto potrbitelq wywejda tekst i syzdawa rechnik, za kluch slujat bukvite a za value e kolko puti se sreshta tazi bukwa
#
# text = input("text: ")
# my_dictionary = {}
# count = 0
#
# for i in range(0, len(text)):
#     for j in range (0, len(text)):
#         if text[i] == text[j]:
#             count += 1
#     my_dictionary[text[i]] = count
#     count = 0
#
# print(my_dictionary)

#--------------------------------

#programa koqto namira lice na geometrichna figura - kvadrat, triygylnik , pravougulen triygylnik i presmqts liceto. s funkciq

# input = input("input: ").split(' ')
# a = int(input[1])
#
# if input[0] == 'square':
#     def square(a):
#         return a * a
#     print(square(a))
#
# if input[0] == 'triangle':
#     h = int(input[2])
#     def square(a, h):
#         return a * h / 2
#     print(square(a, h))
#
# if input[0] == 'right-angledTriangle':
#     b = int(input[2])
#     def square(a, b):
#         return a * b / 2
#     print(square(a, b))

#--------------------------------

#potrbitelska funkciq proverq palindrom chislo li e. wryshta 1 za wqrno i 0 za greshno

# number = input("number: ")
# def palindrome(number):
#     if number == number[::-1]:
#         return 1
#     else:
#         return 0
# print(palindrome(number))

#-------------------------------

#programa koqto realizira kalkulator ot celi chisla - sybirane, izvavdane, umnovenie i delenie. otdelni funkcii

# input = input("input: ").split(' ')
# a = int(input[0])
# b = int(input[2])
#
# sign= input[1]
#
# if sign == '+':
#     def addition(a, b):
#         return a + b
#     print(addition(a, b))
# elif sign == '-':
#     def subtraction(a, b):
#         return a - b
#     print(subtraction(a, b))
# elif sign == '*':
#     def multiplication(a, b):
#         return a * b
#     print(multiplication(a, b))
# elif sign == '/':
#     def division(a, b):
#         return a / b
#     print(division(a, b))

#--------------------------------

#na funkciq se podawat dwa argumenta, spisyk s chisla, a vtoriq prosto chislo. promenete wsichki cisla, koito sa po golemi ot chisloto s 0

# list1 = input("list: ").split(' ')
# number = input("number: ")
# def change(list1, number):
#     for i in range(0, len(list1)):
#         if int(list1[i]) > int(number):
#             list1[i] = 0
#     return list1
#
# print(change(list1, number))

#--------------------------------

#funkciq, koqto da prieama argument ime i godini. vtowa funkciq, koqto priema ryst i pol, koito sa adadeni i nie gi promenqme ot konzolata
# name = 'Stefan'
# age = 21
# def change(name, age):
#     name = input("name: ")
#     age = input("age: ")
#     return name, age
# print(change(name, age))
# hight = 175
# genger = 'man'
# def change(hight, genger):
#     hight = input("hight: ")
#     genger = input("genger: ")
#     return hight, genger
# print(change(hight, genger))

def bubble_sort(input_list):
    n = len(input_list)

    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]


# Example usage:
unsorted_list = [64, 25, 12, 22, 11]
print("Unsorted List:", unsorted_list)

# Call the bubble_sort function to sort the list
bubble_sort(unsorted_list)

print("Sorted List:", unsorted_list)
