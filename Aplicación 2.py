import numpy as np
from matplotlib import pyplot as plt


def fx(t):
    return (t+np.power(t, 0.5))*(20-t + np.power(20-t, 0.5))-155.55


def biseccion(a, b, cota):
    error = 1
    i = 0
    listar = [1, 10]
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


raices = biseccion(1, 10, 0.01)
y = 20-raices[-1]
print(raices)
print("x:", raices[-1], " y = ", y)

vect = np.arange(0, 10, 0.1)
plt.plot(vect, fx(vect))
plt.grid("x")
plt.grid("y")
plt.show()
