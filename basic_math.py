#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 02//22
# Description: Displays basic math operations


import math

add = 5 + 3
sub = 17 - 9
times = 12 * 13
div = 11 / 2
power = pow(4, 3)
square = math.sqrt(144)
print(
    "5 + 3 = {}, \n\n17 - 9 = {},".format(
        add,
        sub,
    )
)
print("\n\n12 x 13 = {},".format(times))
print("\n\n11 / 2 = {}, \n\n4^3 = {},".format(div, power))
print("\n\n2_/144 = {} ".format(square))
