import re
import numpy as np

def part1():
    with open("day6_input.txt") as f:
        lines = [line.rstrip() for line in f]
    
    numbers = []
    for i in range(4):
        numbers.append(re.split(r'\s+', lines[i]))
    symbols = re.split(r'\s+', lines[-1]) 

    grand_total = 0
    for i in range(len(symbols)):
        if symbols[i] == '*':
            grand_total += int(numbers[0][i]) * int(numbers[1][i]) * int(numbers[2][i]) * int(numbers[3][i])
        elif symbols[i] == '+':
            grand_total += int(numbers[0][i]) + int(numbers[1][i]) + int(numbers[2][i]) + int(numbers[3][i])
    print("part. 1 password:", grand_total)

    
def part2():
    with open("day6_input.txt") as f:
        lines = [line for line in f]
    
    symbols = re.split(r'\s+', lines[-1])[:-1]
    numbers = [[] for _ in range(len(symbols))]
    n_i = 0
    
    for l1, l2, l3, l4 in zip(lines[0], lines[1], lines[2], lines[3]):
        n_str = ''.join([l1, l2, l3, l4])
        n_str = re.sub(r'\s', '', n_str)
        if n_str != '':
            n = int(n_str)
            numbers[n_i].append(n)
        else:
            n_i += 1
            
    grand_total = 0
    for s, nums in zip(symbols, numbers):
        if s == '+':
            tot = np.sum(nums)
        elif s == '*':
            tot = np.prod(nums)
        # print(s, nums, tot)
        grand_total += tot
    print("part. 2 password:", grand_total)


if __name__ == "__main__":
    part1()
    part2()
