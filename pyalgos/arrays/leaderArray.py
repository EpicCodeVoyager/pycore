"""

Example 1:

Input:
n = 6
A[] = {16,17,4,3,5,2}
Output: 17 5 2
Explanation: The first leader is 17
as it is greater than all the elements
to its right.  Similarly, the next
leader is 5. The right most element
is always a leader so it is also
included.

"""

from collections import deque

def leaders(A,N):
    leads = []
    max_ = A[N-1]
    leads.append(max_)

    leads = deque(leads)

    for i in range(N-2,-1,-1):
        if A[i] >= max_:
            leads.appendleft(A[i])
            max_ = A[i]

    print(list(leads))
    return list(leads)

leaders([16,17,4,3,5,2], 6)
