

if __name__ == '__main__':
    n = int (input())
    test_case = []
    for i in range(0, n):
        a = int (input())
        test_case.append(a)

    for i in test_case:
        if i % 2 == 0:
            print(-1)
        elif i == 1:
            print(1)
        else:
            j = 1
            print(j, end=' ')
            for j in range(2, i, 2):
                print(j+1, end=' ')
                print(j, end=' ')

            print()
