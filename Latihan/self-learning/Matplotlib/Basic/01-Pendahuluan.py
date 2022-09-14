import numpy as np
import matplotlib.pyplot as plt

# membuat data
x = np.array([2, 4, 6, 8, 10, 12, 14, 16])
y = np.linspace(0, 43, 8)
z = np.array([2, 4, 6, 12, 56, 23, 9, 10])

# Membuat plot
plt.plot(x, y)
plt.plot(x, z)

# Menampilakn plot
plt.show()
