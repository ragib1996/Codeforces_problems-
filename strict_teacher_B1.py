

if __name__ == '__main__':
    t = int(input())
    testcase = []
    for i in range(0, t):
        n,m, q = map(int, input().split())
        b1, b2 = map(int, input().split())
        if b1 > b2:
            temp = b1
            b1 = b2
            b2 = temp
        c = int(input())
        testcase.append([n, b1, b2, c])

    for i in testcase:
        if i[3] < i[2] and i[3] > i[1]:
            d = i[2] - i[1]
            print(int (d/2))
        elif i[3] < i[1]:
            d = i[1] - 1
            print(d)
        else:
            d = i[0] - i[2]
            print(d)
