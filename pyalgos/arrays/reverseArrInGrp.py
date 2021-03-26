"""
Given an array arr[] of positive integers of size N.
 Reverse every sub-array group of size K.
Example 1:

Input:
N = 5, K = 3
arr[] = {1,2,3,4,5}
Output: 3 2 1 5 4
Explanation: First group consists of elements
1, 2, 3. Second group consists of 4,5.
"""


def reverseInGroups_first_attemp(arr, N, K):
    for i in range(0, N, K):
        mid = (i + K - 1) // 2
        for j in range(i, mid+1):
            if i + j < N and i + K < N:
                arr[j], arr[N -1 - j] = arr[N -1 - j], arr[j]

    print(arr)

def reverseInGroups(arr, N, K):
    i = 0
    while i < N:
        left = i
        right = min(i+K-1, N-1)
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        i += K
    print(arr)


reverseInGroups([1, 2, 3, 4, 5], 5, 3)
