def rec(s):
    s = s.replace(" ", "")
    s = s.replace(":", "")
    s = s.replace(",", "")
    s = s.upper()
    print(s)
    n = len(s)
    for i in range(n):
        if n - i > i:
            if s[i] == [n - i]:
                continue
            else:
                return False
        else:
            return True
rec("A man, a plan, a canal: Panama")
