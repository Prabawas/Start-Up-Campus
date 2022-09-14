import numpy as np

# Membuat vektor baris
a = np.array(([1, 2, 3, 4, 5]), dtype=float)


# Membuat matrix dengan function


def kuadrat(baris, kolom):
    return (kolom**2)


def jumlah(baris, kolom):
    return (baris+kolom)


b = np.fromfunction(kuadrat, (2, 10), dtype=float)
c = np.fromfunction(jumlah, (4, 4), dtype=int)

# Membuat matrix dengan iterable
iterable = (x*2 for x in range(5))

d = np.fromiter(iterable, dtype=int)

# multiple array
data_type = [("Nama", "S255"), ("Tinggi", int)]
data = [
    ("Afdoni", 160),
    ("Zaid", 165),
    ("Yodha", 170)
]
e = np.array(data, dtype=data_type)

# display
print(e[2])
