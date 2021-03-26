"""
solved but understand how mid-i+1 is the solution to find inversion.

Given an array of integers.
Find the Inversion Count in the array.

Inversion Count: For an array, inversion count
indicates how far (or close) the array is from being sorted.
 If array is already sorted then the inversion count is 0.
  If an array is sorted in the reverse order then the inversion
   count is the maximum.
Formally, two elements a[i] and a[j]
form an inversion if a[i] > a[j] and i < j.

Example 1:
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5
has three inversions (2, 1), (4, 1), (4, 3).

"""


def inversionCount(a, n):
    # O(n^2) expected is O(n * log n)
    count = 0
    for i in range(n):
        for j in range(n):
            if i < j and a[i] > a[j]:
                count += 1
    print(count)
    return count


def mSInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        a = arr[:len(arr) // 2]
        b = arr[len(arr) // 2:]
        a, ai = mSInversions(a)
        b, bi = mSInversions(b)
        c = []
        i = 0
        j = 0
        inversions = 0 + ai + bi
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            inversions += (len(a) - i)
    c += a[i:]
    c += b[j:]
    return c, inversions


def mergeSortInversion(a,n):
    if len(a) == 1:
        return 0

    #n = len(a)
    mid = n // 2

    l = a[:mid]
    r = a[mid:]

    li = mergeSortInversion(l,len(l))
    ri = mergeSortInversion(r,len(r))
    inv = 0 + li + ri

    i, j = 0, 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            i += 1
        else:
            j += 1
            inv += (len(l) - i)

    return inv


def mergeSort(arr, n):
    temp_arr = [0] * n
    return _mergeSort(arr, temp_arr, 0, n - 1)


def _mergeSort(arr, temp_arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += _mergeSort(arr, temp_arr,
                                left, mid)
        inv_count += _mergeSort(arr, temp_arr,
                                mid + 1, right)
        inv_count += merge(arr, temp_arr, left, mid, right)
    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]
    return inv_count


ans = mergeSort([2, 4, 1, 3, 5], 5)
print(ans)
