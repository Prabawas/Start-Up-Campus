import numpy as np

# Membuat vector baris
a1 = np.array([3, 2])
b1 = np.array([1, 3])

# Perkalian DOT
c1 = np.dot(a1, b1)

# Membuat vector baris ke-2
a2 = np.array([1, 3, 5])
b2 = np.array([2, 4, 1])

# Perkalian cross
c2a = np.cross(a2, b2)
c2b = np.cross(b2, a2)
# ! a di cross ke b .. maka arah akan ke bawah b
# ? b di cross ke a .. maka arah akan ke atas  a

# display
print(c1)
print(c2a)
print(c2b)
