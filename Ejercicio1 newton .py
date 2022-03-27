import numpy as np
from matplotlib import pyplot as plt


def funcion(x):
    return np.tan(x)-3.5


def funcion2(x):
    return np.power((1/np.cos(x)), 2)


def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("i | xi | fxi |fdxi | xr | error")
    while error > cota:
        xr = xi - (funcion(xi)/funcion2(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i += 1
        print("Raiz:", xr, " Error:", error)


newton(0, np.pi, 0.05)

vect = np.arange(0.5, 2, 0.1)

plt.plot(vect, funcion(vect))
plt.grid("x")
plt.grid("y")
plt.show()
