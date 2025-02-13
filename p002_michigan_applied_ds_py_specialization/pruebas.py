import numpy as np


np.random.rand(2, 2, 2, 2)

x = np.array([[1, 1, 1], [1, 1, 1]])
y = x
y[0, :2] = 0
x

x = [0, 1, 2, 3, 4, 5, 6]
x[2:3]

a1 = np.random.rand(4)
a2 = np.random.rand(4, 1)
a3 = np.array([[1, 2, 3, 4]])
a4 = np.arange(1, 4, 1)
a5 = np.linspace(1, 4, 4)

a4.ndim() == 1
a1.shape == a2.shape
a5.shape == a1.shape

np.arange(0, 36, 1).reshape(6, 6)[2:4, 2:4]
