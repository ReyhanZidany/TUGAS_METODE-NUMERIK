import numpy as np

def crout_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        U[j, j] = 1
        for i in range(j, n):
            sum_ = sum(L[i, k] * U[k, j] for k in range(i))
            L[i, j] = A[i, j] - sum_
        for i in range(j + 1, n):
            sum_ = sum(L[j, k] * U[k, i] for k in range(j))
            U[j, i] = (A[j, i] - sum_) / L[j, j]

    return L, U

def solve_using_crout(A, b):
    L, U = crout_decomposition(A)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x

# Testing Code
A = np.array([[2, 1], [5, 3]])
b = np.array([4, 10])
x = solve_using_crout(A, b)
print("Solusi menggunakan metode dekomposisi Crout:", x)
