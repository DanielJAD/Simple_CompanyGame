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

    def gen_profits(self, time):
        return ((self.expertise/4)**3  * (self.ethic/2)**2 * self.happiness )*time*(0.5)


class CompanyStats:
    def __init__(self, funds=0, time = 0):
        self.funds = (1000 if funds == 0 else funds)
        self.employees = []
        self.time = time

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

    def advance_time(self, days):
        self.time += days

    def profit_report(self):
        for person in self.employees:
            print(person.name + ' generates ' + str(person.gen_profits(1)) + ' per day.')

    def gen_company_profits(self, time):
        print('\nGenerating profits for ' + str(time) + ' days...\n')
        total = 0
        for employee in self.employees:
            total += employee.gen_profits(time)
        total = round(total*100) / 100
        print('Profit made: £' + str(total) + '.')
        self.funds += total
        print('New company funds: £' + str(self.funds) + '!')

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


# Init stuff
employee1 = Employee('David Miles', 35, 9, 5, 8, 0)
employee2 = Employee('Jack White', 25, 7, 4, 2, 0)
not_hired_list = [employee1, employee2]


def startUp():
    not_hired_list = [employee1, employee2]
    this_company = CompanyStats()
    this_company.hire(employee1, not_hired_list)
    this_company.hire(employee2, not_hired_list)

    employeeReport(this_company, not_hired_list)

    this_company.gen_company_profits(10)
    this_company.profit_report()

    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    startUp()
