"""
Input:
    N = 5
    arr[] = {1,2,3,-2,5}
Output:
    9
Explanation:
    Max subarray sum is 9
    of elements (1, 2, 3, -2, 5) which
    is a contiguous subarray.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)

"""


def maxSubArraySum(a, size):
    max_sum = float('-inf')
    for i in range(size):
        for j in range(size + 1):
            if i + j <= size:
                s = sum(a[i:i + j])
                if s > max_sum:
                    max_sum = s
    return max_sum


def maxSubArraySum2(a, size):
    max_ = float('-inf')
    current_max = 0
    start = 0
    end = 0
    s = 0

    for i in range(0, size):
        current_max += a[i]
        if current_max > max_:
            max_ = current_max
            end = i
            start = s

        if current_max < 0:
            current_max = 0
            s = i + 1


    print(f"start:{start}, end:{end}")
    return max_


ans = maxSubArraySum2([1, 2, 3, -2, 5], 5)
print(ans)
