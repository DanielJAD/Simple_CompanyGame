class Employee:
    def __init__(self, name, age, expertise, happiness, ethic, status):
        self.name = name
        self.age = age
        self.expertise = expertise  # 0 - 10
        self.happiness = happiness  # 0 - 10
        self.ethic = ethic  # 0 - 10
        self.status = status  # Employed = 1, Not Employed = 0

    def hire(self, hired_list, not_hired_list):
        self.status = 1
        not_hired_list.remove(self)
        hired_list.append(self)

    def fire(self, hired_list, not_hired_list):
        self.status = 0
        hired_list.append(self)
        not_hired_list.remove(self)


class CompanyStats:
    def __init__(self, funds, employees):
        self.funds = 1000
        self.employees = []

    def hire(self, person, hired_list, not_hired_list):
        if person not in hired_list and person in not_hired_list:
            self.hire(person)
            person.hire(hired_list, not_hired_list)


def readnames(list):
    for person in list:
        print(person.name)


def employeeReport(hired_list, not_hired_list):
    print(' ------- Employees -------- ')
    readnames(hired_list)
    print(' __________________________ ')
    print(' ')
    print(' ------- Available For Hire -------- ')
    readnames(not_hired_list)
    print(' ___________________________________ ')


employee1 = Employee('David Miles', 35, 9, 5, 8, 0)
employee2 = Employee('Jack White', 25, 7, 4, 2, 0)

not_hired_list = [employee1, employee2]


# def hire_employee(person):


def startUp():
    employees = []

    employee1.hire(employees, not_hired_list)

    employeeReport(employees, not_hired_list)

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startUp()
