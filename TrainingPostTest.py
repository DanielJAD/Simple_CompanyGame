"""
Basic idea for costs vs expertise

lvl 1 : £100 a week
lvl 2 : £200 a week
lvl 3 : £250 a week
lvl 4 : £300 a week
lvl 5 : £500 a week
lvl 6 : £700 a week
lvl 7 : £1000 a week
lvl 8 : £2000 a week
lvl 9 : £5000 a week
"""
import math

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [100, 200, 250, 300, 500, 700, 1000, 2000, 5000]

import matplotlib.pyplot as plt

fig = plt.figure()
plt.plot(x, y, marker='x', label='Creative Test')

plt.title('Comparison')
plt.grid(True)
plt.legend()


# Looks like an exponential function.
# We want f(1) = 100,
# and f(9) = 5000
# --- So it'll be f(x) = 100*exp(x*A)
# Solve for A.........
# 100*exp(8*A) = 5000
# exp(8*A) = 50
# 8*A = ln(50)
# A = ln(50)/8

z = [0] * 9

for i in range(1, 9):
    z[i] = 100 * math.exp(x[i-1]*math.log(50)/8)

plt.plot(x, z)
plt.show()

# Success! This will be very suitable.