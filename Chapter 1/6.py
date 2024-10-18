def recursive(a, b):
    if b<0 and a<0:
        return recursive(abs(a),abs(b))
    elif b<0 or a<0:
        return (-1)*recursive(abs(a),abs(b))
    if b==0:
        return 0
    return a + recursive(a, b - 1)



print(recursive(3, 5))


"""
def recursive(a, b):
    if b < 0:
        return -recursive(a, -b)
    if b == 0:
        return 0
    return a + recursive(a, b - 1)

print(recursive(3, 5))
"""
