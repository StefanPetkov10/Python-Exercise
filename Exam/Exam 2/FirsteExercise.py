def check_n():
    max_n = 35
    min_n = 15

    while True:
        n = int(input("Enter a number counter"))
        try:
            if n < min_n or n > max_n:
                raise ValueError("Invalid number")
            else:
                return n
        except ValueError as e:
                print(e)
n = check_n()

numbers = []
for _ in range(n):
    while True:
        number = int(input("Enter a number"))
        try:
            if number < 30 or number > 300:
                raise ValueError("Invalid number")
            else:
                numbers.append(number)
        except ValueError as e:
            print(e)

# numbers = [1, 2, 3, 4, 25, 16, 17, 33, 38,39, 47, 56, 66, 78, 79, 160, 101]

numbers_multiple_of_3 = [x for x in numbers if (x //10 % 10 % 3 == 0 and x//10 % 10 != 0) and x > 9]

numbers_to_find = [x for x in numbers if x % 6 == 4]
min_number = min(numbers_to_find)
print(min_number)
index_to_find = numbers.index(min_number)
print(index_to_find)

numbers2 = [x for x in numbers if 9 < x < 100 and (x % 2 == 0 or x % 3 == 0)]
print(numbers2)

odd_numbers = [x for x in numbers2 if x % 2 != 0]
print(odd_numbers)
sum_odd_numbers = sum(odd_numbers)
try:
    average = sum_odd_numbers / len(odd_numbers)
    print(average)
except ZeroDivisionError:
    print("You cannot divide by 0")

numbers2.remove(min(numbers2))
print(numbers2)