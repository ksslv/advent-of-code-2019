"""

Solution for AoC2019.

The Day 1 problem statement and input file can be found on
https://adventofcode.com/2019/day/1

"""

# Recursive function for part 2.
def helper_pt2(num):
    res = int(num) // 3 - 2
    if res <= 0:
        return 0
    return res + helper_pt2(res)



input_file = "input_day1.txt"

with open(input_file) as f:
    total_pt1 = 0
    total_pt2 = 0

    lines = f.readlines()

    for line in lines:
        num = int(line) // 3 - 2

        total_pt1 += num # this is correct
        total_pt2 += helper_pt2(line)

    print(f"Part 1 Total fuel: {total_pt1}\n"
          f"Part 2 Total fuel: {total_pt2}"
         )
