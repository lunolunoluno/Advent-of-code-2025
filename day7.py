def part1():
    with open("day7_input.txt") as f:
        lines = [line.rstrip() for line in f]
    
    nb_split = 0
    s_index = lines[0].index("S")
    beam_indexes = [s_index]
    print(lines[0])
    for l in lines[1:]:
        new_beam_indexes = set()
        continuing_beam_indexes = []
        if l.find("^") != -1:
            for i, c in enumerate(list(l)):
                if i in beam_indexes:
                    if c == '^':
                        # split the beam!
                        nb_split += 1
                        new_beam_indexes.add(i - 1)
                        new_beam_indexes.add(i + 1)
                    else:
                        continuing_beam_indexes.append(i)
            if len(new_beam_indexes) != 0:
                beam_indexes = list(new_beam_indexes) + continuing_beam_indexes

        for i in beam_indexes:
            l = l[:i] + "|" + l[i+1:]
        print(l, len(new_beam_indexes))

    print("part. 1 password:", nb_split)

    
def part2_notworking(): # dont know why it doesnt work :(
    with open("day7_input.txt") as f:
        lines = [line.rstrip() for line in f]
    
    lines = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "..............."
    ]

    new_lines = lines
    nb_timelines_total = 0
    cache = {}

    def dfs(depth, beam_index):
        if f"{depth}{beam_index}" in cache.keys():
            # print("USE CACHE", cache[f"{depth}{beam_index}"])
            return cache[f"{depth}{beam_index}"]

        nb_timelines = 0
        if depth < len(lines):
            line = list(lines[depth])
            if line[beam_index] == '^':
                new_beam_indexes = []
                new_beam_indexes.append(beam_index - 1)
                new_beam_indexes.append(beam_index + 1)
                

                for i in new_beam_indexes:
                    l = new_lines[depth]
                    l = l[:i] + "|" + l[i+1:]
                    new_lines[depth] = l
                    # print(l, depth)
                    t = dfs(depth + 1, i)
                    cache[f"{depth + 1}{i}"] = t
                    nb_timelines += t
                
                l = new_lines[depth]
                l = l[:len(line)] + f"{nb_timelines}" 
                new_lines[depth] = l
            else:
                l = new_lines[depth]
                l = l[:beam_index] + "|" + l[beam_index+1:]
                new_lines[depth] = l
                # print(l, depth)
                t = dfs(depth + 1, beam_index)
                cache[f"{depth + 1}{beam_index}"] = t
                nb_timelines += t
        else:
            nb_timelines += 1
        return nb_timelines
    

    s_index = lines[0].index("S")
    # print(lines[0])
    nb_timelines_total = dfs(1, s_index)


    for l in new_lines:
        print(l)

    print("part. 2 password:", nb_timelines_total)
    # 42941677653766 too low
    print(nb_timelines_total > 42941677653766)


def part2():
    with open("day7_input.txt") as f:
        lines = [line.rstrip() for line in f]

    beams = [0] * len(lines[0])
    s_index = lines[0].index("S")
    beams[s_index] = 1

    # print(lines[0])
    for l in lines[1:]:
        if l.find("^") != -1:
            for i, c in enumerate(list(l)):
                if c == '^':
                    if beams[i] > 0:
                        beams[i + 1] += beams[i]
                        beams[i - 1] += beams[i]
                        beams[i] = 0
        # print(l, beams, sum(beams))
    print("part. 2 password:", sum(beams))


if __name__ == "__main__":
    part1()
    part2()
    # part2_notworking()
