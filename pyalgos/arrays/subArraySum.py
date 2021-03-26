"""
Given an unsorted array A of size N that contains
only non-negative integers,
find a continuous sub-array
which adds to a given number S.

N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements
from 2nd position to 4th position
is 12.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

Constraints:
1 <= N <= 105
1 <= Ai <= 1010
"""


def subArraySum(arr, n, s):
    for i in range(n):
        j = 0
        while i + j <= n:
            if sum(arr[i:i+j]) == s:
                return [i+1, i+j]
            j += 1
    return -1


def subArraySum2(arr, n, s):
    curr_sum = arr[0]
    start = 0

    for i in range(1, n):
        while curr_sum > s and start < i-1:
            curr_sum = curr_sum - arr[start]
            start += 1

        if s == curr_sum:
            return [start, i]

        if curr_sum < s:
            curr_sum += arr[i]

    return -1





ans = subArraySum2([1, 2, 3, 7, 5], 5, 12)

print(ans)