import numpy as np
import matplotlib.pyplot as plt

# membuat data sinus_generator
#        ! (sin(2wf * theta))


def sinus_generator(amplitudo, frekuensi, t_akhir, theta):
    t = np.arange(0, t_akhir, 0.1)
    y = amplitudo * np.sin(2*frekuensi*t + np.deg2rad(theta))
    return t, y


# Membuat plot
t1, y1 = sinus_generator(1, 1, 4, 0)
plt.plot(t1, y1, "r")

t2, y2 = sinus_generator(1, 1, 4, 30)
plt.plot(t2, y2, "g-.")

t3, y3 = sinus_generator(1, 1, 4, 60)
plt.plot(t3, y3, "b-,")

t4, y4 = sinus_generator(1, 1, 4, 90)
plt.plot(t4, y4, "c-v")

# Menampilkan
plt.show()

# "."	point
# ","	pixel
# "o"	circle
# "v"	triangle_down
# "^"	triangle_up
# "<"	triangle_left
# ">"	triangle_right
# "1"	tri_down
# "2"	tri_up
# "3"	tri_left
# "4"	tri_right
# "8"	octagon
# "s"	square
# "p"	pentagon
# "P"	plus (filled)
# "*"	star
# "h"	hexagon1
# "H"	hexagon2
# "+"	plus
# "x"	x
# "X"	x (filled)
# "D"	diamond
# "d"	thin_diamond
# "|"	vline
# "_"	hline
