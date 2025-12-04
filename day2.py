def part1():
    with open("day2_input.txt") as f:
        txt_input = f.read()

    ranges = txt_input.split(',')
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges]
    
    password = 0
    for r in ranges:
        # print(r, end=': ')
        for i in range(1, r[1] + 1):
            if len(str(i)) > len(str(r[1]))//2:
                break
            id_str = str(str(i)*2)
            if len(id_str) > len(str(r[1])) or int(id_str) > r[1]:
                break
            if int(id_str) >= r[0]:
                # print(id_str, end=', ')
                password += int(id_str)
        # print()

    print("part. 1 password:", password)


def part2():
    with open("day2_input.txt") as f:
        txt_input = f.read()

    ranges = txt_input.split(',')
    ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges]

    wrong_ids = set()
    for r in ranges:
        # print(r, end=': ')
        for mult in range(2, len(str(r[1])) + 1):
            for i in range(1, r[1] + 1):
                if len(str(i)) > len(str(r[1]))//2:
                    break
                id_str = str(str(i)*mult)
                if len(id_str) > len(str(r[1])) or int(id_str) > r[1]:
                    break
                if int(id_str) >= r[0]:
                    # print(id_str, end=', ')
                    wrong_ids.add(int(id_str))
        # print()

    password = sum(wrong_ids)
    print("part. 2 password:", password)


if __name__ == "__main__":
    part1()
    part2()