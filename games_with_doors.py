

if __name__ == '__main__':
    t = int (input())
    alice = []
    bob = []
    for i in range(0, t):
       a = list(map(int, input().split()))
       b = list(map(int, input().split()))

       c = []
       d  = []
       for j in range(a[0], a[-1]+1):
           c.append(j)
       alice.append(c)
       for j in range(b[0], b[len(b)-1]+1):
           d.append(j)
       bob.append(d)


    for i in range(0, t):
        ans = 0
        l = len(list(set(alice[i]) & set(bob[i])))
        if l == 0:
            print(ans+1)
            continue
        else:
           ans = ans = ans + len(list(set(alice[i]) & set(bob[i]))) - 1

        if alice[i][0] != bob[i][0]:
            ans += 1
        if alice[i][-1] != bob[i][-1]:
            ans += 1
        print(ans)
