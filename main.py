# This is a sample Python script.
import random
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    options = [1, 2, 3, 4]
    probabilities = [0.1, 0.1, 0.1,0.9]
    n = random.choices(options, probabilities)
    print(f'Hi, {n}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
