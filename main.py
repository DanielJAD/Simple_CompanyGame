class Employee:
    def __init__(self, name, age, expertise, happiness, ethic, status, wage):
        self.name = name
        self.age = age
        self.expertise = expertise  # 0 - 10
        self.happiness = happiness  # 0 - 10
        self.ethic = ethic  # 0 - 10
        self.status = status  # Employed = 1, Not Employed = 0
        self.wage = wage
        self.tac = 0
        self.dtw = (self.wage / 50)  # Time for initial training etc.

    def hire(self):
        self.status = 1

    def fire(self):
        self.status = 0
        self.happiness = round(self.happiness / 2)  # Getting fired is not an enjoyable experience

    def gen_profits(self, time):
        return (((self.expertise + 2) / 3) ** 3 * ((self.ethic + 2) / 3) ** 1.5 * (
                (self.happiness + 2) / 2) ** 1.25) * time

    def gen_gross_profits(self, time, mod=1):
        return self.gen_profits(time) * mod - (time * self.wage)


class CompanyStats:
    def __init__(self, funds=0, time=0):
        self.funds = (1000 if funds == 0 else funds)
        self.employees = []
        self.time = time

    def hire(self, person, not_hired_list):
        if person not in self.employees and person in not_hired_list:
            self.employees.append(person)
            not_hired_list.remove(person)
            person.hire()

    def fire(self, person, not_hired_list):
        if person not in not_hired_list and person in self.employees:
            self.employees.remove(person)
            not_hired_list.append(person)
            person.fire()

    def advance_time(self, days):
        self.time += days
        self.funds += self.gen_gross_company_profits(days)
        for person in self.employees:
            person.tac += days

    def profit_report(self):
        for person in self.employees:
            print(person.name + ' generates ' + str(person.gen_profits(1)) + ' per day.')

    def employee_wages_tot(self):
        tot = 0
        if len(self.employees) == 0:
            return tot
        for person in self.employees:
            tot += person.wage
        return tot

    def gen_company_profits(self, time):
        total = 0
        for employee in self.employees:
            total += employee.gen_profits(time)
        total = round(total * 100) / 100
        return total

    def gen_gross_company_profits(self, time):
        total = 0
        for employee in self.employees:
            if employee.dtw > 0:
                print(employee.name + ' is not available to work for ' +str(employee.dtw) + ' days.')
                total += employee.gen_gross_profits(min(time, employee.dtw), 0)
                if time > employee.dtw:
                    print(employee.name + ' has returned to work.')
            total += employee.gen_gross_profits(max(0, time - min(time, employee.dtw)))
            employee.dtw -= max(0, min(employee.dtw, time))

        total = round(total * 100) / 100
        print('Profit made: £' + str(total) + '.')
        return total


def readnames(list_people):
    if len(list_people) == 0:
        print(' NONE ')
    else:
        for person in list_people:
            print(' +  ' + person.name)


def read_employee_names(list_employees):
    if len(list_employees) == 0:
        print(' NONE ')
    else:
        for person in list_employees:
            statement = ' +  ' + person.name + ' - Time at company - ' + str(person.tac) + ' days.'
            if person.dtw > 0:
                statement += ' Not available to work (for ' + str(person.dtw) + ' days).'
            print(statement)


def companyReport(company, not_hired_list):
    employeeReport(company, not_hired_list)
    print(' ------- Company Funds -------- ')
    print('Available : £' + str(round(company.funds * 100) / 100) + '.')
    print(' - Employee Wages - ')
    if len(company.employees) == 0:
        print('No employees. No wages to pay.')
    else:
        print('£' + str(company.employee_wages_tot()) + ' per day.')
    print('___________________________________')


def employeeReport(company, not_hired_list):
    print(' ------- Employees -------- ')
    read_employee_names(company.employees)
    print(' __________________________ ')
    print(' ')
    print(' ------- Available For Hire -------- ')
    readnames(not_hired_list)
    print(' ___________________________________ ')


def do_something(this_company, input_command, not_hired_list):
    if input_command.lower() == 'quit' or input_command.lower() == 'q':
        print('Exiting program...')
        quit()
    elif input_command.lower() == "hire" or input_command.lower() == 'h':
        print('Hire mechanism.')
        hire_mechanism(this_company, not_hired_list)
        # hire mechanism
    elif input_command.lower() == "fire" or input_command.lower() == 'f':
        print('Fire mechanism.')
        fire_mechanism(this_company, not_hired_list)
        # fire mechanism
    elif input_command.lower() == "ereport" or input_command.lower() == 'er':
        print('Employee Report...')
        employeeReport(this_company, not_hired_list)
    elif input_command.lower() == 'report' or input_command.lower() == 'r':
        print('Company Report...')
        companyReport(this_company, not_hired_list)
    elif input_command.lower() == 'advance' or input_command.lower() == 'a' or input_command.split(' ')[0].lower() \
            == 'advance' or input_command.split(' ')[0].lower() == 'a':
        if len(input_command.split(' ')) != 1 and input_command.split(' ')[1].isdigit():
            print('Advancing time by ' + str(input_command.split(' ')[1]) + ' days....')
            this_company.advance_time(int(input_command.split(' ')[1]))
        else:
            days = 'default'
            while days.lower() != 'q' and days.lower() != 'quit':
                days = input('Advance time by how many days?')
                if days.isdigit() and int(days) > 0:
                    this_company.advance_time(int(days))
                    return
                elif days.lower() != 'q' and days.lower() != 'quit':
                    print('Exiting...')
                    break
                else:
                    print('Input not recognised.')

        # advance mechanism
    else:
        # No other processes recognised
        print('Command not recognised.')


def hire_mechanism(company, not_hired_list):
    print('The following people are available for hire, and their info...')
    enum = 1
    for person in not_hired_list:
        print(str(enum) + ': ' + person.name + ' - Exp: ' + str(person.expertise) + ' - Wage requested : ' +
              str(person.wage) + '.')
        enum += 1
    choice = 'C'
    #  print(' ENUM VALUE IS  ' + str(enum))
    while choice.lower() != 'R' and choice.lower() != 'quit':
        choice = input('Who do you wish to hire? Send R to exit: ')
        if 1 <= int(choice) <= (enum - 1):
            print(not_hired_list[int(choice) - 1].name + ' hired.')
            company.hire(not_hired_list[int(choice) - 1], not_hired_list)
            break


def fire_mechanism(company, not_hired_list):
    if len(company.employees) == 0:
        print('The company has no employees. No one can be fired.')
        return
    print('Who do you wish to fire? :')
    enum = 1
    for person in company.employees:
        print(str(enum) + ': ' + person.name + ' - Wage: ' + str(person.wage) + ' - Redundancy cost : ' +
              str(person.wage * 5) + '.')
        enum += 1
    choice = 'C'
    #  print(' ENUM VALUE IS  ' + str(enum))  - testing purposes
    while choice.lower() != 'R' and choice.lower() != 'quit':
        choice = input('Who do you wish to fire? Send R to exit.')
        if 1 <= int(choice) <= (enum - 1):
            confirm = input('Confirm firing ' + company.employees[int(choice) - 1].name + '? Y/N: ')
            if confirm.lower() == 'y':
                print(company.employees[int(choice) - 1].name + ' fired.')
                company.funds -= company.employees[int(choice) - 1].wage * 5
                company.fire(company.employees[int(choice) - 1], not_hired_list)
            else:
                print('Firing not confirmed. Process exited.')
            break


# name, age, expertise, happiness, ethic, status, wage):

# Init stuff
emp1 = Employee('David Miles', 35, 9, 5, 8, 0, 1000)
emp2 = Employee('Jack White', 25, 7, 4, 2, 0, 500)
emp3 = Employee('Sarah Gold', 30, 6, 6, 4, 0, 400)
emp4 = Employee('Carl Smith', 53, 9, 5, 4, 0, 1200)
emp5 = Employee('Lucy Newton', 18, 3, 9, 7, 0, 100)

def startUp():
    # Initialise the people available for hire
    not_hired_list = [emp1, emp2, emp3, emp4, emp5]

    # Initialise the company
    this_company = CompanyStats()

    in_put = 'default'
    while in_put.lower() != 'quit' or in_put.lower != 'q':
        print('\nYou can choose: \'hire\', \'fire\', \'report\' or \'advance\'. \'quit\' will exit the program.')
        in_put = input('What do we do?: ')
        if in_put.lower() != 'quit' or in_put.lower != 'q':
            do_something(this_company, in_put, not_hired_list)
        else:
            break

    return 0


if __name__ == '__main__':
    startUp()
