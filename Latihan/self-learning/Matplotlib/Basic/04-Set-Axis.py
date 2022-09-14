import numpy as np
import matplotlib.pyplot as plt


def sinus_generator(amplitudo, frekuensi, t_akhir, theta):
    t = np.arange(0, t_akhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t, y


t, y = sinus_generator(1, 1, 4, 0)

plt.plot(t, y)

# !set AXIS
plt.axis([0, 4, -1, 1])  # ? plt.axis([xMin,xMax,yMin,yMax])

plt.show()
