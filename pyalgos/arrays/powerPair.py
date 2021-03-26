"""
Given two arrays X and Y of positive integers,
 find the number of pairs such that xy > yx (raised to power of)
  where x is an element from X and y is an element from Y.

  Expected Time Complexity: O((N + M)log(N)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ M, N ≤ 105
1 ≤ X[i], Y[i] ≤ 103
"""



def countPairs(a,b,M,N):
    cnt = 0
    for i in range(M):
        for j in range(N):
            if a[i] ** b[j] > b[j] ** a[i]:
                cnt += 1
    print(cnt)
    return cnt


countPairs([2,1,6],[1,5],3,2)
