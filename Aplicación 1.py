import numpy as np
from matplotlib import pyplot as plt


def fx(t):
    return 300 + (((0.25*-32.27)/0.1)*t) - (np.power(0.25, 2)*-32.27) / \
        (np.power(0.1, 2))*(1-np.exp((-0.1*t)/0.25))-0.01


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


raices = biseccion(2, 10, 0.01)
print(raices)
print("X:", raices[-1])

vect = np.arange(1, 10, 0.01)
plt.plot(vect, fx(vect))
plt.grid("x")
plt.grid("y")
plt.show()
