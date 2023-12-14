def f1(number):
    binary_list = []
    binary_string = ""

    while number > 0:
        remainder = number % 2
        binary_list.insert(0, remainder)
        binary_string += str(remainder)
        number //= 2

    print("Числото от десетична в двоична бройна система е:", binary_string)

    choice = input("Желаете ли проверка 2->10? (Y/N): ")
    if choice.upper() == 'Y':
        f2(binary_string)

def f2(binary_string):
    decimal_result = int(binary_string, 2)
    print("Числото от двоична в десетична бройна система е:", decimal_result)

input_number = int(input("Въведете цяло положително число: "))
f1(input_number)
