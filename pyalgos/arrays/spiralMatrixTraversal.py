"""
Given a matrix of size R*C. Traverse the matrix in spiral form.

Example 1:

Input:
R = 4, C = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""


def get_tra_arr(matrix, i, j, r, c, tra_arr):
    if i >= r or j >= c:
        return
    for p in range(i, c):
        tra_arr.append(matrix[i][p])

    for p in range(i + 1, r):
        tra_arr.append(matrix[p][c - 1])

    if i != r-1:
        for p in range(c - 2, j - 1, -1):
            tra_arr.append(matrix[r - 1][p])
    
    if j != c-1:
        for p in range(r - 2, i, -1):
            tra_arr.append(matrix[p][j])

    get_tra_arr(matrix, i + 1, j + 1, r - 1, c - 1, tra_arr)
    return tra_arr


def spirallyTraverse(matrix, r, c):
    tra_arr = []
    arr = get_tra_arr(matrix, 0, 0, r, c, tra_arr)
    return arr


mat = [[1, 2, 3, 4, 100],
       [5, 6, 7, 8, 101],
       [9, 10, 11, 12, 111]]

# mat = [[1,2,3,4,5,6],
#        [7,8,9,10,11,12],
#        [13,14,15,16,17,18],
#        [19,20,21,22,23,24],
#        [25,26,27,28,29,30],
#        [31,32,33,34,35,36]]

# mat = [[1,2,3,4],
#        [5,6,7,8],
#        [9,10,11,12],
#        [13,14,15,16]]
r = 3
c = 5
ans = spirallyTraverse(mat, r, c)
print(ans)
