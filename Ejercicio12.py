import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.tan(np.pi*x)-6
# MÉTODO DE LA SECANTE


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


# LLAMANDO AL MÉTODO DE LA SECANTE
secante(0, 0.44, 0.001, 10)

# REALIZANDO LA GRÁFICA
vectorx = np.arange(.2, .5, 0.001)
plt.plot(vectorx, f(vectorx))
plt.title("Ejercicio 12")
plt.grid("X")
plt.grid("Y")
plt.show()
