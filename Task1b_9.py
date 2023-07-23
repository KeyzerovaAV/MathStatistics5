import numpy as np
import matplotlib.pyplot as plt

X1 = np.array([30, 30, 40, 40])
Y1 = np.array([37, 47, 50, 60])

X2 = np.array([30, 30, 40, 40, 20, 20, 50, 50])
Y2 = np.array([37, 47, 50, 60, 25, 35, 62, 72])

X3 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

x = X1.reshape((len(X1), 1))
y = Y1.reshape((len(Y1), 1))
X = np.hstack([np.ones((len(X1), 1)), x])
B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)
print(B)

# x = X2.reshape((len(X2), 1))
# y = Y2.reshape((len(Y2), 1))
# X = np.hstack([np.ones((len(X2), 1)), x])
# B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)
# print(B)

# x = X3.reshape((len(X3), 1))
# y = Y3.reshape((len(Y3), 1))
# X = np.hstack([np.ones((len(X3), 1)), x])
# B = np.dot(np.linalg.inv(np.dot(X.T, X)), X.T @ y)
# print(B)
