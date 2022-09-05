import numpy as np
from matplotlib import pyplot as plt


def f(EX, EC, HP):
    return (((EX+2) / 3) ** 3 * ((EC+2) / 3) ** 1.5 * ((HP+2) / 2) ** 1.25 ) * 1


expertise_range = np.linspace(5, 10, 15)
ethic_range = np.linspace(5, 10, 15)
happiness_range = 5

EX, EC = np.meshgrid(expertise_range, ethic_range)
OUT = f(EX, EC, happiness_range)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(EX, EC, OUT, rstride=1, cstride=1,
             cmap='viridis', edgecolor='none')
ax.set_xlabel('Expertise')
ax.set_ylabel('Ethic')
ax.set_zlabel('Profit')

plt.show()
