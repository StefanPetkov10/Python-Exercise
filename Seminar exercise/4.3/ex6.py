n = int(input("Enter count: "))
sum = 0
multiply = 1

for i in range(0, n):
   inputNumber = int(input("Enter number: "))
   if inputNumber == -99:
       break

   if inputNumber > 0:
      sum += inputNumber
      multiply *= inputNumber



print("Sum of positive numbers: ", sum)
print("Multiply of positive numbers: ", multiply)