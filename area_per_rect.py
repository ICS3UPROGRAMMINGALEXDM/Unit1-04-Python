#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 02//22
# Description: calculates the area and perimeter of a rectangle


def calculate():
    print("Make sure to enter numbers only!")
    num1 = input("What is the height of your retangle? \n").strip()
    num2 = input("What is the width of your rectangle?\n").strip()
    height = int(num1)
    width = int(num2)
    perimeter = (2 * height) + (2 * width)
    area = height * width
    print("The perimeter of your rectangle is {} u. ".format(perimeter))
    print("The area of your rectangle is {} u^2!".format(area))


def main():
    calculate()


if __name__ == "__main__":
    main()
