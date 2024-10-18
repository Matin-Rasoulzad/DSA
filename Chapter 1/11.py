def recursive(n, Combination = [], coins = [2, 5, 10], start = 0):
    if n==0:
        print(Combination)
        return
    elif n<0:
        return
    else:
        for i in range(start,len(coins)):
            recursive(n - coins[i], Combination + [coins[i]], coins, i)


recursive(20)
