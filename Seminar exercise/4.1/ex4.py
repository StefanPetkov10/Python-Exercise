n1 = int(input("Enter numbers of integers N1: "))
n2 = int(input("Enter numbers of integers N2: "))

set1 = set()
print("Enter elements for the first set: ")
for _ in range(n1):
    element = int(input())
    set1.add(element)

set2 = set()
print("Enter elements for the second set:")
for _ in range(n2):
    element = int(input())
    set2.add(element)

size_set1 = len(set1)
size_set2 = len(set2)

print(f"The size of first set is: {size_set1}")
print(f"The size of second set is: {size_set2}")

union_set = set1.union(set2)
# Алтернативно: union_set = set1 | set2

print("Union of the two sets", union_set)

intersection_set = set1.intersection(set2)
# Алтернативно: intersection_set = set1 & set2

print("Intersection of the two sets:", intersection_set)

inputNumber = int(input('Enter a number for delete: '))
set1.remove(inputNumber)
print(set1)

set1.clear()
set2.clear()
print(set1)