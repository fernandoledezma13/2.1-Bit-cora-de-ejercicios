import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.power(x, 4)-3*np.power(x, 2)-3


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
        if(error <= 0.01):
            print("La raíz es: ", xr, " f(raíz): ", f(xr))
            print("Con un error de: ", error)
            plt.plot(xinf, 0, 'o', color="g")
            plt.plot(xsup, f(xsup), 'o', color="y")


secante(1, 2, 0.01, 10)
# REALIZANDO LA GRÁFICA
x = np.linspace(0, 3, 7)
plt.plot(x, f(x))
plt.grid('on')
plt.show()
