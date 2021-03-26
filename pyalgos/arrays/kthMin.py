"""
Given an array arr[] and a number K where K
is smaller than size of array, the task is to
find the Kth smallest element in the given array.
It is given that all array elements are distinct.

Example 1:
Input:
N = 6
arr[] = 7 10 4 3 20 15
K = 3
Output : 7
Explanation :
3rd smallest element in the given
array is 7.
"""
import heapq

def kthSmallest(arr, l, r, k):
    import bisect
    # ([7, 10, 4, 3, 20, 15], 0, 5, 3)
    # Fails for the given output.
    k_mins = []
    min_ = float('inf')
    for i in range(l, r + 1):
        min_ = arr[i]
        if len(k_mins) < k:
            bisect.insort(k_mins, min_)
        else:
            for j in range(k-1, -1, -1):
                if min_ < k_mins[j]:
                    k_mins[j] = min_
                    break
    print(k_mins)
    return max(k_mins)

def kthSmallest2(arr, l, r, k):
    import heapq
    nsml = heapq.nsmallest(k, arr)
    print(nsml)
    return nsml[-1]
ans = kthSmallest2([7, 10, 4, 3, 20, 15], 0, 5, 3)
print(ans)