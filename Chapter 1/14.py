def recursive(n, s, d, a):
    if n==1:
        print(s + '->' + a)
        print(a + '->' + d)

    else:
        recursive(n - 1, s, d, a)
        print(s + '->' + a)
        recursive(n - 1, d, s, a)
        print(a + '->' + d)
        recursive(n - 1, s, d, a)



recursive(2, 'S', 'D', 'A')
print('-------------------------------------------------')
recursive(1, 'S', 'D', 'A')