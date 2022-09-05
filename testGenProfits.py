from main import Employee, CompanyStats
import matplotlib.pyplot as plt
# def __init__(self, name, age, expertise, happiness, ethic, status):
# def __init__(self, funds=0, time = 0):

worst_employee=Employee('Worst Employee', 0, 0,  0,  0,  1, 0)
best_employee =Employee('Best Employee',  0, 10, 10, 10, 1, 0)
an_employee = Employee('Jane Doe', 0, 5, 5, 5, 1, 0)
high_skill_low_ethic = Employee('Sarah Stone', 0, 10, 5, 1, 1, 0)
low_skill_great_ethic = Employee('Roger Danger', 0, 1, 5, 10, 1, 0)
happy_but_low_skill = Employee('Leah Anthony', 0, 1, 10, 5, 1, 0)
unhappy_high_skill = Employee('Lucy Smith', 0, 5, 1, 5, 1, 0)

days = range(10)
scenario_1 = []
scenario_2 = []
scenario_3 = []
scenario_4 = []
scenario_5 = []
scenario_6 = []
scenario_7 = []

for day in days:
    scenario_1.append(worst_employee.gen_profits(day))
    scenario_2.append(best_employee.gen_profits(day))
    scenario_3.append(an_employee.gen_profits(day))
    scenario_4.append(high_skill_low_ethic.gen_profits(day))
    scenario_5.append((low_skill_great_ethic.gen_profits(day)))
    scenario_6.append(happy_but_low_skill.gen_profits(day))
    scenario_7.append(unhappy_high_skill.gen_profits(day))

fig = plt.figure()
plt.plot(days, scenario_1, marker= 'x', label = 'Worst Employee')
plt.plot(days, scenario_2, marker= 'o', label = 'Best Employee')
plt.plot(days, scenario_3, marker= 'X', label = 'An employee')
plt.plot(days, scenario_4, marker= 'X', label = 'HighSkill LowEthic')
plt.plot(days, scenario_5, marker= 'X', label = 'LowSkill GreatEthic')
plt.plot(days, scenario_6, marker= 'X', label = 'HappyBut LowSkill')
plt.plot(days, scenario_7, marker= 'X', label = 'UnhappyBut HighSkill')
plt.title('Comparison')
plt.grid(True)
plt.legend()
plt.show()