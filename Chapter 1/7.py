def recursive(a, b):
    if a % b == 0 or b % a == 0:
        return b
    else:
        c = a % b
        return recursive(b, c)


print(recursive(2, 10))
