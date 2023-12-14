def f1(x):
    if x == 0:
        y = g2(x)
    else:
        y = 4 * x
    return y

def g2(x):
    z = float(input("Въведете число различно от нула: "))
    k = f1(z)
    return k

result_f1 = f1(input("Въведете число: "))
result_g2 = g2(2)
print(result_f1)
print(result_g2)
