def recursive(a,b):
    if a < b:
        return 0
    else:
        return 1 + recursive(a - b, b)


print(recursive(12, 3))