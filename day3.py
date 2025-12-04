def part1():
    with open("day3_input.txt") as f:
        banks = [line.rstrip() for line in f]

    max_joltage = 0

    for b in banks:
        # print(b)
        b_sorted = sorted(b)
        first_digit = b_sorted[-1]
        first_digit_index = b.index(first_digit)
        if first_digit_index == len(b)-1:
            first_digit = b_sorted[-2]
            first_digit_index = b.index(first_digit)
            
        b_sorted = sorted(b[first_digit_index+1:])
        second_digit = b_sorted[-1]
        
        # print(int(f"{first_digit}{second_digit}"))
        max_joltage += int(f"{first_digit}{second_digit}")

    print("part. 1 password:", max_joltage)


def part2():
    with open("day3_input.txt") as f:
        banks = [line.rstrip() for line in f]

    max_joltage = 0

    for b in banks:
        # print(b)
        digits = []
        bank = b
        for i in range(0, 12):
            bank_sorted = sorted(bank)
            biggest_digit = bank_sorted[-1]
            j = 2
            while bank.index(biggest_digit) + (12 - i) > len(bank):
                biggest_digit = bank_sorted[-j]
                j += 1
            biggest_digit_index = bank.index(biggest_digit)
            bank = bank[biggest_digit_index + 1:]
            digits.append(biggest_digit)

        # print("".join(digits))
        max_joltage += int("".join(digits))

    print("part. 2 password:", max_joltage)


if __name__ == "__main__":
    part1()
    part2()
