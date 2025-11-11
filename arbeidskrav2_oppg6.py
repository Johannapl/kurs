# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 20:13:13 2025

@author: Johanna

"""

import numpy as np
import matplotlib.pyplot as plt
# Genererer en array med 200 punkter jevnt fordlet på intervallet. #
x = np.linspace(-10, 10, 200)

# Funksjonen f(x) #
y = -x** 2 - 5
plt.plot(x,y)
