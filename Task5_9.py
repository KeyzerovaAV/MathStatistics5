import numpy as np
import scipy.stats as stats

X3 = np.array([30, 30, 40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84])

b1 = (np.mean(X3 * Y3) - np.mean(X3) * np.mean(Y3)) / (np.mean(X3 ** 2) - np.mean(X3) ** 2)
b0 = np.mean(Y3) - b1 * np.mean(X3)
y_pred = b0 + b1 * X3

df1 = 1
df2 = len(X3) - 2
SSf = np.sum((y_pred - np.mean(Y3)) ** 2)
SSo = np.sum((Y3 - y_pred) ** 2)
Msf = SSf / df1
Mso = SSo / df2
F = Msf / Mso
print(F)

print(stats.f.ppf(1 - 0.05, df1, df2))
