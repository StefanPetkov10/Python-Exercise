listTown = []
townToSplit = (input('Enter a town to split: ').split(', '))
for i in townToSplit:
    listTown.append(i)

index = int(input('Enter a index: '))
listTown.pop(index)
print(listTown)

newTown = input('Enter a new town: ')
listTown.append(newTown)
print(listTown)

index = int(input('Enter a index: '))
newTown = input('Enter a new town: ')
listTown.insert(index, newTown)
print(listTown)

listTown.sort()
print(listTown)

town = input('Enter a town: ')
if town in listTown:
    print('Yes')

newListTown = []
newTownToSplit = (input('Enter a new town to split: ').split(', '))
for i in newTownToSplit:
    newListTown.append(i)

listTown.extend(newListTown)
print(listTown)