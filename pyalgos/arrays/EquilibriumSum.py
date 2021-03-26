"""
Given an array A of n positive numbers.
The task is to find the first Equilibium Point in the array.
Equilibrium Point in an array is a position such that the sum
of elements before it is equal to the sum of elements after it.

Example 2:

Input:
n = 5
A[] = {1,3,5,2,2}
Output: 3
Explanation: For second test case
equilibrium point is at position 3
as elements before it (1+3) =
elements after it (2+2).

"""


def eqilibriumPoint(A, N):
    t_sum = sum(A)
    sum_ = A[0]
    if N == 1:
        return 1
    for i in range(1, N):
        if sum_ == t_sum - sum_ - A[i]:
            return i + 1
        sum_ += A[i]

    return -1


ans = eqilibriumPoint([1], 1)
print(ans)
