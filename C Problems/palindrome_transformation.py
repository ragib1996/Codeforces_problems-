import math

if __name__ == '__main__':
    n, p = map(int, input().split())
    s = input()
    p1 = 0
    p2 = 0
    ans = 0


    s2 = '-'
    s2 += s
    s2 = list(s2)
    changing_index = []
    for i in range(1, int(n/2)+1):
        if p == n - (i-1):
            p = i
        t = abs( ord(s2[i]) - ord(s2[-1-(i-1)]) )
        if t != 0:
            changing_index.append(i)
        if t >= 14:
            ans += (t - (t-13)*2)
        else:
            ans += t
    """
    if n%2 == 1:
        if p > math.ceil(n/2):
            if n - p < p - (math.ceil(n/2) + 1):
               p1 = n
               ans += (n-p)
            else:
               p1 = math.ceil(n/2) + 1
               ans += (p - (math.ceil(n/2) + 1) )
        elif p < math.ceil(n/2):
            if p -1 < math.floor(n/2) - p:
                p1 = 1
                ans += (p-1)
            else:
                p1 = math.floor(n/2)
                ans += (math.floor(n/2) - p)
        else:
            p1 = p+1
            ans += 1
    else:
        if p > int (n/2):
            if n - p <  p - (int(n/2) + 1 ):
                p1 = n
                ans += (n-p)
            else:
                p1 = int (n/2) + 1
                ans += (p - (int(n/2) + 1))
        else:
            if p - 1 < n/2 - p:
                p1 = 1
                ans += (p-1)
            else:
                p1 = int (n/2)
                ans += (int(n/2) - p)
    """
    if len(changing_index) > 0:
       if n % 2 == 1 and p > math.floor(n/2):
          ans += (p-changing_index[0])
       else:
            if p < changing_index[0]:
               ans += (changing_index[-1] - p)
            elif p > changing_index[-1]:
               ans += (p - changing_index[0])
            else:
               if p - changing_index[0] < changing_index[-1] - p:
                  ans += (p-changing_index[0])
                  ans += (changing_index[-1] - changing_index[0])
               else:
                  ans += (changing_index[-1] - p)
                  ans += (changing_index[-1] - changing_index[0])

    print(ans)


