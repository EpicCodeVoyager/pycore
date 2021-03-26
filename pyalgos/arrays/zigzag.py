"""
Given an array Arr (distinct elements) of size N.
Rearrange the elements of array in zig-zag fashion.
The converted array should be in form a < b > c < d > e < f.

The relative order of elements is same in the output
i.e you have to iterate on the original array only.

Input:
N = 7
Arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: 3 7 4 8 2 6 1
Explanation: 3 < 7 > 4 < 8 > 2 < 6 > 1

"""


def zigZag(arr, n):
    flg = True

    for i in range(1, n):
        if flg:
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        else:
            if arr[i - 1] < arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        flg = not flg
    return arr

ans = zigZag([4, 3, 7, 8, 6, 2, 1], 7)
print(ans)
