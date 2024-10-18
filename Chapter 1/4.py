def recursive(n):
    if n==0 :
        return ""
    else:
        return recursive(n//2) + str(n%2)

print(recursive(100))