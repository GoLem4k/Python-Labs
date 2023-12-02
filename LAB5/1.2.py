import numpy as np


X = np.array([
    [1 for i in range(12)],
    np.random.randint(22,22+12,12),
    np.random.randint(60,82,12)
]).T

Y = np.array([np.round(np.random.rand() * 5.1 + 13.5, 1) for i in range(12)])

A = np.linalg.inv(X.T.dot(X)).dot(X.T.dot(Y))

print(f"Матрица A: {A}")

Y2=X.dot(A)
print("Y = ", Y)
print("Y2 = ", Y2)

if np.allclose(Y, Y2, 0.2):
    print("YES!")
else:
    print("NO!")