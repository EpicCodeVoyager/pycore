"""
Given an unsorted array of size N.
Find the first element in array such that all
of its left elements are smaller and all right
elements to it are greater than it.

Note: Left and right side elements can be equal to
required element.

And extreme elements cannot be required element.
Example 1:

Input:
N = 4
A[] = {4, 2, 5, 7}
Output:
5
Explanation:
Elements on left of 5 are smaller than 5
and on right of it are greater than 5.
"""


def findElement(arr, n):
    max_ = float('-inf')
    max_break = -1
    max_curr_i = 0

    for i in range(n):
        if arr[i] >= max_:
            max_ = arr[i]
            max_curr_i = i
        else:
            max_break = i

    if max_break == -1 and max_curr_i == n-1:
        return arr[1]

    elif max_break + 1 in [0, n - 1]:
        return -1

    elif max_break < max_curr_i and max_curr_i == n - 1:
        return arr[max_break + 1]

    return -1


ans = findElement([2, 4, 6, 7, 8, 9], 6)
print(ans)
