# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    points = {}
    a_unique = []
    d = {}

    for i in a:
        if i not in points:
            #d[i] = 0
            points[i] = 0
            a_unique.append(i)
        #d[i] += 1
        points[i] += i

    a_unique.sort()
    gained_point = [0] * len(a_unique)

    for i in range(0, len(a_unique)):
        if i == 0:
            gained_point[i] = points[a_unique[i]]
        else:
            j = i-1
            if a_unique[j] == a_unique[i] - 1:
                j -= 1
            if j < 0:
                gained_point[i] = points[a_unique[i]]
            else:
                gained_point[i] = gained_point[j] + points[a_unique[i]]
            gained_point[i] = max(gained_point[i-1], gained_point[i])

    ans = gained_point[-1]
    print(ans)





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
