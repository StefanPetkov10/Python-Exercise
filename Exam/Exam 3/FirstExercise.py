while True:
    try:
        n = int(input("n - "))
        k = int(input("k - "))
        if n < 1:
            raise ValueError("Invalid n")
        elif k < 1:
            raise ValueError("Invalid k")
        else:
            break
    except ValueError as e:
        print(e)


list = []
for _ in range(n):
    number = int(input("Enter number - "))
    list.append(number)

list1 = [x for x in list if x > k]
print(list1)

multiplication = 1
for i in range(len(list1)):
   if i % 2 != 0:
       multiplication *= list1[i]
print(multiplication)

min_number = min(list1)
index = list1.index(min_number)
print(index)

list2 = [x for x in list if x <= k and x > 0]

min_number2 = min(list2)
max_number2 = max(list2)

difference = max_number2 - min_number2


