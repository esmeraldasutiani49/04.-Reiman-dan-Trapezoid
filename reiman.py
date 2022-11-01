import numpy as p
import matplotlib.pyplot as plt
def func(x):
    return (x**2)*p.exp(-x)

a = 1.0
b = 10
n = 1000

#reiman
x = p.linspace(a,b,n)
dx = (x[-1]-x[0])/(n-1)

hasil = 0

for i in range(n-1):
    hasil += dx*func(x[i])

xp = p.linspace(a,b)
plt.plot(xp,func(xp))
for i in range(n-1):
    plt.bar(x[i], func(x[i]), align = 'edge', width = dx, color = 'red', edgecolor = 'black')
plt.show()
print(hasil)
