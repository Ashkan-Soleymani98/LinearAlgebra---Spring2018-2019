# HW3 Question3

from math import hypot

import numpy as np


def rotate_calculator(a, b):
    r = hypot(a, b)
    c = a/r
    s = -b/r

    return (c, s)


def QR_decompose(A):
    R = np.copy(A)
    (num_rows, num_cols) = np.shape(A)
    (rows, cols) = np.tril_indices(num_rows, -1, num_cols)

    Q = np.identity(num_rows)
    for (row, col) in zip(rows, cols):

        if R[row, col] != 0:
            (c, s) = rotate_calculator(R[col, col], R[row, col])

            rotate = np.eye(num_rows)
            rotate[row, col] = s
            rotate[col, row] = -s
            rotate[[col, row], [col, row]] = c

            R = np.dot(rotate, R)
            Q = np.dot(Q, rotate.T)

    return (Q, R)


# when n > m
A = np.array([[1, 1, 9], [-1, 1, 2]])
b = np.array([2, 7])
(Q, R) = QR_decompose(A.T)
(m, n) = np.shape(A)
R_tilda = R[0:m, 0:m]
X = np.dot(Q[:, 0:m], np.linalg.inv(R_tilda.T))
X = np.dot(X, b)
print("X with minimum squire error is: ")
print(X)






