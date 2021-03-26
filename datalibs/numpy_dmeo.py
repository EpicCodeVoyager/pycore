import numpy as np
import numpy.linalg as la

A = [[1, 2, 3, 4],
     [5, 6, 1, 1],
     [1, 2, 3, 1],
     [3, 4, 1, 2]]

nA = np.array(A, dtype=np.float32)

print(nA[:, 0] / la.norm(nA[:, 0]))

nA[:, 1] = np.zeros_like(nA[:, 0])
print(nA[:, 1])
print(nA.shape)
