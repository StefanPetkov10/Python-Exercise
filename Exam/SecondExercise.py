class Car:
    def __init__(self, car_brand, car_model, car_price, car_color, manifacture_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_price = car_price
        self.car_color = car_color
        self.manifacture_year = manifacture_year

self = Car('Audi', 'A4', 8000, 'black', 2007)
def display_info(self):
    print(f"{self.car_brand}, {self.car_model}, {self.car_price}, {self.car_color}, {self.manifacture_year}")

display_info(self)

cars = []

# for i in range(7):
#     car_brand = input('Enter car brand: ')
#     car_model = input('Enter car model: ')
#     car_price = input('Enter car price: ')
#     car_color = input('Enter car color: ')
#     manifacture_year = input('Enter manifacture year: ')
#     cars.append(Car(car_brand, car_model, car_price, car_color, manifacture_year,))

cars.append(Car('Audi', 'A4', 8000, 'black', 2007))
cars.append(Car('Audi', 'A5', 22000, 'white', 2012))
cars.append(Car('Audi', 'A6', 60000, 'gold', 2015))
cars.append(Car('Audi', 'A8', 80000, 'gold', 2023))
cars.append(Car('Mercedes', 'S class', 70000, 'metallic', 2016))

def sort_bt_price(cars):
    sorted_cars = sorted(cars, key=lambda car: car.car_price, reverse= True)
    return sorted_cars

sorted_cars = sort_bt_price(cars)
for car in sorted_cars:
    print(f"{car.car_brand}, {car.car_model}, {car.car_price} ...")


list_brand = []
def list_by_brand(car_brand_for_search):
    for car in cars:
        if car.car_brand == car_brand_for_search:
            list_brand.append(car)
    return  list_brand

audi_cars = list_by_brand('Audi')
for car in audi_cars:
    print(f"{car.car_brand}")

# def lisr_by_brand2(car_brand_for_search):
#     for i in range(len(cars)):
#         if cars[i].car_brand == car_brand_for_search:
#             list_brand.append(car)
#     return list_brand

def search_color(cars, car_color_for_search):
    highest_price = -1
    highest_price_car = None

    for car in cars:
        if car.car_color == car_color_for_search:
            if car.car_price > highest_price:
                highest_price = car.car_price
                highest_price_car = car
    return highest_price_car

color_to_search = 'gold'
result_car = search_color(cars, color_to_search)
print(f"The {color_to_search} car with the highest price is {result_car.car_brand} {result_car.car_model} "
      f"- Price: {result_car.car_price}")

def newest_car(cars):
    list_newes_car = []
    for car in cars:
        if car.manifacture_year > 2022:
            list_newes_car.append(car)
    return list_newes_car

result = newest_car(cars)
for car in result:
    print(f"{car.manifacture_year}")