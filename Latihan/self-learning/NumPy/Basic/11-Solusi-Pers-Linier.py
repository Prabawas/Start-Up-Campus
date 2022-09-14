import numpy as np

A = np.array([(4, 3), (2, 5)])
Y = np.array([28, 19])

print(A)
print(Y)
print()

# Invers A
A_inv = np.linalg.inv(A)
print(A_inv)
print()

# Menyelesaikan persamaan linier / mencari Y
X1 = np.dot(A_inv, Y)
print(X1)
print()

Y1 = np.dot(A, X1)
print(Y1)
