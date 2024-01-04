n = input("Enter count: ")

maxEven = -1
minOdd = 10000000000
countEven = 0
countOdd = 0

for i in range(0, int(n)):
    inputNum = input("Enter number: ")
    if int(inputNum) % 2 == 0:
        if int(inputNum) > maxEven:
            maxEven = int(inputNum)
        countEven += 1
    else:
        if int(inputNum) < minOdd:
            minOdd = int(inputNum)
        countOdd += 1

print("Max even number: ", maxEven)
print("Min odd number: ", minOdd)
print("Count of even numbers: ", countEven)
print("Count of odd numbers: ", countOdd)

