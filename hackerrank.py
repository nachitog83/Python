import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):

    totalCost = float()
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100
    totaCost = meal_cost + tax + tip
    print(totalCost)

    return int(totaCost)

if __name__ == '__main__':
	
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)