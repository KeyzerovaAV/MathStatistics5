import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b1 = (np.mean(zp * ks) - np.mean(zp) * np.mean(ks)) / (np.mean(zp ** 2) - np.mean(zp) ** 2)
print(b1)
b0 = np.mean(ks) - b1 * np.mean(zp)
print(b0)
y_pred = b0 + b1 * zp
r = np.corrcoef(zp, ks)[0, 1]
print(r)
plt.scatter(zp, ks)
plt.title('r = 0.8874900920739162')
plt.xlabel('zp')
plt.ylabel('ks')
plt.plot(zp, y_pred)
plt.show()
