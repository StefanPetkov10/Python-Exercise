input_str = input("Enter key-value pairs separated by commas (like key1:value1, key2:value2): ")

pairs = input_str.split(',')

my_dict = {}

for pair in pairs:
    key, value = pair.split(':')
    my_dict[key.strip()] = value.strip()

print("Resulting Dictionary:", my_dict)
for key, value in my_dict.items():
    print(key, value)

key = input('Enter a key: ')
value = input('Enter a value: ')
my_dict[key] = value
print(my_dict)

key = input('Enter a key to delete: ')
del my_dict[key]
print(my_dict)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key in sorted(my_dict.keys()):
    print(key, my_dict[key])