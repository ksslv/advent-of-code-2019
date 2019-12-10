"""

Solution for AoC2019.

The Day 2 problem statement and input file can be found on
https://adventofcode.com/2019/day/2

"""

def run_prog(code, noun = 12, verb = 2):
    start = 0

    # create a copy to not modify the original input
    code_copy = code[:]

    code_copy[1] = noun
    code_copy[2] = verb

    while start <= (len(code_copy) - 1):
        if code_copy[start] == 99:
            break

        if code_copy[start] == 1:

            idx1 = code_copy[start + 1]
            idx2 = code_copy[start + 2]
            save_idx = code_copy[start + 3]

            code_copy[save_idx] = code_copy[idx1] + code_copy[idx2]

        elif code_copy[start] == 2:

            idx1 = code_copy[start + 1]
            idx2 = code_copy[start + 2]
            save_idx = code_copy[start + 3]

            code_copy[save_idx] = code_copy[idx1] * code_copy[idx2]

        start += 4
    return code_copy[0]

# Part 2 is brute-forced. TODO: see if there's a better approach
def find_input(code):

    for noun in range(100):
        for verb in range(100):
            if run_prog(code, noun, verb) == 19690720:
                print(100 * noun + verb)
                return 100 * noun + verb


input_file = "input_day2.txt"

with open(input_file) as f:
    code = f.readlines()
    code = [int(num) for num in code[0].split(',')]

    # Part 1 solution
    prog = run_prog(code)
    print(f"Part 1. Value at position 0 after the program terminates: {prog}\n")

    # Part 2 solution
    input = find_input(code)
    print(f"Part 2. The input was: {input}\n")
