# Graph for x=sin(2t)

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 10000)
# x is equals to sin of a function of t that has a peak and a valley of 120 in the interval [0, 60]
x = np.sin(2 * np.pi * t)
x = abs(x)

# Count the peaks
peaks = 0
for i in range(len(x)-1):
    if x[i] > x[i-1] and x[i] > x[i+1]:
        peaks += 1

print('Number of peaks:', peaks)

# Count the valleys
valleys = 0
for i in range(len(x)-1):
    if x[i] < x[i-1] and x[i] < x[i+1]:
        valleys += 1

print('Number of valleys:', valleys)

plt.plot(t, x)
plt.xlabel('t')
plt.ylabel('x')
plt.title('x=|A*sin(2*pi*t)|')
plt.grid()
plt.show()