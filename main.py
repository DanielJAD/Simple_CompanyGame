class Employee:
    def __init__(self, name, age, expertise, happiness, ethic, status):
        self.name = name
        self.age = age
        self.expertise = expertise  # 0 - 10
        self.happiness = happiness  # 0 - 10
        self.ethic = ethic  # 0 - 10
        self.status = status  # Employed = 1, Not Employed = 0

    def hire(self):
        self.status = 1

    def fire(self):
        self.status = 0


class CompanyStats:
    def __init__(self, funds = 0):
        self.funds = 1000
        self.employees = []

    def hire(self, person, not_hired_list):
        if person not in self.employees and person in not_hired_list:
            self.employees.append(person)
            not_hired_list.remove(person)
            person.hire()

    def fire(self, person, ):
        if person not in not_hired_list and person in self.employees:
            self.employees.remove(person)
            not_hired_list.append((person))
            person.fire()



def readnames(list):
    if len(list) == 0:
        print(' NONE ')
    else:
        for person in list:
            print(' +  ' + person.name)


def employeeReport(company, not_hired_list):
    print(' ------- Employees -------- ')
    readnames(company.employees)
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

    not_hired_list = [employee1, employee2]
    this_company = CompanyStats()
    this_company.hire(employee1, not_hired_list)
    this_company.hire(employee2, not_hired_list)

    employeeReport(this_company, not_hired_list)

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startUp()
