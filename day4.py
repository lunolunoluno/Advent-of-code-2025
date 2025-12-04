def part1():
    with open("day4_input.txt") as f:
        diagram = [line.rstrip() for line in f]

    nb_roll_accessible = 0
    for i, row in enumerate(diagram):
        for j, spot in enumerate(row):
            if spot == "@":
                nb_rolls_adj = 0
                for ii in range(-1, 2):
                    if i + ii < 0 or i + ii >= len(diagram):
                        # out of range
                        continue
                    for jj in range(-1, 2):
                        if ii == 0 and jj == 0:
                            # crt spot
                            # print(f"\033[41m{spot}\033[0m", end='')
                            continue
                        if j + jj < 0 or j + jj >= len(row):
                            # out of range
                            continue

                        # print(diagram[i+ii][j+jj], end='')
                        if diagram[i + ii][j + jj] == "@":
                            nb_rolls_adj += 1
                #     print()
                # print(nb_rolls_adj)
                # print("="*40)
                if nb_rolls_adj < 4:
                    nb_roll_accessible += 1
    print("part. 1 password:", nb_roll_accessible)


def part2():
    with open("day4_input.txt") as f:
        diagram = [line.rstrip() for line in f]

    total_nb_roll_removed = 0
    while True:
        # print(diagram)
        updated_diagram = diagram
        nb_roll_removed = 0
        for i, row in enumerate(diagram):
            for j, spot in enumerate(row):
                if spot == "@":
                    nb_rolls_adj = 0
                    for ii in range(-1, 2):
                        if i + ii < 0 or i + ii >= len(diagram):
                            # out of range
                            continue
                        for jj in range(-1, 2):
                            if ii == 0 and jj == 0:
                                # crt spot
                                continue
                            if j + jj < 0 or j + jj >= len(row):
                                # out of range
                                continue

                            if diagram[i + ii][j + jj] == "@":
                                nb_rolls_adj += 1

                    if nb_rolls_adj < 4:
                        updated_diagram[i] = diagram[i][:j] + "x" + diagram[i][j + 1 :]
                        nb_roll_removed += 1

        diagram = updated_diagram
        total_nb_roll_removed += nb_roll_removed
        if nb_roll_removed == 0:
            break

    print("part. 2 password:", total_nb_roll_removed)


if __name__ == "__main__":
    part1()
    part2()
