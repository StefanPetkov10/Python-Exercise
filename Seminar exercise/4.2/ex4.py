#A
def product ():
    numbers = []
    while True:
        try:
            user_input = input("Enter a number or 'done' to finish: ")
            if user_input == 'done':
                break
            number = int(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please try again.")

    product_of_numbers = 1
    for number in numbers:
        product_of_numbers *= number

    return product_of_numbers

result = product()
print(result)

#B
def product_of_numbers(args):
    product = 1
    for num in args:
        product *= num
    return product

result = product_of_numbers([1, 2, 3, 4, 5])
print(result)

#C
def product_function():
    def Funct(numbers_tuple=([1, 2, 3, 4])):
        def product_of_tuple(numbers):
            result = 1
            for num in numbers:
                result *= num
            return result

        return 0.5 * product_of_tuple(numbers_tuple)

    return Funct

result = product_function()
print(result())