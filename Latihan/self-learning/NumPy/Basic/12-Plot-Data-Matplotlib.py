import numpy as np
import matplotlib.pyplot as plt

# Membuat persamaan linier
# y = x**2 * (x2) + 2

x = np.arange(0, 11, 1)
y = ((x**2 * (x*2))+2)
print(x)
print(y)

plt.figure(1)
plt.plot(x, y)

# Membuat lingkaran
jari2 = 7

# TODO: Cara dengan arange
sudut_arange = np.arange(0, 2*np.pi, 0.001)
# TODO: Cara dengan linspace
sudut_linspace = np.linspace(0, 2*np.pi, 1000)
x1 = jari2*np.cos(sudut_arange)
y1 = jari2*np.sin(sudut_arange)

plt.figure(2)
plt.plot(x1, y1)
plt.show()
