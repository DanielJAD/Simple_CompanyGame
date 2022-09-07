'''
This file was created to test an algorithm for "what employees think they're worth" (wage-wise).

Employees will create this expectation, based on:
-   Their happiness [Low modifier] (if the job is not enjoyable and they're unhappy, they'll expect to be compensated).
-   Their expertise [High modifier] (if they're skilled, they'll expect more)
-   Their work ethic [Low modifier] (if they work hard, they'll expect to be paid a bit more)
-   Their time at the company [High modifier] (If they've been at the company a long time, this should be rewarded).
-   Their age [Medium Modifier] (An 18 year old vs. a 50 year old - they have different expenses)

The expected wage vs. their work wage will impact their happiness and ethic.

'''

import numpy as np
from matplotlib import pyplot as plt
from main import Employee


def f(EX, EC, HP, TAC, AGE):
    return ((EX+2)/2) ** 2 * (((EC +2)/2) * ((HP+2)/5) * (1 + (TAC+1)/(20*365)) * ((AGE)/(20*365))) * 750


emp1 = Employee('David Miles', 35, 9, 5, 8, 0, 1000)
emp2 = Employee('Jack White', 25, 7, 4, 2, 0, 500)
emp3 = Employee('Sarah Gold', 30, 6, 6, 4, 0, 400)
emp4 = Employee('Carl Smith', 53, 9, 5, 4, 0, 1200)
emp5 = Employee('Lucy Newton', 18, 3, 9, 7, 0, 100)

emp1.tac = 0
emp2.tac = 0
emp3.tac = 0
emp4.tac = 0
emp5.tac = 0 #  365*20

EMP_LIST = [emp1, emp2, emp3, emp4, emp5]

for employee in EMP_LIST:
    exp_wage = f(employee.expertise, employee.ethic, employee.happiness, employee.tac, employee.age)
    print(employee.name + ' expects £' + str(exp_wage) + ' and is paid £' + str(employee.wage) + '.' \
          + ' They generate £' + str(employee.gen_profits(1)) + ' per day.')

'''
Per week
- Happiness goes down (expected/given)/10 ; i.e if expected was 40,000 and given was 30,000, it goes down 0.13.
    However, if given is 40,000 and expected is 30,000, happiness will increase by 0.75 -> this will be capped at 0.3.
--- Noted an issue with the way happiness is added/reduced. If the wage and expectations do not change (relatively) the
    increase/decrease is uniform and will not stop over time - happiness may reach 10 or even 0 - which is not the 
    intention. It should decrease/increase to a steady state. 
    
    Decrease formula ---  (person.expected_wage/person.wage)/10
    
    Consider:
    
    H = H - (E/W)/10
    
    4 = 4 - (40/30)/10
    4 = 4 -(4/30)
    
    The data points...
    
    Expected = 100k, Wage = 30 k, happiness SS = 2
    Expected = 50, Wage = 40k, happiness SS = 4
    Expected = Wage, Happiness = 5
    Expected = 30k, Wage = 60k, happiness = 8.5
    Expected = 20k, Wage = 80k, Happiness = 9
    
    a : (E/W)/10 = 0.333..      ...... 0.23333
    b : (E/W)/10 = 0.125        ...... 0.075
    c : (E/W)/10 = 0.1          ...... 0
    d : (E/W)/10 = 0.05         ...... 0.05
    e : (E/W)/10 = 0.025        ...... 0.075
    
    Let's rethink this from the start.
    
    A percentage should be vital...
    30 Expected, 20 Given.. you're expecting 50% more ... ( G - E ) / G = -0.5
    20 Expected, 30 Given... you're given 50% more than you expected ... ( G - E ) / G => (30 - 20)/30 = 0.333
    
    3 = 3 - 0.5     + x * 3 
    8 = 8 + 0.333   + x * 8
'''

happiness_inc_cap = 0.3

def cap(inp, cap):
    if inp > cap:
        return cap
    else:
        return inp