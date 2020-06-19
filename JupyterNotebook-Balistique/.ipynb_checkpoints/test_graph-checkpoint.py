import numpy as np
import matplotlib.pyplot as plt

def graph(formula, x_range):
    x = np.array(x_range)
    y = formula(x)  # <- note now we're calling the function 'formula' with x
    plt.plot(x, y)
    plt.show()

def fonction(x):
    return .3 * pow(x,2) - 7 

graph(fonction, range(-10, 11))
