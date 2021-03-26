"""
The cost of stock on each day is given in an array A[] of size N.
Find all the days on which you buy and sell the stock so that
in between those days your profit is maximum.

Note: There may be multiple possible solutions.
Print any one of them.
"""


def stockBuySell(A, n):
    bs_pairs = []
    start = 0
    end = 0
    for i in range(1, n):
        if A[i - 1] <= A[i]:
            end = i
        else:
            if start != end:
                bs_pairs.append((start, end))
            start = i
            end = i

    if start != end:
        bs_pairs.append((start, end))

    return bs_pairs


ans = stockBuySell([4,2,2,2,4], 5)
print(ans)
