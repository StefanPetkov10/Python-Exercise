n = int(input("Enter count: "))

for i in range(0, n):
    numberOnDegree = 1
    number = int(input("Enter number: "))
    degree = int(input("Enter degree: "))
    while(degree > 0):
        numberOnDegree *= number
        degree -= 1
    print("Result: ", numberOnDegree)
