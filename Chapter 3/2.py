def combination(n, r):
    """
    This function is o(n) while recursive format of this is o(2^n). We could
    also use memorized functions to reduce complexity of recursive.
    """
    if r > n or r < 0:
        return 0
    if r == 0 or r == n:
        return 1
    numerator = [n - i for i in range(r)]
    denominator = [i + 1 for i in range(r)]
    result = 1
    for i in range(r):
        result *= numerator[i]
        result //= denominator[i]
    return result

print(combination(10, 3))
