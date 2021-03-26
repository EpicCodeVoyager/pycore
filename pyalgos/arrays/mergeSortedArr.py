""" NOT SOLVED, NEEDs REVISION.
Given two sorted arrays arr1[] and arr2[] of sizes n and m
in non-decreasing order. Merge them in sorted order without
using any extra space.

Modify arr1 so that it contains
the first N elements and modify
arr2 so that it contains the last
M elements.

Example 1:

Input:
    n = 4, arr1[] = [1 3 5 7]
    m = 5, arr2[] = [0 2 6 8 9]

Output:
    arr1[] = [0 1 2 3]
    arr2[] = [5 6 7 8 9]

Explanation:
    After merging the two
    non-decreasing arrays, we get,
    0 1 2 3 5 6 7 8 9.
"""


def merge(arr1, arr2, n, m):
    i = 0
    j = 0
    arr3 = []
    while i < n and j < m:
        if arr2[j] < arr1[i]:
            arr3.append(arr2[j])
            j += 1
        else:
            arr3.append(arr1[i])
            i += 1
    while i < n:
        arr3.append(arr1[i])
        i += 1
    while j < m:
        arr3.append(arr2[j])
        j += 1
    print(arr3)


def merge2(arr1, arr2, n, m):
    for i in range(n):
        if arr1[i] > arr2[0]:
            arr1[i], arr2[0] = arr2[0], arr1[i]
            j = 0
            while j + 1 < m and arr2[j] > arr2[j + 1]:
                arr2[j], arr2[j + 1] = arr2[j + 1], arr2[j]
                j = j + 1
            print(arr1)
            print(arr2)


merge2([1, 3, 5, 7], [0, 2, 6, 8, 9], 4, 5)
