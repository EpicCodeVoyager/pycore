"""
Given an array arr[] of N non-negative integers
representing the height of blocks. If width of each block is 1,
compute how much water can be trapped
between the blocks during the rainy season.

Example 1:

Input:
N = 6
arr[] = {3,0,0,2,0,4}
Output:
10

4,2,1,0,3
2+1+
"""


def trappingWater(arr, n):
    l_max = 0
    r_max = 0
    sum_ = 0
    i = 0
    j = n - 1
    while i <= j:
        if arr[i] < arr[j]:
            if arr[i] > l_max:
                l_max = arr[i]
            else:
                sum_ += l_max - arr[i]
            i += 1
        else:
            if arr[j] > r_max:
                r_max = arr[j]
            else:
                sum_ += r_max - arr[j]
            j -= 1
    return sum_


ans = trappingWater([3, 0, 0, 2, 0, 4], 6)
print(ans)