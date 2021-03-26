from sys import maxsize


def maxSubArray(a):
    max_sum = -maxsize - 1
    current_max = 0

    for element in a:
        current_max = current_max + element
        if max_sum < current_max:
            max_sum = current_max

        if current_max < 0:
            current_max = 0
    return max_sum


# Driver function to check the above function
a = [-1, -2, -3, -4, -5, -10]
print("Maximum contiguous sum is", maxSubArray(a))
