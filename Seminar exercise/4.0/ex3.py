numbers = input("Enter numbers: ")
numbersSplit = numbers.split()

multiply = 1

for i in range(len(numbersSplit)):
    multiply *= int(numbersSplit[i])

print(multiply)