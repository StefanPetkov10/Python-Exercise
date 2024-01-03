# kod na metod koito priema ime na textov fail prochita sudurjanieto
# i go vrushta kato string kakvo trqbva da napravi metoda pri exceptioni

# def read_file(file_name):
#     try:
#         file = open(file_name, 'r')
#         content = file.read()
#         file.close()
#         return content
#     except FileNotFoundError:
#         return 'File not found'
#     except:
#         return 'Error'
#
# file_name = 'text.txt'
# print(read_file(file_name))

#---------------------------------------------

#programa chete ot terminala cqlo chislo koren kvadraten ot chisloto - finally:
# good bye ako chisloto e otricatelno ili nevalidno da se izpishe nevalidno

# import math
#
# def square_root(number):
#     try:
#         result = math.sqrt(int(number))
#         return result
#     except ValueError:
#         return 'Invalid number'
#     finally:
#         print('Good bye')
#
# # Input from the user
# number_input = input('Enter a number: ')
#
# # Call the function with user input
# print(square_root(number_input))

#---------------------------------------------

#funkciq koqto priema vhod ot potrebite dve celi chisla i gi deli.
# ako delitelq e 0 da se izpishe greshka, ako ne e da se izpishe chastnoto

# def division(a, b):
#     try:
#         result = a / b
#         return result
#     except ZeroDivisionError:
#         return 'Error'

#---------------------------------------------

#Sazdaite class koito da se kazwa invalid input error. v nego da ima funkciq
#koqto priema potrebitelski vhod i pravim custom exeption ako vhoda ne e polojitelno cqlo chislo

class InvalidInputError(Exception):
    def __init__(self, input_value):
        self.input_value = input_value

    def process_input(input_value):
        try:
            if int(input_value) < 0:
                raise InvalidInputError(input_value)
                print(f"Processing input: {input_value}")

        except InvalidInputError as e:
            print(f"Invalid input value: {e}")
            print("Please try again")

inputValue = input("Enter a number: ")
print(InvalidInputError.process_input(inputValue))


#---------------------------------------------

#sredna stoinost na chislata koito sa predostaveni ot potrebitelq te sa v masiv s edin while cikul shte iskame da ima mnogokratno vuvejdane ot potrebitelq dokato ne budat vuvedeni validni chisla
# programata shte otrabotva izklucheniq kato nevaliden vhod i delenie na nula a finally da garantira che shte prikluchim programta po pravilen nachin

# def average(numbers):
#     return sum(numbers) / len(numbers)
#
# numbers = []
#
# while numbers != 'exit':
#     try:
#         number = int(input("Enter a number: "))
#         if number < 0:
#             raise Exception("Invalid number")
#         numbers.append(number)
#     except Exception as exception:
#         print(exception)
#         break
#
# print(average(numbers))














































