import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.tan(x)


def secante(xinf, xsup, cota, maxiteraciones):
    error = 1
    i = 1
    while error > cota:

        # NUEVA APROXIMACIÓN (RAÍZ)
        xr = xinf - ((f(xinf)*(xinf-xsup))/(f(xinf)-f(xsup)))
        # CALCULANDO EL ERROR
        error = np.abs((xr-xinf)/xr)
        print("Iteración:", i, " xsup:", xsup, "xinf:",
              xinf, " Raiz:", xr, " Error:", error)
        # REASIGNANDO VALORES
        xinf = xsup
        xsup = xr
        i += 1
        # IMPRIMIENDO EL RESULTADO DE LA RAÍZ Y EL ERROR
        if(error <= 0.001):
            print("La raíz es: ", xr, " f(raíz): ", f(xr))
            print("Con un error de: ", error)
            plt.plot(xinf, 0, 'o', color="g")
            plt.plot(xsup, f(xsup), 'o', color="y")


secante(4, 4.5, 0.001, 15)
# REALIZANDO LA GRÁFICA
x = np.linspace(0, 7, 20)
plt.plot(x, f(x))
plt.grid('on')
plt.show()
