
max_number = 30
min_number = 20
def check_count_of_numbers(min_number, max_number):

    while True:
        count_of_numbers = int(input("Enter count of numbers: "))

        try:
            if (count_of_numbers > max_number or count_of_numbers < min_number):
                raise ValueError("Invalid number!")
            else:
                return count_of_numbers

        except ValueError as e:
            print(e)
count_of_numbers = check_count_of_numbers(min_number, max_number)

numbers = []

for i in range(5):
    while True:
        currentNumber = int(input('Enter number from -100 to 100: '))
        try:
            if currentNumber < -100 or currentNumber > 100:
                raise ValueError("Invalid number!")
            else:
                numbers.append(currentNumber)
                break
        except ValueError as e:
            print(e)

print(numbers)

def sum_of_odd_index(numbers):
    sum = 0
    for i in range(len(numbers)):
        if i % 2 != 0:
            sum += numbers[i]

    return sum

print(sum_of_odd_index(numbers))


# n = 10
# s = 160 // 10
# i = s % 10
# print(i)
# f = i % 2 == 0
# print(f) somthing for see the result

def count_of_even_digits(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] % 10 % 2 == 0:
            count += 1
    return count

print(count_of_even_digits(numbers))

def multiply_of_negative_numbers(numbers):
    multuply = 1
    for i in range(len(numbers)):
        if numbers[i] < 0 and numbers[i] % 2 == 0:
            multuply *= numbers[i]
    return multuply

print(multiply_of_negative_numbers(numbers))

print(sorted(numbers, reverse = True))

numbersTwo = []

for i in range(len(numbers)):
    if count_of_numbers < numbers[i]:
        numbersTwo.append(numbers[i])

max_elemnt = -1
min_element = 10000000000000

for i in range(len(numbersTwo)):
    if numbersTwo[i] > max_elemnt:
        max_elemnt = numbersTwo[i]

    if numbersTwo[i] < min_element:
        min_element = numbersTwo[i]

difference = max_elemnt - min_element

print(difference)
print(numbersTwo)

oddNumbers = []
count = 0
for i in range(len(numbersTwo)):
    if numbersTwo[i] % 2 == 0:
        oddNumbers.append(numbersTwo[i])
        count += 1
print(oddNumbers)
print(len(oddNumbers))

numbersTwo.remove(min_element)
print(numbersTwo)

