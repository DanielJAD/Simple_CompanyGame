import math

import numpy as np


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
        self.expected_wage = (1 + (self.tac / 100)) * ((self.expertise + 2) / 2) ** 2 * (((self.ethic + 2) / 2) * ((
                              self.happiness + 2) / 5) * (1 + (self.tac + 1) / (20 * 365)) *
                            (self.age / (20 * 365))) * 750
        self.training_days = 0

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

    def recalculate_expected_wage(self):
        self.expected_wage = max(self.expected_wage, (1 + (self.tac / 100)) * ((self.expertise + 2) / 2) ** 2 * (((
                       self.ethic + 2) / 2) * ((self.happiness + 2) / 5) * (1 + (self.tac + 1) / (20 * 365)) * (
                       self.age / (20 * 365))) * 750)

    def training_experise(self, inc):
        if self.expertise + inc > 10:
            self.expertise = 10
        else:
            self.expertise += inc


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

        weeks_adv = int(np.floor((self.time % 7 + days) / 7))
        days_adv = (days + (weeks_adv * 7)) % 7
        #  print('---- WEEKS ADVANCE - ' + str(weeks_adv))
        for i in range(1, weeks_adv + 1):
            print('\nA week was advanced... (week ' + str(i) + ')...')
            self.funds += self.gen_gross_company_profits(7)
            self.time += 7
            for person in self.employees:

                # Recalculate what the person thinks they should be paid.
                person.recalculate_expected_wage()

                # Happiness impacts ethic (Wage impacts happiness)
                if person.happiness > 5:
                    person.ethic = min(10.0, round(person.ethic + round(person.happiness / 50, 2), 2))
                else:
                    person.ethic = max(0.0, round(person.ethic - round(person.happiness / 50, 2), 2))

                #  Wage impacts happiness
                if person.expected_wage > person.wage:
                    person.happiness -= max(0.5, abs((person.expected_wage / person.wage) / 10 + person.happiness / 30))
                else:
                    person.happiness += min(happiness_inc_cap,
                                            abs((person.expected_wage / person.wage) / 10 - person.happiness / 30))
                person.happiness = min(10, round(person.happiness, 2))
                person.happiness = max(0, round(person.happiness, 2))
                person.tac += 7

                # If person is training, increase their expertise
                if person.training_days > 0:
                    person.expertise += min(7, person.training_days) * 0.03
                    person.training_days -= min(7, person.training_days)


        if days_adv > 0:
            print('\nAdvancing ' + str(days_adv) + ' days...')
            self.funds += self.gen_gross_company_profits(days_adv)
            self.time += days_adv
            for person in self.employees:
                person.tac += days_adv
                if person.training_days > 0:
                    person.expertise += 0.03
                    person.training_days -= 1

    def show_info(self):
        for person in self.employees:
            print(person.name + ' - Expected: £' + str(round(person.expected_wage)) + ' - Paid: £' + str(person.wage) +
                  ' - Happiness: ' + str(person.happiness) + ' - Ethic: ' + str(person.ethic))

    def show_info2(self):
        for person in self.employees:
            print(person.name + ' - TimeAtCompany: ' + str(person.tac) + ' - Expertise: ' + str(person.expertise))

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
                print(employee.name + ' is not available to work for ' + str(employee.dtw) + ' days.')
                total += employee.gen_gross_profits(min(time, employee.dtw), 0)
                if time > employee.dtw:
                    print(employee.name + ' has returned to work.')
            total += employee.gen_gross_profits(max(0, time - min(time, employee.dtw)))
            employee.dtw -= max(0, min(employee.dtw, time))

        total = round(total * 100) / 100
        print('Profit made: £' + str(total) + '.')
        return total

    def train_employee(self, employee, time):

        if employee.expertise < 1:

            # The training to 1 expertise might as well occur in one go - no need to set training days.
            employee.dtw += 21
            self.funds -= 300
            employee.training_experise(1 - employee.expertise)

        else:

            # Add the time to train as a variable that will decrement with the advance_time() command.
            # Take the funds immediately.
            employee.dtw += 7 * time
            employee.training_days += 7 * time
            self.funds -= get_training_cost(employee, time)


#  Constants
happiness_inc_cap = 0.3


#  Functions

def training_cost(expertise_in):
    return round(100 * math.exp((expertise_in - 1) * (math.log(50) / 8)))


def get_training_cost(person, weeks):
    cost = 0

    # The issue is that training will be based on their expertise, but if they're sent on 12 weeks, this is an
    # increase in expertise of 2.4, so this could potentially be too cheap.
    # So instead give no benefit to sending employees on many weeks at a time, rather than doing it separately.
    # Simulate the addition of expertise.

    for time in range(0, weeks):
        cost += training_cost(person.expertise + (0.2 * (weeks-1)))
        print(str(time+1) + ' weeks passed.... (test) - Cost here: ' + str(cost))
    return round(cost)


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
    elif input_command.lower() == 'train' or input_command.lower() == 't':
        print('Train Employee...')
        train_mechanism(this_company)
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
    elif input_command.lower() == 'hidden' or input_command.lower() == 'dd':
        this_company.show_info()
    elif input_command.lower() == 'hidden2' or input_command.lower() == 'dd2':
        this_company.show_info2()
    elif input_command.lower() == 'setup' or input_command.lower() == 'quick' and len(not_hired_list) == 5:
        print('Setting up...')
        this_company.hire(not_hired_list[0], not_hired_list)  # Hire David Miles
        this_company.hire(not_hired_list[3], not_hired_list)  # Hire Lucy Newton
        this_company.advance_time(100)  # Advance time 100 days.
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


def train_mechanism(company):
    if len(company.employees) == 0:
        # If there's no employees, selecting training does nothing - return.
        print('The company has no employees. No one can be trained.')
        return

    print('Who do you wish to train? :')
    enum = 1

    # Each person in the company is given the status of their training availability.
    for person in company.employees:
        if person.dtw > 0:
            print(str(enum) + ': ' + person.name + ' [Cannot be trained, they are currently not available to work].')
        elif person.expertise < 1:
            print(str(enum) + ': ' + person.name + ' - Expertise: ' + str(person.expertise) + ' - Fundamental Training'
                  + 'Package Cost: ' + str(100) + '.')
        elif person.expertise < 10:
            print(str(enum) + ': ' + person.name + ' - Expertise: ' + str(person.expertise) + ' - Cost Per Week:'
                  + str(training_cost(person.expertise)) + '.')
        else:
            print(str(enum) + ': ' + person.name + ' [Cannot be trained, they have nothing more to learn].')
        enum += 1
    choice = 'C'
    #  print(' ENUM VALUE IS  ' + str(enum))  - testing purposes
    while choice.lower() != 'q' and choice.lower() != 'quit':
        # Keep user within this loop until they intentionally quit.
        choice = input('Who do you wish to train? Send q to exit :')

        if not choice.isdigit():
            # An input that wasn't a number was entered, if it was quit, then process this, otherwise return invalid.
            if choice.lower() == 'q' or choice.lower() == 'quit':
                print('Quitting...')
            else:
                # The input was not an employee enum, and wasn't quit. So it's invalid. Return the loop.
                print('Invalid Input!')
            continue

        if 1 <= int(choice) <= (enum - 1):
            # Select a valid choice (each employee has an enum)
            chosen_employee = company.employees[int(choice) - 1]

            # If the employee doesn't benefit from training they cannot be trained.
            if not chosen_employee.expertise < 10 or chosen_employee.dtw > 0:
                print(chosen_employee.name + ' cannot be trained!')
                continue

            # Otherwise confirm training.
            confirm = input('Train  ' + chosen_employee.name + '? Y/N: ')

            if confirm.lower() == 'y' and not chosen_employee.expertise < 1:
                # The employee mas more than basic knowledge, so has the usual training process.

                choice_2 = 'C'
                while choice_2.lower() != 'R' and choice_2.lower() != 'quit':
                    # Keep user in this loop until they intentionally quit.

                    choice_2 = input('Train ' + chosen_employee.name + ' for how long? :')
                    if not choice_2.isdigit():
                        # The input choice for length of training was not a digit, so the loop resets.
                        print('Invalid Input!')
                    elif (not int(choice_2) > 0) or (not int(choice_2) < 13):
                        # The input was valid, but training can only be done for 1 to 12 weeks - the loop resets.
                        print('Number of weeks training must be between 1 and 12.')
                    else:
                        # The input was valid, so give them the price of the training and final confirmation.
                        choice_3 = input('This will cost £' + str(get_training_cost(chosen_employee, int(choice_2))) +
                                         '. '
                                         'Confirm? :')
                        if choice_3.lower() == 'y' or choice_3 == 'yes':
                            # Person confirmed, price is confirmed, so perform the training.
                            print('Training confirmed for ' + chosen_employee.name + '.')
                            # ______________ TRAINING ISSUED _______________
                            company.train_employee(chosen_employee, int(choice_2))
                            # Break the loop, a command was issued.
                            break
                        else:
                            print('Training not confirmed. Process exited')
                            # Break the loop, training for this person wasn't confirmed, so reset.
                            break

            elif confirm.lower() == 'y':
                # Training is confirmed, but the employee has below basic knowledge. So basic training is offered.

                input_2 = input('Send ' + chosen_employee.name + ' on basic training for 3 weeks? Y/N:')
                if input_2.lower != 'y' and input_2.lower != 'yes':
                    print('Training not confirmed. Process exited.')
                else:
                    # ______________ TRAINING ISSUED _______________
                    print(chosen_employee.name + 'sent on training course at the cost of £100.')
                    company.train_employee(chosen_employee, 0)
            else:
                # Employee training wasn't given a value, so exit the process.
                print('Training not confirmed. Process exited.')
                break
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
