import numpy as np

# Membuat array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Membuat matrix
aMat = np.array(([2, 3, 4, 5],
                 [3, 4, 5, 6]))
bMat = np.ones((2, 4))

# Stacking Array , Menumpuk Array
c = np.hstack((a, b))
d = np.vstack((a, b))

# Stacking matrix , Menumpuk matrix
cMat = np.hstack((aMat, bMat))
dMat = np.vstack((aMat, bMat))

# Display
print(dMat)
