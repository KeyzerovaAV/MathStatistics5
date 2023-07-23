import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(b, y = ks, x = zp, n = len(zp)):
    return np.sum((y - b * x) ** 2) / n

alpha = 0.000001
b = 0.1
n = len(zp)

for i in range (5000):
    b -= alpha * (2 / n) * np.sum((b * zp - ks) * zp)
    if i % 500 == 0:
        print('Iteration = {i}, b = {b}, mse = {mse}'.format(i = i, b = b, mse = mse_(b)))

print(mse_(5.889820420132673))
