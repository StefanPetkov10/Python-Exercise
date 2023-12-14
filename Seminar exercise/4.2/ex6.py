print("Въведете информация за избраните стоки: ")
print("Въведете код на стока 00 за краай на въвеждането: ")

def product_function():
    dictProduct = {}
    while True:
        try:
            user_input_code = input("Въведете код на стока: ")
            if user_input_code == '00':
                break

            number = int(user_input_code)

            if user_input_code not in dictProduct:
                dictProduct[user_input_code] = 0

            user_input_price = input("Въведете цена на стока: ")
            number_price = float(user_input_price)

            user_input_quantity = input("Въведете количество на стока: ")
            number_quantity = float(user_input_quantity)
            number_price *= number_quantity
            dictProduct[user_input_code] += number_price

        except ValueError:
            print("Invalid input. Please try again.")


    return dictProduct

result = product_function()
print("КАСОВА БЕЛЕЖКА")
print("========================================")
print(result)
print ("Общо: ", sum(result.values()))
pay = input("You have:")
pay = float(pay)
if pay > sum(result.values()):
    print("Сумата е по-голяма от необходимата сума!")
else:
    print("Сумата е по-малка от необходимата сума!")
    print("Необходимо е да платите още: ", sum(result.values()) - pay)
print("========================================")
#data now
import datetime
now = datetime.datetime.now()
print ("Дата: ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
