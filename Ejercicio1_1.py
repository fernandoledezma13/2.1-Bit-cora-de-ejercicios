import numpy as np
from matplotlib import pyplot as plt


def funcion(e):
    i = e
    resul = ((8*np.exp(-0.5*i))*np.cos((3)*(i)))
    return resul

# Metodo de Newton


def derivada1(x):
    evaluacion = -4*np.exp(-0.5*x)*np.cos(3*x)-24*np.exp(-0.5*x)*np.sin(3*x)
    return evaluacion


def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("i | xi | fxi |fdxi | xr | error")
    while error > cota:
        xr = xi - (funcion(xi)/derivada1(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i += 1
        print("Raiz:", xr, " Error:", error)


newton(0.1, 10, 0.01)

vectorx = np.arange(0.01, 1, 0.01)

plt.plot(vectorx, funcion(vectorx))
plt.grid("x")
plt.grid("y")
plt.show()
