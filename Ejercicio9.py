import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.power(x, 2)-6


def secante(xinf, xsup, cota, maxiteraciones):
    error = 1
    i = 1
    while error > cota:

        xr = xinf - ((f(xinf)*(xinf-xsup))/(f(xinf)-f(xsup)))
        error = np.abs((xr-xinf)/xr)
        print("Iteración:", i, " xsup:", xsup, "xinf:",
              xinf, " Raiz:", xr, " Error:", error)
        xinf = xsup
        xsup = xr
        i += 1
        if(error <= 0.001):
            print("La raíz es: ", xr, " f(raíz): ", f(xr))
            print("Con un error de: ", error)
            plt.plot(xinf, 0, 'o', color="g")
            plt.plot(xsup, f(xsup), 'o', color="y")


secante(1, 5, 0.001, 10)
x = np.linspace(1, 10, 7)
plt.plot(x, f(x))
plt.title("Ejercicio 9")
plt.grid('on')
plt.show()
