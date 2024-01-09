class Worker:
    def __init__(self, worker_num, fname, lname, work_experience_company, salary, age):
        self.worker_num = worker_num
        self.fname = fname
        self.lname = lname
        self.work_experience_company = work_experience_company
        self.salary = salary
        self.age = age

    def worker_information(self):
        return f"({self.worker_num},{self.fname},{self.lname},{self.work_experience_company},{self.salary},{self.age})"

    def salary_bonus(self):
        if self.work_experience_company > 5 and self.work_experience_company < 10:
            self.salary += self.salary * 0.015
            print(self.salary)
        elif self.work_experience_company > 10:
            self.salary += self.salary * 0.02
            print(self.salary)
        elif self.work_experience_company < 5:
            self.salary += self.salary * 0.005
            print(self.salary)

worker1 = Worker(1, 'Stefan', 'Petkov', 6, 1500, 20)
print(worker1.worker_information())
worker1.salary_bonus()

workers_list = []
count = int(input("Enter a count"))
for _ in range(count):
    worker_num = int(input("worker_num"))
    fname = input('fname')
    lname = input('lname')
    work_experience_company = int(input("work_experience_company"))
    salary = int(input("salary"))
    age = int(input("age"))
    workers_list.append(Worker(worker_num, fname, lname, work_experience_company, salary, age))

def search_by_num(worker_num, workers_list):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            return True
        return False
    # mylist = [worker for worker in workers_list
    #           if worker.worker_num == worker_num]
    # print(mylist)
    # return len(mylist) > 0

print(search_by_num(1, workers_list))

def search_by_name_experience(workers_list, fname, work_experience_company):
    return [worker for worker in workers_list
            if worker.fname == fname and
            worker.work_experience_company == work_experience_company]

def add_worker(workers_list, worker):
    workers_list.append(worker)

def remove_worker(worker_num):
    for worker in workers_list:
        if worker.worker_num == worker_num:
            workers_list.remove(worker)
            return print("Information deleted")
        return print("Wrong worker_num")

remove_worker(1)

workers_list.append(Worker(1, 'Ivan', 'Ivanov', 5, 1000, 25))
workers_list.append(Worker(2, 'Petar', 'Petrov', 10, 2000, 30))
workers_list.append(Worker(3, 'Georgi', 'Georgiev', 3, 500, 20))

def sorted_by_num():
    new_list = sorted(workers_list, key=lambda worker: worker.worker_num, reverse=True)
    for worker in new_list:
        print(worker.worker_num)

sorted_by_num()
