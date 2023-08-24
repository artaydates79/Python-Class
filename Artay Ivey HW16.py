# Artay Ivey
# Homework assignment Week 1

import math

def calcmaturity(time, temp, ratio):

    maturity = 23.7 * time ** 3 + temp / 273 + math.log(ratio)
    print(maturity)

calcmaturity(10,72,34.5)