import numpy as np

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

def mse_(b0, b1, y = ks, x = zp, n = len(zp)):
    return np.sum((y - (b0 + b1 * x)) ** 2) / n

alpha = 0.000001
b0 = 0.1
b1 = 0.1
n = len(zp)

for i in range (5000):
    b0 -= alpha * (2 / n) * np.sum((b0 - ks) * zp)
    b1 -= alpha * (2 / n) * np.sum((b1 * zp - ks) * zp)
    if i % 500 == 0:
        print('Iteration = {i}, b0 = {b0}, b1 = {b1}, mse = {mse}'.format(i = i, b0 = b0, b1 = b1, mse = mse_(b0, b1)))

print(mse_(5.889820420132673))
