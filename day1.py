starting_value = 50

def part1():
    with open("day1_input.txt") as f:
        lines = [line.rstrip() for line in f]

    password = 0
    value = starting_value
    for l in lines:
        steps = int(l[1:])
        if l[0] == 'L':
            value -= steps
        if l[0] == 'R':
            value += steps
        value %= 100
        
        if value == 0:
            password += 1
    
    print("part. 1 password:", password)


def part2():
    with open("day1_input.txt") as f:
        lines = [line.rstrip() for line in f]

    password = 0
    value = starting_value
    for l in lines:
        prev_value = value
        steps = int(l[1:])

        if steps > 100:
            password += steps//100
            steps %= 100

        if l[0] == 'L':
            value -= steps
        if l[0] == 'R':
            value += steps
        
        if (prev_value != 0 and value <= 0) or value >= 100:
            password += 1
        value %= 100
        
        # print(l, value, password)
    
    print("part. 2 password:", password)


if __name__ == "__main__":
    part1()
    part2()