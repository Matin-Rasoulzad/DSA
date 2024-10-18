def recursive(str):
    n = len(str)
    if n == 0:
        return True
    elif n%2 == 1:
        return False
    elif str[0:n//2] != str[n//2:]:
        return False
    else:
        return recursive(str[1:n // 2])

print(recursive("ALLALL"))
print(recursive("ALILIALILI"))
