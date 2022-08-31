from main import Employee, CompanyStats
import matplotlib.pyplot as plt
# def __init__(self, name, age, expertise, happiness, ethic, status):
# def __init__(self, funds=0, time = 0):

worst_employee=Employee('Worst Employee', 0, 0,  0,  0,  1)
best_employee =Employee('Best Employee',  0, 10, 10, 10, 1)

days = range(10)
scenario_1 = []
scenario_2 = []

for day in days:
    scenario_1.append(worst_employee.gen_profits(day))
    scenario_2.append(best_employee.gen_profits(day))

fig = plt.figure()
plt.plot(days, scenario_1, marker= 'x', label = 'Worst Employee')  #, label = 'Worst Employee'
plt.plot(days, scenario_2, marker= 'o', label = 'Best Employee')  #, label = 'Best Employee'
plt.title('Comparison')
plt.grid(True)
plt.legend()
plt.show()