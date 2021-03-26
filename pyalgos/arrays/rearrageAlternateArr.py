"""
Given a sorted array of positive integers.
 Your task is to rearrange  the array elements alternatively
  i.e first element should be max value, second should be min value,
   third should be second max, fourth should be second min and so on.

Example 1:

Input:
N = 6
arr[] = {1,2,3,4,5,6}
Output: 6 1 5 2 4 3
Explanation: Max element = 6, min = 1,
second max = 5, second min = 2, and
so on... Modified array is : 6 1 5 2 4 3.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= N <= 107
1 <= arr[i] <= 107
"""


def rearrange(arr, n):
    tarr = []
    for i in range(n//2):
        tarr.append(arr[n - i - 1])
        tarr.append(arr[i])
    l
    print(tarr)


rearrange([1, 2, 3, 4, 5], 5)
