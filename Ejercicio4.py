import numpy as np
from matplotlib import pyplot as plt


def funcion(x):
    return np.tan(x)-0.1*x


def funcion2(x):
    return (np.power((1/np.cos(x)), 2)-0.1)


r = np.pi*1.5


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


newton(np.pi, r, 0.001)

vecto = np.arange(3.2, 3.8, 0.01)
plt.plot(vecto, funcion(vecto))
plt.grid("x")
plt.grid("y")
plt.show()
