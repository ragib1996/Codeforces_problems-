

if __name__ == '__main__':
    t = int(input())
    test_case = []
    for i in range(0, t):
        n = int(input())
        a = []
        a  = list(map(int, input().split()))
        test_case.append(a)

    for i in test_case:
        b = [False] * (len(i) + 1 )

        for j in range(0, len(i)):
            if j == 0:
                b[i[j]] = True
            else:
                if i[j] == 1:
                    if b[2] == True:
                        b[1] = True
                    else:
                        print("NO")
                        break
                elif i[j] == len(i):
                    if b[i[j] - 1 ] == True:
                        b[i[j]] = True
                    else:
                        print("NO")
                        break

                else:
                    if b[i[j] + 1] == True or b[i[j] - 1 ] == True:
                        b[i[j]] = True
                    else:
                        print("NO")
                        break

        if j + 1 == len(i):
            print("YES")