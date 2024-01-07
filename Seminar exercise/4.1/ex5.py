dictionary = {}
for i in range(7):
    key = int(input('Enter a key: '))
    value = input('Enter a value: ')
    dictionary[key] = value
print(dictionary)


maxKey = -1
for key in dictionary.keys():
    if key > maxKey:
        maxKey = key
print(maxKey)

#change value from key
key = int(input('Enter a key to change: '))
value = input('Enter a value: ')
dictionary[key] = value

#delete value from key and add new value

key = int(input('Enter a key to delete value: '))
del dictionary[key]
print(dictionary)
key = int(input('Enter a key: '))
value = input('Enter a value: ')
dictionary[key] = value
print(dictionary)