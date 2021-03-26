from itertools import permutations
import os
from pyDecorators.loggerDecorator import log_it

@log_it
def perms(a, start, end):
    if start == end:
        print(''.join(a))
        return ''.join(a)

    for i in range(start, end + 1):
        a[start], a[i] = a[i], a[start]
        perms(a, start + 1, end)
        a[start], a[i] = a[i], a[start]


s = list('abc')
r = perms(s, 0, len(s)-1)
print(r)
