import numpy as np

def solve_using_inverse_matrix(A, b):
    A_inv = np.linalg.inv(A) # Menghitung invers dari matriks A
    x = np.dot(A_inv, b) # Menggunakan invers untuk menghitung solusi
    return x

# Testing Code
A = np.array([[2, 1], [5, 3]])
b = np.array([4, 10])
x = solve_using_inverse_matrix(A, b)
print("Solusi menggunakan metode matriks balikan:", x)
