# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = input()
    num_7 = 0
    num_4 = 0

    for i in n:
        if int(i) == 7:
            num_7 = num_7 + 1
        elif int(i) == 4:
            num_4 = num_4 + 1

    if num_4 > 0 and num_7 > 0:
      if num_4 > num_7:
         print('4')
      elif num_7 > num_4:
         print('7')
      else:
          print('4')
    elif num_7 > 0 and num_4 == 0:
        print('7')
    elif num_4 > 0 and num_7 == 0:
        print('4')
    else:
        print('-1')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
