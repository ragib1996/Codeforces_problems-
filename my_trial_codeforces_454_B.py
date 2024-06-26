from collections import deque


if __name__ == '__main__':
    n = int(input())

    # nums = list(map(int, input("Please enter multiple integers separated by spaces: ").split()))
    a = deque(map (int,  (input().split())))

    #print(a)
    l = len(a)
    flag = True
    count = 0
    while ( a[l-1] <= a[0]  and count < n ):
        x = a.pop()
        a.appendleft(x)
        count = count + 1

    for i in range(1, l):
        if a[i-1]  > a[i]:
            print(-1)
            flag = False
            break

    if flag:
        if count == n:
            count = 0
        print(count)





