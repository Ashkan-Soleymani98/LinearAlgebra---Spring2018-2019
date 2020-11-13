import numpy as np

print("This program calculates best approximation of a matrix given rank and its singular value decomposition.\n")
print("Please enter matrix dimension.")

m, n = map(int, input().split())

print("Please enter matrix U")
U = [list() for j in range(m)]
for i in range(m):
    U[i] = list(map(int, input().split()))

print("Please enter matrix S")
S = [list() for j in range(m)]
for i in range(m):
    S[i] = list(map(int, input().split()))

print("Please enter matrix V_transposed")
V_transposed = [list() for j in range(n)]
for i in range(n):
    V_transposed[i] = list(map(int, input().split()))

print("Please enter approximation rank")
k = int(input())
for i in range(min(m, n) - 1, k - 1, -1):
    S[i][i] = 0


U = np.asmatrix(U)
S = np.asmatrix(S)
V_transposed = np.asmatrix(V_transposed)

A = np.matmul(U, S)
A = np.matmul(A, V_transposed)

print(*A)




