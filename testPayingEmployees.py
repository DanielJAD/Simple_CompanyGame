from main import Employee  # as EmployeeEdit
from main import CompanyStats  # as CompanyStatsEdit
import matplotlib.pyplot as plt


# def __init__(self, name, age, expertise, happiness, ethic, status):
# def __init__(self, funds=0, time = 0):

class EmployeeEdit(Employee):
    def __init__(self, name, age, expertise, happiness, ethic, status, wage):
        super().__init__(name, age, expertise, happiness, ethic, status)
        self.wage = wage

    def gen_gross_profits(self, time):
        return self.gen_profits(time) - (time * self.wage)


worst_employee = EmployeeEdit('Worst Employee', 0, 0, 0, 0, 1, 50)
best_employee = EmployeeEdit('Best Employee', 0, 10, 10, 10, 1, 500)
an_employee = EmployeeEdit('Jane Doe', 0, 5, 5, 5, 1, 50)
high_skill_low_ethic = EmployeeEdit('Sarah Stone', 0, 10, 5, 1, 1, 200)
low_skill_great_ethic = EmployeeEdit('Roger Danger', 0, 1, 5, 10, 1, 25)
happy_but_low_skill = EmployeeEdit('Leah Anthony', 0, 1, 10, 5, 1, 60)
unhappy_high_skill = EmployeeEdit('Lucy Smith', 0, 5, 1, 5, 1, 150)

days = range(10)
scenario_1 = []
scenario_2 = []
scenario_3 = []
scenario_4 = []
scenario_5 = []
scenario_6 = []
scenario_7 = []

for day in days:
    scenario_1.append(worst_employee.gen_gross_profits(day))
    scenario_2.append(best_employee.gen_gross_profits(day))
    scenario_3.append(an_employee.gen_gross_profits(day))
    scenario_4.append(high_skill_low_ethic.gen_gross_profits(day))
    scenario_5.append((low_skill_great_ethic.gen_gross_profits(day)))
    scenario_6.append(happy_but_low_skill.gen_gross_profits(day))
    scenario_7.append(unhappy_high_skill.gen_gross_profits(day))

fig = plt.figure()
plt.plot(days, scenario_1, marker='x', label='Worst Employee')
#plt.plot(days, scenario_2, marker='o', label='Best Employee')
plt.plot(days, scenario_3, marker='X', label='An employee')
plt.plot(days, scenario_4, marker='X', label='HighSkill LowEthic')
plt.plot(days, scenario_5, marker='X', label='LowSkill GreatEthic')
plt.plot(days, scenario_6, marker='X', label='HappyBut LowSkill')
plt.plot(days, scenario_7, marker='X', label='UnhappyBut HighSkill')
plt.title('Comparison of Paying Wages')
plt.grid(True)
plt.legend()
plt.show()
