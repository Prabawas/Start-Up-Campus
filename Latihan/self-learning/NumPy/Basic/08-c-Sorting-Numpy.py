import numpy as np

data_type = [("nama", "S23"), ("tinggi", int)]
data = [
    ("Afdoni", 160),
    ("Zaid", 165),
    ("Yodha", 170)
]

a = np.array(data, dtype=data_type)

print(a)
print()

print(np.sort(a, order="tinggi"))
print(np.sort(a, order="nama"))
