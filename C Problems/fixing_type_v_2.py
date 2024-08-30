

if __name__ == '__main__':
    n = input()
    n = list(n)
    i = 0

    while i < len(n):
        if i + 2 < len(n) and n[i] == n[i+1] and n[i+1] == n[i+2]:
            n[i] = '-'
        elif i + 3 < len(n) and n[i] == n[i+1] and n[i+1] != n[i+2] and n[i+2] == n[i+3]:
            j = i + 4
            while j < len(n):
                if n[j] != n[i+3]:
                    break
                n[j] = '-'
                j += 1
            n[i+3] = '-'
            i = j-1

        i += 1

    for i in n:
        if i != '-':
            print(i, end='')
