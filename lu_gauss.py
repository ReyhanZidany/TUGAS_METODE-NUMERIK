import numpy as np

def lu_decomposition(A):
    n = len(A)
    L = np.eye(n) # Matriks identitas untuk matriks segitiga bawah
    U = A.astype(float) # Mengubah tipe data matriks A menjadi float

    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i] / U[i, i]
            L[j, i] = factor
            U[j] -= factor * U[i]

    return L, U

def solve_using_lu_gauss(A, b):
    L, U = lu_decomposition(A)
    y = np.linalg.solve(L, b) # Solusi Ly = b
    x = np.linalg.solve(U, y) # Solusi Ux = y
    return x

# Testing Code
A = np.array([[2, 1], [5, 3]], dtype=float)
b = np.array([4, 10], dtype=float)
x = solve_using_lu_gauss(A, b)
print("Solusi menggunakan metode dekomposisi LU Gauss:", x)
