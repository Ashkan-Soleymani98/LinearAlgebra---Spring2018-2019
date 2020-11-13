import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

print("This program calculates best approximation of an image given approximation rank.(Image Compression)\n")

path = "input_image_1.jpg"
try:
    img = Image.open(path)
except IOError:
    pass

data = np.asarray(img)
r = [[pixel[0] for pixel in row] for row in data]
g = [[pixel[1] for pixel in row] for row in data]
b = [[pixel[2] for pixel in row] for row in data]

print("Please enter approximation rank!")
k = int(input())

if k <= min(np.asarray(r).shape):
    U_r, S_r, V_transposed_r = np.linalg.svd(r, full_matrices=True)
    Smat_r = np.zeros(np.asarray(r).shape)
    Smat_r[:k, :k] = np.diag(S_r[:k])
    r = np.matmul(U_r, np.matmul(Smat_r, V_transposed_r))

    U_g, S_g, V_transposed_g = np.linalg.svd(g, full_matrices=True)
    Smat_g = np.zeros(np.asarray(g).shape)
    Smat_g[:k, :k] = np.diag(S_g[:k])
    g = np.matmul(U_g, np.matmul(Smat_g, V_transposed_g))

    U_b, S_b, V_transposed_b = np.linalg.svd(b, full_matrices=True)
    Smat_b = np.zeros(np.asarray(b).shape)
    Smat_b[:k, :k] = np.diag(S_b[:k])
    b = np.matmul(U_b, np.matmul(Smat_b, V_transposed_b))
    data = np.zeros(data.shape)
    data[..., 0] = r
    data[..., 1] = g
    data[..., 2] = b
    data = np.rint(data)
    data = data.astype(int)
    data = np.clip(data, 0, 255)
    plt.imshow(data)
    plt.show()
else:
    print("Sorry! Approximation rank is too high for this image, try later!")
