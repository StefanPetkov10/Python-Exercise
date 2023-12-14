def set_gen(numbers_list):
    result_set = set()

    for num in numbers_list:
        occurrences = numbers_list.count(num)

        if occurrences == 1:

            result_set.add(num)
        else:
            result_set.add(str(num) * occurrences)

    return result_set

user_input = input("Enter a numbers separated by commas: ")
numbers_list = user_input.split(",")

result_set = set_gen(numbers_list)
print(result_set)
