starting_value = 50

if __name__ == "__main__":
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
    
    print("password:", password)