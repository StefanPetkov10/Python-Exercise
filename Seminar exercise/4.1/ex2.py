numberToSplit = (input('Enter a number to split: ').split())
numberList = []

for i in numberToSplit:
    numberList.append(i)

maxLenght = ''

for i in numberList:
    if len(i) > len(maxLenght):
        maxLenght = i

print(maxLenght)


index = int(input('Enter a index: '))
numberList.pop(index)
print(numberList)

index = int(input('Enter a index: '))
number = input('Enter a string: ')
numberList.insert(index, number)
print(numberList)