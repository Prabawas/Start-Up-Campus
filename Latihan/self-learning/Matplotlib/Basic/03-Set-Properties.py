from cmath import sin
import numpy as np
import matplotlib.pyplot as plt


def sinus_generator(amplitudo, frekuensi, t_akhir, theta):
    t = np.arange(0, t_akhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t, y


t1, y1 = sinus_generator(1, 1, 4, 0)
t2, y2 = sinus_generator(1, 1, 4, 90)
t3, y3 = sinus_generator(1, 1, 4, 180)

data_plot_1 = plt.plot(t1, y1)
data_plot_2 = plt.plot(t2, y2)
data_plot_3 = plt.plot(t3, y3)

# !Set Properties
plt.setp(data_plot_1, color='r', linewidth='0.5', linestyle='-.')
plt.setp(data_plot_2, color='g', linewidth='3', linestyle='-.')
plt.setp(data_plot_3, color='b', linewidth='1.29', linestyle='-.')

plt.show()
