count = int(input('Enter a count number: '))
numberListMultiply = []
for i in range(count):
    number = int(input("Enter a number: "))
    numberListMultiply.append(number * 3)

for i in numberListMultiply:
    print(i)

secialNumber = int(input('Enter a special number: '))
if secialNumber in numberListMultiply:
    print('Yes')

numberListMultiply.sort()

maxNumber = -1
for i in numberListMultiply:
    if i > maxNumber:
        maxNumber = i
print(maxNumber)


inputNumber = int(input('Enter a number for delete: '))
numberListMultiply.remove(inputNumber)
print(numberListMultiply)


index = int(input('Enter a index: '))
number = int(input('Enter a number to change: '))
numberListMultiply[index] = number
print(numberListMultiply)