"""
Largest Number formed from an Array:

Input:
N = 4
Arr[] = {54, 546, 548, 60}
Output: 6054854654
Explanation: Given numbers are {54, 546,
548, 60}, the arrangement 6054854654
gives the largest value.

Your Task:
You don't need to read input or print anything.
Your task is to complete the function printLargest()
which takes the array of strings arr[] as parameter and
 returns a string denoting the answer.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
0 ≤ Arr[i] ≤ 1018

"""


def cmp_pl(a, b):
    a = str(a)
    b = str(b)
    al = len(a)
    bl = len(b)

    i, j = 0, 0

    if a == b:
        return 0
    while i < al or j < bl:
        if a[i] > b[j]:
            return 1
        if i + 1 >= al:
            i = 0
        else:
            i += 1
        if j + 1 >= bl:
            j = 0
        else:
            j += 1
        if i ==0 and j ==0:
            break
    return -1


def cmp_pl2(a, b):
    a = str(a)
    b = str(b)
    ab = a + b
    ba = b + a
    if a == b:
        return 0
    if ab > ba:
        return 1
    return -1


def printLargest(arr):
    import functools
    arr.sort(key=functools.cmp_to_key(cmp_pl2), reverse=True)
    return "".join(list(map(str, arr)))


arr = [54, 541, 548, 60]
ans = printLargest(arr)
print(ans)
