# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    m,s = map(int, input().split())

    tm= m
    ts = s
    part1 = ""
    part2 = ''
    t = ''
    if ts == 0:
        b = False

    while(tm != 0):

        if s > m *9 or ( s <= 0 and m >1) :
            break
        if ts >= 9:
            part1 = part1 +'9'
            ts = ts - 9
            tm = tm - 1
        else:
            if ts == 0 and len(part2) == 0 and len(part1) > 0:
                a = part1[-1]
                part1 = list(part1)
                part1.pop()
                part1 = ''.join(part1)
                part2 = str(a)
            part2 = part2 + str(ts)
            ts = 0
            tm = tm - 1

    if (part1 != '' or part2 != '')  :
       ans2 = part1 + part2
       #part1 = part1[::-1]
       if part2 != '' and   part2[-1] == '0' and len(part2) >= 2:
          part2 = list(part2)
          a = int(part2[0])
          part2[0] = '1'
          part2[-1] = str(a-1)
          part2 = ''.join(part2)
       ans = part2 + part1

       print(int(ans)," ", int(ans2))
    else:
        print(-1," ",-1)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
