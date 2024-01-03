
def make_salat(availability):
    if availability["tomato"] >= 1 and availability["cocumber"] >= 1 and availability["cheese"] >= 1:
        print("Salat is ready")
        availability["tomato"] -= 1
        availability["cucumber"] -= 1
        availability["cheese"] -= 1
    else:
        print("We don't have enough products")
