def calculate_sum(numbers):
    # Функцията изчислява сумата на всички числа в кортежа
    return sum(numbers)

def calculate_even_sum(numbers):
    even_sum = sum(num for num in numbers if num % 2 == 0)
    return even_sum


numbers = tuple(map(int, input("Въведете цели числа, разделени със запетая: ").split(', ')))

total_sum = calculate_sum(numbers)

print(f"Общата сума на числата в кортежа е: {total_sum}")

even_sum = calculate_even_sum(numbers)
print(f"Сумата на четните числа в кортежа е: {even_sum}")


