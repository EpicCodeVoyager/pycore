"""
Missing number in array
Given an array of size N-1 such that it can only contain
distinct integers in the range of 1 to N. Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4

"""


def findMissingNumber(arr,n):
    sum_ = (n * (n+1)) / 2
    sum_ = int(sum_)
    for ele in arr:
        sum_ -= ele
    return sum_

ans = findMissingNumber([1,2,3,5], 5)
print(ans)