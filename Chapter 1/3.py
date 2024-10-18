def recursive(array,n,i=0):
    if n-i <= i:
        return array
    else:
        array[i] , array[n-i-1] = array[n-i-1] , array[i]
        return recursive(array,n,i+1)

bcv
print(recursive([1,2,3,4],4,0))
print(recursive([1,2,3],3,0))
