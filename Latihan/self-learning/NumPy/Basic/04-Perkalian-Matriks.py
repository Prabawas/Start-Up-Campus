import numpy as np

# Membuat matriks
a = np.array(([1, 2, 5],
              [3, 6, 1],
              [10, 5, 3]))
b = np.identity(3)

# Perkalian matriks
c1 = np.dot(a, b)
c2 = a.dot(b)

# # # display
# print("matriks a :")
# print(a)
# print("matriks b :")
# print(b)
# print()

print(c2)
