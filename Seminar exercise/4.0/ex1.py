numbers = input("Enter numbers: ")
numbersSplit = numbers.split()

sumPositive = 0
sumNegative = 0

for i in range(len(numbersSplit)):
    if int(numbersSplit[i]) > 0:
        sumPositive += int(numbersSplit[i])
    else:
        sumNegative += int(numbersSplit[i])

print("Sum of positive numbers: ", sumPositive)
print("Sum of negative numbers: ", sumNegative)