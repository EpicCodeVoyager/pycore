"""
Given an array arr of N integers, write a function that
returns true if there is a triplet (a, b, c) that satisfies
a2 + b2 = c2, otherwise false.
Example 1:
Input:
N = 5
Arr[] = {3, 2, 4, 6, 5}
Output: Yes
Explanation: a=3, b=4, and c=5 forms a
pythagorean triplet.

"""


def checkTriplet(arr, n):
    c_2 = {ele**2 for ele in arr}

    for i in range(n-1):
        for j in range(i+1, n-1):
            a_2 = arr[i] ** 2
            b_2 = arr[j] ** 2
            c = a_2 + b_2
            if c in c_2:
                print(arr[i], arr[j])
                return "Yes"

    return "No"


ans = checkTriplet([4, 49, 1, 59, 19, 81, 97, 99, 82, 90, 99, 10, 58, 73, 23], 15)
print(ans)

