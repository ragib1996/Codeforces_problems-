

if __name__ == '__main__':
    n, m, k = map(int, input().split())

    cells = n * m
    cell_per_tube = int(cells / k)
    extra_cel = cells % k
    tube_put = 0
    cell_completed = 0

    row = 1
    col = 1
    ans = []
    tube_record = []
    br  = True
    for i in range(1, n + 1):
        j = 1
        if i %2 == 1:
            br = True
            j = 1
        else:
            br = False
            j = m
        while(True):
            tube_record.append(i)
            tube_record.append(j)
            if len(tube_record) >= 2 * cell_per_tube and tube_put < k-1:
                tube_put += 1
                ans.append(tube_record)
                tube_record = []
            if br == True:
                j += 1
                if j == m+1:
                    br = False
                    j -= 1
                    break
            else:
                j -= 1
                if j == 0:
                    br = True
                    j += 1
                    break

    if len(tube_record) > 0:
        ans.append(tube_record)

    for i in ans:
        print( int (len(i)/2), end=' ')
        for j in i:
            print(j, end=' ')
        print()