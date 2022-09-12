import numpy as np

# Membuat vector array
a = np.array([1, 2, 3, 4, 5, 6])
b = [1, 2, 3, 4, 5, 6, 7]

# Membuat range array
c = np.arange(1, 20, 3)  # (start, last, range)

# Membuat linier Space
d = np.linspace(1, 20, 30)  # (start, last, jumlah)

# Membuat matriks biasa
e = np.array(([1, 2, 3, 4, 5],
              [2, 3, 4, 5, 6]))

# Membuat matriks kosong
f = np.zeros((7, 5))

# Membuat matrik bernilai 1
g = np.ones((3, 2))

# Membuat matriks identity
h1 = np.identity(7)
h2 = np.eye(7)

# display
print(e)
