# Right Shift by Division

from math import floor

def shift_to_right(x, y):
    number = 1

    for i in range(y):
        number = number * 2

    return floor(x / number)

def main():
    n = int(input("Number: "))
    n2 = int(input("Second number: "))

    print("shift: ", shift_to_right(n, n2))

if __name__ == "__main__":
    main()