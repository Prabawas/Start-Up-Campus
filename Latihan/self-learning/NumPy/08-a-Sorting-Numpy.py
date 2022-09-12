import numpy as np

a = np.floor(np.random.randn(1, 10)*5)

print(a)
print("Nilai max dari a = ", a.max())
print("Posisi nilai max dari a = ", a.argmax())
print()
print("Nilai min dari a = ", a.min())
print("Posisi nilai min dari a = ", a.argmin())
print()

print("Mengurutkan nilai a: ")
print(np.sort(a))
print(np.argsort(a))
