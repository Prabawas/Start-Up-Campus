import numpy as np

# membuat array
a = np.array(([2, 3, 6],
              [4, 7, 9]))

print("Matrix a : ")
print(a)
print("Ukuran matrix a => ", a.shape)
print()

# ? transpose
print("Transpose matrix a ; ")
print(a.transpose())
# print(np.transpose(a))
# print(a.T)
print()

# ? Flatten array, vector baris
print("Flatten matrix a : ")
# print(a.ravel())
print(np.ravel(a))
print()

# reshape matrix
print("ReShape matrix a : ")
print(a.reshape(3, 2))
print()

# resize matrix
a.resize(3, 2)
print("Resize matrix a : ")
print(a)
print("ukuran matrix a : ", a.shape)
