"""
Given a string S consisting only '0's and '1's,
find the last index of the '1' present in it.

Example 1:
Input:
S = 00001
Output:
4
Explanation:
Last index of  1 in given string is 4.
"""


def lastIndex(s):
    one_i = -1
    for i, char in enumerate(s):
        if char == "1":
            one_i = i
    return one_i


ans = lastIndex("0000100100")
print(ans)
