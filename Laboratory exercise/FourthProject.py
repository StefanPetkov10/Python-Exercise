# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person1 = Person(name = "Stefan",age = 19)
# print(person1.name + " " + str(person1.age))

#---------------------------------------------

#definira class person s poleta - ime familiq wyzrast nacionalnost
#da se definira konstruktor, koito incializira  poletata na klasa
#da se syzdadat obekti na tozi klas i da se izwikwa method print

# class Person:
#     def __init__(self, name, secondName, age, nationality):
#         # Constructor - initializes the object's attributes
#         self.name = name
#         self.secondName = secondName
#         self.age = age
#         self.nationality = nationality
#
#     def printPerson(self):
#         # Property - provides a way to access the values of attributes
#         return f"Hello, my name is {self.name} {self.secondName} and I am {self.age} years old and i am {self.nationality}."
#
# person1 = Person(name= "Stefan", secondName= "Petkov", age=30, nationality= "Bulgarian")
#
# print(person1.printPerson())
# print("]#4")
# class Student(Person):
#     def __init__(self, name, secondName, age, nationality, university, year):
#         super().__init__(name, secondName, age, nationality)
#         self.university = university
#         self.year = year
#
#     def student_info(self):
#         return f"Student University: {self.university} and year: {self.year}"
#
# student1 = Student(name= "Stefan", secondName= "Petkov", age=30, nationality= "Bulgarian", university= "TU", year= 3)
#
# print(student1.printPerson())
# print(student1.student_info())


#class lecture, da ima universitet i gofini opit

# class Person:
#     def __init__(self, name, secondName, age, nationality):
#         # Constructor - initializes the object's attributes
#         self.name = name
#         self.secondName = secondName
#         self.age = age
#         self.nationality = nationality
#
#     def printPerson(self):
#         # Property - provides a way to access the values of attributes
#         return f"Hello, my name is {self.name} {self.secondName} and I am {self.age} years old and i am {self.nationality}."
#
# person1 = Person(name= "Stefan", secondName= "Petkov", age=40, nationality= "Bulgarian")
#
# print(person1.printPerson())
# print("------------------------")
# class Lecture(Person):
#     def __init__(self, name, secondName, age, nationality, university, year):
#         super().__init__(name, secondName, age, nationality)
#         self.university = university
#         self.year = year
#
#     def student_info(self):
#         return f"Student University: {self.university} and years of experience: {self.year}"
#
# lecture1 = Lecture(name= "Stefan", secondName= "Petkov", age=40, nationality= "Bulgarian", university= "TU", year= 20)
#
# print(lecture1.printPerson())
# print(lecture1.student_info())

#---------------------------------------------

#bank account system - 3 clasa - akaunt, saving akaunt, current akaunt
#akaunt - number, holdeerName, balance: deposit, withdraw, displayBalance

# class Account:
#     def __init__(self, number, holderName, balance):
#         self.number = number
#         self.holderName = holderName
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"New balance: {self.balance}")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Not enough money")
#         else:
#             self.balance -= amount
#             print(f"New balance: {self.balance}")
#
#     def displayBalance(self):
#         print(f"Balance: {self.balance}")
#
# account1 = Account(number = 1, holderName = "Stefan", balance = 1000)
# account1.deposit(100)
# account1.withdraw(200)
# account1.displayBalance()
#
# class SavingAccount(Account):
#     def __init__(self, number, holderName, balance, interestRate):
#         super().__init__(number, holderName, balance)
#         self.interestRate = interestRate
#
#     def addInterest(self):
#         self.balance += self.balance * self.interestRate
#         print(f"New balance: {self.balance}")
#
# savingAccount1 = SavingAccount(number = 1, holderName = "Stefan", balance = 900, interestRate = 0.1)
# print(savingAccount1.addInterest())
#
# class CurrentAccount(Account):
#     def __init__(self, number, holderName, balance, overdraftLimit):
#         super().__init__(number, holderName, balance)
#         self.overdraftLimit = overdraftLimit
#
#     def withdraw(self, amount):
#         if amount > self.balance + self.overdraftLimit:
#             print("Not enough money")
#         else:
#             self.balance -= amount
#             print(f"New balance: {self.balance}")
#
# currentAccount1 = CurrentAccount(number = 1, holderName = "Stefan", balance = 900, overdraftLimit = 100)
# currentAccount1.withdraw(1000)

#---------------------------------------------

#biblioteka - class book - avtor, janr, available kopiq i obshtiq broi kopiq, serien nomer(ID)
#checkOut - kolko sa ostanalite kopiq
#checkIn - uvelichavane na available kopiq

class Book:
    def __init__(self, author, genre, availableCopies, totalCopies, ID):
        self.author = author
        self.genre = genre
        self.availableCopies = availableCopies
        self.totalCopies = totalCopies
        self.ID = ID

    def checkOut(self):
        if (self.availableCopies > 0):
            self.availableCopies -= 1
        print(f"Available copies: {self.availableCopies}")

    def checkIn(self):
        if(self.availableCopies < self.totalCopies):
            self.availableCopies += 1
        print(f"Available copies: {self.availableCopies}")

book1 = Book(author = "Stefan", genre = "Fantasy", availableCopies = 10, totalCopies = 10, ID = 1)
book1.checkOut()
book1.checkIn()

#class person - ime gofini i adres
#method da printira informaciq za choveka

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def printPerson(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

person1 = Person(name = "Stefan", age = 21, address = "Sofia")
person1.printPerson()

#class lybrary - list ot registrirani potrebiteli  i list ot knigi
#method za addBook mahane, registrirame i displeivame knigi i potrebiteli

class Library:
    def __init__(self, users, books):
        self.users = list()
        self.books = list()

    def addBook(self, book):
        self.books.append(book)
        print(f"New book: {book}")

    def removeBook(self, book):
        self.books.remove(book)
        print(f"User removed: {book}")

    def registreition(self, name, age, address):
        self.users.append(Person(name, age, address))
        print(f"New user: {name}")

    def displayBooks(self):
        for book in self.books:
            print(book)

    def displayUsers(self):
        for user in self.users:
            print(user)

library1 = Library(users = [], books = [])
library1.addBook("book1")
library1.removeBook("book1")
library1.registreition("Stefan", 21, "Sofia")
library1.displayBooks()
library1.displayUsers()