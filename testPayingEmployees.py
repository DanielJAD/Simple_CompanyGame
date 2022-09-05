from main import Employee
from main import CompanyStats
import matplotlib.pyplot as plt

# def __init__(self, name, age, expertise, happiness, ethic, status):
# def __init__(self, funds=0, time = 0):


worst_employee = Employee('Worst Employee', 0, 0, 0, 0, 1, 50)
best_employee = Employee('Best Employee', 0, 10, 10, 10, 1, 500)
an_employee = Employee('Jane Doe', 0, 5, 5, 5, 1, 50)
high_skill_low_ethic = Employee('Sarah Stone', 0, 10, 5, 1, 1, 200)
low_skill_great_ethic = Employee('Roger Danger', 0, 1, 5, 10, 1, 25)
happy_but_low_skill = Employee('Leah Anthony', 0, 1, 10, 5, 1, 60)
unhappy_high_skill = Employee('Lucy Smith', 0, 5, 1, 5, 1, 150)
a = Employee('Bad Employ', 0, 4, 4, 3, 1, 70)
b = Employee('Another Bad', 0, 6, 3, 3, 1, 85)

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
'''
fig = plt.figure(0)
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
# plt.show()
'''
available_for_hire = [worst_employee, best_employee, an_employee, high_skill_low_ethic, low_skill_great_ethic,
                      happy_but_low_skill, unhappy_high_skill, a, b]

a_company = CompanyStats()
# a_company.hire(worst_employee, available_for_hire)
# a_company.hire(best_employee, available_for_hire)
a_company.hire(a, available_for_hire)
a_company.hire(b, available_for_hire)

company_scenario = []

long_days = range(20)

for day in long_days:
    company_scenario.append(a_company.gen_gross_company_profits(day))

fig2 = plt.figure(1)
plt.plot(long_days, company_scenario, marker='x')
plt.title('Company Funds Growth')
plt.grid(True)
plt.show()
