import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([30, 30, 40, 40])
Y1 = np.array([37, 47, 50, 60])

X2 = np.array([30, 30, 40, 40, 20, 20, 50, 50])
Y2 = np.array([37, 47, 50, 60, 25, 35, 62, 72])

X3 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

n = len(X1)
b1 = (n * np.sum(X1 * Y1) - np.sum(X1) * np.sum(Y1)) / (n * np.sum(X1 ** 2) - np.sum(X1) ** 2)
print(b1)
b1 = (np.mean(X1 * Y1) - np.mean(X1) * np.mean(Y1)) / (np.mean(X1 ** 2) - np.mean(X1) ** 2)
print(b1)
b0 = np.mean(Y1) - b1 * np.mean(X1)
print(b0)
y_pred = b0 + b1 * X1
r = np.corrcoef(X1, Y1)[0, 1]
print(r)
determin_coef = r ** 2
print(determin_coef)
plt.scatter(X1, Y1)
plt.title('r = 0.7926239891046001')
plt.xlabel('X1')
plt.ylabel('Y1')
plt.plot(X1, y_pred)
plt.show()

# n = len(X2)
# b1 = (n * np.sum(X2 * Y2) - np.sum(X2) * np.sum(Y2)) / (n * np.sum(X2 ** 2) - np.sum(X2) ** 2)
# print(b1)
# b1 = (np.mean(X2 * Y2) - np.mean(X2) * np.mean(Y2)) / (np.mean(X2 ** 2) - np.mean(X2) ** 2)
# print(b1)
# b0 = np.mean(Y2) - b1 * np.mean(X2)
# print(b0)
# y_pred = b0 + b1 * X2
# r = np.corrcoef(X2, Y2)[0, 1]
# print(r)
# determin_coef = r ** 2
# print(determin_coef)
# plt.scatter(X2, Y2)
# plt.title('r = 0.940582293998595')
# plt.xlabel('X2')
# plt.ylabel('Y2')
# plt.plot(X2, y_pred)
# plt.show()

# n = len(X3)
# b1 = (n * np.sum(X3 * Y3) - np.sum(X3) * np.sum(Y3)) / (n * np.sum(X3 ** 2) - np.sum(X3) ** 2)
# print(b1)
# b1 = (np.mean(X3 * Y3) - np.mean(X3) * np.mean(Y3)) / (np.mean(X3 ** 2) - np.mean(X3) ** 2)
# print(b1)
# b0 = np.mean(Y3) - b1 * np.mean(X3)
# print(b0)
# y_pred = b0 + b1 * X3
# r = np.corrcoef(X3, Y3)[0, 1]
# print(r)
# determin_coef = r ** 2
# print(determin_coef)
# plt.scatter(X3, Y3)
# plt.title('r = 0.9725791007224713')
# plt.xlabel('X3')
# plt.ylabel('Y3')
# plt.plot(X3, y_pred)
# plt.show()
