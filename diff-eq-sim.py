# Python for modelling the modelling of the project system using differential equations

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Equation: dy/dt = -0.1 * y

# Define the differential equation
def model(y, t):
    dydt = -0.1 * y
    return dydt

# Initial condition
