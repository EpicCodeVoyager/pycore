import numpy as np
import numpy.linalg as la

L = np.array([[0,   1/2, 1/3, 0, 0,   0],
              [1/3, 0,   0,   0, 1/2, 0],
              [1/3, 1/2, 0,   1, 0,   1/2],
              [1/3, 0,   1/3, 0, 1/2, 1/2],
              [0,   0,   0,   0, 0,   0],
              [0,   0,   1/3, 0, 0,   0]])

eVal, eVec = la.eig(L)

for eval in eVec:
    print(eval)

order = np.absolute(eVal).argsort()[::-1]

print("######")
#print(eVec)
M = np.array([[0,1,0,0],
              [1,0,0,0],
              [1,0,0,1],
              [0,0,1,0]])

# M = np.array([[3/2, -1],
#               [-1/2, 1/2]])
vals, vecs = np.linalg.eig(M)
deter = la.det(M)
print(deter)
print(vecs)
print(vals)