import numpy as np

# Membuat array vector baris
a = np.array([(1, -1), (1, 1)])

print(a)

# Invers matrix
a_inv = np.linalg.inv(a)
print(a_inv)


# Determinan matrix
a_det = np.linalg.det(a)
a_det_inv = np.linalg.det(a_inv)

print(a_det)
print(a_det_inv)

#! Digunakan untuk menyelesaikan persamaan linier
