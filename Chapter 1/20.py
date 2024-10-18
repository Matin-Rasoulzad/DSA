def recursive(m, n):
    if n<0 or m<0:
        return 0
    elif m==0:
        return n+1
    elif n==0:
        return recursive(m - 1, 1)
    else:
        return recursive(m - 1, recursive(m, n - 1))



print(recursive(3, 2))