number = int(input("Enter number 1 - 12: "))

def January():
    print("January")
def February():
    print("February")
def March():
    print("March")

def default_case():
    print("This is the default case")


# Switch-like dictionary
switch_dict = {
    '1': January,
    '2': February,
    '3': March
}
n = int(input("Enter number 1 - 12: "))

switch = {
    1: "January",
    2: "February",
    3: "March"
}

print(switch.get(n, " " + str(n)))
