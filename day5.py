def part1():
    with open("day5_input.txt") as f:
        txt_input = f.read()

    inputs = txt_input.strip().split("\n\n")
    fresh_ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in inputs[0].split('\n')]
    
    nb_fresh = 0
    for id in inputs[1].split('\n'):
        id = int(id)
        for r in fresh_ranges:
            if id >= r[0] and id <= r[1]:
                nb_fresh+=1
                break
    
    print("part. 1 password:", nb_fresh)


# def part2_desontwork():
#     with open("day5_input.txt") as f:
#         txt_input = f.read()

#     txt_input = """
# 3-5
# 10-14
# 16-20
# 12-18"""

#     inputs = txt_input.strip().split("\n\n")

#     fresh_ids = []
#     for r in inputs[0].split('\n'):
#         print(r)
#         a = int(r.split('-')[0])
#         b = int(r.split('-')[1])
#         new_range = True
#         for ids in fresh_ids:
#             if ids[0] < a and ids[1] > b:
#                 print(f"({a} - {b}) fully in the range ({ids[0]} - {ids[1]})")
#                 new_range = False
#                 break # (a - b) fully in the range (ids[0] - ids[1])
#             elif a < ids[0] and b > ids[1]:
#                 print(f"({ids[0]} - {ids[1]}) fully in the range ({a} - {b})")
#                 new_range = False
#                 ids[0] = a
#                 ids[1] = b
#                 break # (ids[0] - ids[1]) fully in the range (a - b)
#             elif a < ids[0] and b > ids[0]:
#                 print(f"range is updated to ({a} - {ids[1]})")
#                 new_range = False
#                 ids[0] = a
#                 break # range is updated to (a - ids[1])
#             elif a < ids[1] and b > ids[1]:
#                 print(f"range is updated to ({ids[0]} - {b})")
#                 new_range = False
#                 ids[1] = b
#                 break # range is updated to (ids[0] - b)               
#         if new_range:
#             print(f"{r} is a new range")
#             fresh_ids.append([a, b])

#     print(fresh_ids)
#     print("part. 2 password:", len(fresh_ids))


def part2():
    with open("day5_input.txt") as f:
        txt_input = f.read()

    inputs = txt_input.strip().split("\n\n")
    fresh_ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in inputs[0].split('\n')]
    fresh_ranges = sorted(fresh_ranges)

    # solution from https://www.reddit.com/r/adventofcode/comments/1pemdwd/comment/nsshk8y/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
    solution = 0
    range_temp = fresh_ranges[0]
    for range in fresh_ranges[1:]:
        if range[1] <= range_temp[1]:
            pass
        elif range[0] > range_temp[1]:
            solution += 1 + (range_temp[1] - range_temp[0])
            range_temp = range
        elif range[0] <= range_temp[1]:
            range_temp = (range_temp[0], range[1])
    solution += 1 + (range_temp[1] - range_temp[0])
    print("part. 2 password:", solution)

if __name__ == "__main__":
    part1()
    part2()
