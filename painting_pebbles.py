# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import copy

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    d = {}
    n, k = input().split()
    n = int(n)
    k = int (k)
    a = list(map(int, input().split()))
    """
    for i in range(0, n):
        if a[i] not in d:
            d[a[i]] = []
        d[a[i]].append(i)
    """
    b = copy.deepcopy(a)
    b.sort()
    flag =  False
    ans = []
    c = 0
    x= 0
    for i in range(0, n):
        if c > k:
            break
        if i == 0:
            for j in range(0, b[i]):
                ans.append(1)
            d[b[i]] = ans
            c = 1
            x = b[i]
        else:
            if b[i] == b[i-1]:
                continue
            else:
                d[b[i]] = copy.deepcopy(d[x])
                if c == 1:
                    d[b[i]].append(c)
                    c += 1
                    if c > k :
                        break
                for j in range ( len(d[b[i]]), b[i] ):
                    d[b[i]].append(c)
                    c += 1
                    if c > k:
                        break
                x = b[i]




    if b[-1] in d and len(d[b[-1]]) == b[-1]:
        print("YES")
        flag = True
    else:
        print("NO")

    for i in range(0, n):
        if flag == False:
            break
        j = d[a[i]]
        for x in j:
            print(x , end=" ")

        print()













# See PyCharm help at https://www.jetbrains.com/help/pycharm/
