from MakeRecipe import make_salat

def check_if_we_have(recipe, availability, price):
    if "Salat" in recipe:
        make_salat(availability)
        sum = price["tomato"] + price["cucumber"] + price["cheese"]
        print(sum)


