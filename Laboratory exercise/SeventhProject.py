import random

minNumbers = 15
maxNumbers = 35

def checkCountNumber(minNumbers, maxNumbers):
    while True:
        countNumber = int(input('Enter count of numbers '))
        try:
            if countNumber < minNumbers or countNumber > maxNumbers:
                raise ValueError("Invalid number!")
            else:
                return countNumber
        except ValueError as e:
            print(e)


numbers = []
# for i in range(0, checkCountNumber(minNumbers, maxNumbers)):
#     currentNumber = int(input('Enter number from 30 to 300: '))
#     try:
#         if currentNumber < 30 or currentNumber > 300:
#             raise ValueError("Invalid number!")
#         else:
#             numbers.append(currentNumber)
#     except ValueError as e:
#         print(e)
#
countNumber = checkCountNumber(minNumbers, maxNumbers)
for i in range(countNumber):
    numbers.append(random.randint(30, 300))
print(numbers)

numbersDividerBy3 = []
for i in range(0, len(numbers)):
    if numbers[i] //10 % 10 % 3 == 0:
         numbersDividerBy3.append(numbers[i])

print(numbersDividerBy3)

minIndex = 0
for i in range(countNumber):
    if numbers[i] % 6 == 4 and numbers[i] < numbers[minIndex]:
        minIndex = i

print(minIndex)

numbersNew = []
for i in range(countNumber):
    if numbers[i] % 2 == 0 and numbers[i] % 3 == 0:
        numbersNew.append(numbers[i])


print(numbersNew)

avarage = 0.00
for i in range(countNumber):
    if numbers[i] % 2 != 0:
        avarage += numbers[i]
    avarage /= len(numbers)

print(avarage)


for i in range(countNumber):
    if numbers[i] % 2 == 0:
        numbers.remove(numbers[i])

print(numbers)

#-------------------------------------------------

# class Worker:
#
#     def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
#         self.worker_num = worker_num
#         self.fname = fname
#         self.lname = lname
#         self.work_experience_company = work_experience_company
#         self.salary = salary
#         self.age = age
#
# self = Worker(1, 'Ivan', 'Ivanov', 7, 1000, 25)
#
# def worker_information(self):
#     print(self.worker_num)
#     print(self.fname)
#     print(self.lname)
#     print(self.work_experience_company)
#     print(self.salary)
#     print(self.age)
#
# worker_information(self)
#
# def salary_bonus(self):
#     if self.work_experience_company > 5 and self.work_experience_company < 10:
#         self.salary += self.salary * 0.015
#         print(self.salary)
#     elif self.work_experience_company > 10:
#         self.salary += self.salary * 0.02
#         print(self.salary)
#     elif self.work_experience_company < 5:
#         self.salary += self.salary * 0.005
#         print(self.salary)
#
#
# list_of_workers = []
#
# # for i in range(0, 3):
# #     worker_num = input('Enter worker number: ')
# #     fname = input('Enter first name: ')
# #     lname = input('Enter last name: ')
# #     work_experience_company = input('Enter work experience in company: ')
# #     salary = input('Enter salary: ')
# #     age = input('Enter age: ')
# #     list_of_workers.append(Worker(worker_num, fname, lname, work_experience_company, salary, age))
#
# list_of_workers.append(Worker(1, 'Ivan', 'Ivanov', 5, 1000, 25))
# list_of_workers.append(Worker(2, 'Petar', 'Petrov', 10, 2000, 30))
# list_of_workers.append(Worker(3, 'Georgi', 'Georgiev', 3, 500, 20))
#
#
# def search_by_num(list_of_workers, worker_num):
#     for i in range(0, len(list_of_workers)):
#         if list_of_workers[i].worker_num == worker_num:
#             return True
#         else:
#             return False
#
#
# print(search_by_num(list_of_workers, 1))
#
# list_search_by_name_experience = []
# def search_by_name_experience(list_of_workers, fname, work_experience_company):
#     for i in range(0, len(list_of_workers)):
#         if list_of_workers[i].fname == fname and list_of_workers[i].work_experience_company == work_experience_company:
#             list_search_by_name_experience.append(list_of_workers[i])
#
# search_by_name_experience(list_of_workers, 'Ivan', 5)
# print(list_search_by_name_experience)
#
# def remove_worker(worker_num):
#     try:
#         for i in range(0, len(list_of_workers)):
#             if list_of_workers[i].worker_num == worker_num:
#                 list_of_workers.remove(list_of_workers[i])
#             else:
#                 raise ValueError("Wrong_num!")
#
#     except ValueError as e:
#         print(e)
#
# remove_worker(1)
# #todo __str__
#

#-------------------------------------------------

##dve celi polojitelni n i k, n e 10 vuvejdame 10 chisla
# suzdavame dva spisuka purviq da sa tezi po golemi ot k i da se namerqt indexite koito sa nechetni, i posle tezi s minimalna stoinost
# n po malki ili ravni na k da se nameri razlikata mejdu elementi s max i min


# numbers1 = []
# numbers2 = []
#
# for i in range(n):
#     currentNumber = int(input('Enter number: '))
#     try:
#         if currentNumber < 0:
#             raise ValueError("Invalid number!")
#         else:
#             numbers1.append(currentNumber)
#     except ValueError as e:
#         print(e)


