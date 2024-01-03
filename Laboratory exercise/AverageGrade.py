
def average_grade(gradesList):
    sum = 0
    for grade in gradesList:
        sum += grade
    return sum / len(gradesList)

def finalResult(sum: int):
    if sum >= 90:
        return "A"
    elif sum >= 80:
        return "B"
    elif sum >= 70:
        return "C"
    elif sum >= 60:
        return "D"




