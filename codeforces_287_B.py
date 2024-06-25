# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math

  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    r , x1, y1, x2, y2 =  map(int, input().split())
    d = (x1 - x2) * ( x1 - x2) + (y1 - y2) * (y1 - y2)
    d = math.sqrt( float (d))
    ans = math.ceil(d / (2 * r))
    print(ans)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
