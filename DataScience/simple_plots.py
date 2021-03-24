import matplotlib.pyplot as plt
import math
import numpy
from common import utilities 

x = numpy.linspace(0, 2*math.pi, 20)
y = [math.cos(value) for value in x]

where = [utilities.is_in_interval(value, 0, math.pi) for value in x]
print(where)

plt.plot(x,y)
plt.fill_between(x,y,where=where)

plt.xlabel("values in radians")
plt.ylabel("cos(x)")

plt.show()