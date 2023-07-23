import numpy as np
import matplotlib.pyplot as plt

zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

b = (np.sum(zp * ks)) / (np.sum(zp ** 2))
print(b)

y_pred = b * zp
r = np.corrcoef(zp, ks)[0, 1]
print(r)
plt.scatter(zp, ks)
plt.title('r = 0.8874900920739162')
plt.xlabel('zp')
plt.ylabel('ks')
plt.plot(zp, y_pred)
plt.show()

x = zp.reshape((len(zp), 1))
y = ks.reshape((len(ks), 1))
b = np.dot(np.linalg.inv(np.dot(x.T, x)), x.T @ y)
print(b)
