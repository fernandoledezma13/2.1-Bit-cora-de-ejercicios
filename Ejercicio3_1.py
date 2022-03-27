import numpy as np
from matplotlib import pyplot as plt


def funcion(x):
    return 10-20*(np.exp(-0.2*x)-np.exp(-0.75*x))-5


def derivada(x):
    return (4*np.exp((3/4)*x)-15*np.exp((1/5)*x))/np.exp((19/20)*x)


def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("i | xi | fxi |fdxi | xr | error")
    while error > cota:
        xr = xi - (funcion(xi)/derivada(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i += 1
        print("Raiz:", xr, " Error:", error)


newton(0.1, 20, 0.1)

vect = np.arange(0, 2, 0.01)

plt.plot(vect, funcion(vect))
plt.grid("x")
plt.grid("y")
plt.show()
