number = int(input("Enter count: "))

rangeStart = 0
rangeEnd = 100

sum = 0

for i in range(0, int(number)):
    numberInput = int(input("Enter number: "))
    if numberInput >= rangeStart and numberInput <= rangeEnd:
        sum += numberInput
print("Sum of numbers in range: ", sum)

