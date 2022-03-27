import numpy as np
from matplotlib import pyplot as plt


def fx(t):

    return 10*(1-np.exp(-0.04*t))+4*np.exp(-0.04*t)-9.3


def biseccion(a, b, cota):
    error = 1
    i = 0
    listar = [1, 20]
    if fx(a)*fx(b) < 0:
        while error > cota:
            xr = (a+b)/2
            fxr = fx(xr)
            fxa = fx(a)
            if fxr * fxa < 0:
                b = xr
            elif fxr * fxa > 0:
                a = xr
            else:
                break
            listar.append(xr)
            xractual = xr
            if(len(listar) >= 2):
                xranterior = listar[-2]
                error = np.abs((xractual-xranterior)/xractual)
            else:
                error = 1
            i += 1
    else:
        print("NO EXISTE SOLUCION")
    return listar


raices = biseccion(50, 60, 0.001)
print(raices)
print("X:", raices[-1])

vect = np.arange(52, 56, 1)
plt.plot(vect, fx(vect))
plt.grid("X")
plt.grid("Y")
plt.show()
