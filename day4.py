"""

Solution for AoC2019.

The Day 4 problem statement can be found on
https://adventofcode.com/2019/day/4

The possible passwords are in the [158126, 624574] interval.

"""


lo = 158126
hi = 624574

pt1_res = []
pt2_res = []


def double_digit(num):
    num = [int(x) for x in str(num)]

    for digit in num:
        count = num.count(digit)

        if count >= 2:
            return True
    return False


def double_digit_pt2(num):
    num = [int(x) for x in str(num)]

    for digit in num:
        count = num.count(digit)

        if count == 2:
            return True
    return False


def digits_increase(num):
    num = [int(x) for x in str(num)]

    for i in range(5):
        if num[i] > num[i+1]:
            return False
    return True


for num in range(lo, hi):
    # part1:
    if double_digit(num) and digits_increase(num):
        pt1_res.append(num)

    # part2:
    if double_digit_pt2(num) and digits_increase(num):
        pt2_res.append(num)

print(f"Part 1. Number of possible passwords: {len(pt1_res)}\n")
print(f"Part 2. Number of possible passwords: {len(pt2_res)}\n")
