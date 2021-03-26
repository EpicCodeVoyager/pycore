"""
Given an array of distinct integers.
The task is to count all the triplets such that sum of two
elements equals the third element.
Example 1:

Input:
N = 4
arr[] = {1, 5, 3, 2}
Output: 2
Explanation: There are 2 triplets:
1 + 2 = 3 and 3 +2 = 5

Expected Time Complexity: O(N2)
Expected Auxiliary Space: O(1)
"""


def countTriplets(arr, n):
    count = 0
    sarr = set(arr)
    for i in range(0, n):
        for j in range(i+1, n):
            print(f"{i}-{j}")
            if (arr[i] + arr[j]) in sarr:
                count += 1
    return count


ans = countTriplets([1,5,3,2], 4)

print(ans)