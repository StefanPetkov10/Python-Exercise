n = input("Enter count: ")
sumEven = 0
sumOdd = 0
averageEven = 0
averageOdd = 0

countEven = 0

for i in range(0, int(n)):
    inputNum = input("Enter number: ")
    if int(inputNum) % 2 == 0:
        sumEven += int(inputNum)
        countEven += 1
    else:
        sumOdd += int(inputNum)

averageEven = sumEven / countEven
averageOdd = sumOdd / (int(n) - countEven)

print("Sum of even numbers: ", sumEven)
print("Average of even numbers: ", averageEven)

print("Sum of even numbers: ", sumOdd)
print("Average of even numbers: ", averageOdd)