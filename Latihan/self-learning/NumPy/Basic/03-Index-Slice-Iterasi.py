import numpy as np

# membuat array
a = np.arange(20)**2

# indexing
print("Elemen ke 1 dari a = ", a[0])
print("Elemen ke 20(last) dari a = ", a[-1])

# Slicing
print("Elemen ke 1-5 dari a = ", a[0:5])
print("Elemen awal-akhir dengan range 2 dari a = ", a[0:-1:2])
print("Elemen awal-akhir dengan range 2 dari a = ", a[::3])

# Iterasi
for i in a:
    print("Value i = ", i)
