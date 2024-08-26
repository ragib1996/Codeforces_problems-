

if __name__ == '__main__':
    t = int (input())
    test_cases = []

    for i in range(0,t):
        n =  int (input())
        a = list(map(int, input().split()))
        test_cases.append(a)

    for i in test_cases:
        flag  = True
        i.sort()
        l = len(i)
        if l % 2 == 1:
            flag = False
        l = int (l/2)
        ans = i[l]
        print(ans)