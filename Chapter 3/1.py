def fibonacci(n):
    """
    This function is o(n) while recursive format of this is o(2^n)
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]

    array = [1, 1]
    for i in range(2, n):
        array.append(array[i - 1] + array[i - 2])

    print(array)


fibonacci(10)
