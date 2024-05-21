# Graph for x=sin(2t)

import numpy as np
import matplotlib.pyplot as plt

# t = 60 seconds
t = np.linspace(0, 60, 10000)   # Uncomment this line to see the graph for t = 60 seconds

# 1 sinusoidal cycle
# t = np.linspace(0, 1, 10000)   # Uncomment this line to see the graph for 1 sinusoidal cycle

# x is equals to sin of a function of t that has a peak and a valley of 120 in the interval [0, 60]
x = 0.03 * np.sin(2 * np.pi * t + 1/2*np.pi) + 0.03


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
plt.ylabel('y')
# plt.title('x=A*cos(2*pi*t)')
plt.title('y(t)=0.03sin(2.pi.t + 1/2.pi) + 0.03')
plt.grid()
plt.show()