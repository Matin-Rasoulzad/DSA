def recursive(n, s, d, a):
    if n==1:
        print(s + ' -> ' + d)
    else:
        recursive(n - 1, s, a, d)
        print(s + ' -> ' + d)
        recursive(n - 1, a, d, s)


recursive(3, 'S', 'D', 'A')