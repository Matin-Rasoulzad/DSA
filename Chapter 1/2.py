def recursive(array, n, i=0):
    if i==n:
        return 0
    else:
        return array[i]/n + recursive(array, n, i+1)

print(recursive([1,2],2,0))