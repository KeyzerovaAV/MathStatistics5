import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])

x2 = np.array([10, 8, 9, 11, 14, 6, 4, 12, 7, 5])
y2 = np.array([7.46, 6.77, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])

x1 = x.reshape((len(x), 1))
y1 = y.reshape((len(y), 1))
X = np.hstack([np.ones((len(x), 1)), x1])
B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y1)
print(B)
y_pred = 3.00009091 + 0.50009091 * x
r = np.corrcoef(x, y)[0, 1]
print(r)
plt.scatter(x, y)
plt.title('r = 0.81642051634484')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(x, y_pred)
plt.show()
residue = y - y_pred
print(stats.shapiro(residue))

# x1 = x.reshape((len(x), 1))
# y1 = y3.reshape((len(y3), 1))
# X = np.hstack([np.ones((len(x), 1)), x1])
# B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y1)
# print(B)
# y_pred = B[0] + B[1] * x
# r = np.corrcoef(x, y3)[0, 1]
# print(r)
# plt.scatter(x, y3)
# plt.title('r = 0.8162867394895982')
# plt.xlabel('x')
# plt.ylabel('y3')
# plt.plot(x, y_pred)
# plt.show()
# residue = y3 - y_pred
# print(stats.shapiro(residue))

# x1 = x2.reshape((len(x2), 1))
# y1 = y2.reshape((len(y2), 1))
# X = np.hstack([np.ones((len(x2), 1)), x1])
# B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y1)
# print(B)
# y_pred = B[0] + B[1] * x2
# r = np.corrcoef(x2, y2)[0, 1]
# print(r)
# plt.scatter(x2, y2)
# plt.title('r = 0.9999965537848283')
# plt.xlabel('x2')
# plt.ylabel('y2')
# plt.plot(x2, y_pred)
# plt.show()
# residue = y2 - y_pred
# print(stats.shapiro(residue))
