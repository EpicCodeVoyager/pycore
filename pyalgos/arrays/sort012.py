"""
Given an array of size N containing only 0s, 1s, and 2s;
 sort the array in ascending order.
Example 1:
Input:
N = 5
arr[]= {0 2 1 2 0}
Output:
0 0 1 2 2
Explanation:
0s 1s and 2s are segregated
into ascending order.
"""


def sort012(arr, n):
    c0 = 0
    c1 = 0
    c2 = 0
    for ele in arr:
        if ele == 0:
            c0 += 1
        elif ele == 1:
            c1 += 1
        else:
            c2 += 1
    i = 0
    while c0 != 0:
        arr[i] = 0
        i += 1
        c0 -= 1
    while c1 != 0:
        arr[i] = 1
        i += 1
        c1 -= 1
    while c2 != 0:
        arr[i] = 2
        i += 1
        c2 -= 1
    print(arr)


def sort012_opti(arr, n):
    start = 0
    mid = 0
    end = n - 1

    while mid <= end:
        if arr[mid] == 0:
            arr[start], arr[mid] = arr[mid], arr[start]
            start = start + 1
            mid = mid + 1
        elif arr[mid] == 1:
            mid = mid + 1
        else:
            arr[mid], arr[end] = arr[end], arr[mid]
            end = end - 1
    print(arr)


sort012_opti([0, 1, 1, 2, 0, 1, 1], 7)
