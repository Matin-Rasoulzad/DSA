def recursive(array, n):

    if n == 1:
        return array[0]
    else:

        return max(array[n-1], recursive(array, n-1))

print(recursive([1, 2, 3], 3))
