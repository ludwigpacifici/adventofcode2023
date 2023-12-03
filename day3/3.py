#!/usr/bin/python3

input = open("input.txt").read()


input = list(input.splitlines())
lines = len(input)
columns = len(input[0])


def to_dict(schematic):
    d = dict()
    for l in range(0, len(schematic)):
        for c in range(0, len(schematic[0])):
            d[(l, c)] = schematic[l][c]
    return d


def symbol_coord(schematic, l, c):
    ch = schematic.get((l, c))
    if (ch is not None) and (ch != ".") and (not ch.isdigit()):
        return (l, c)
    else:
        return None


schematic = to_dict(input)


def neighbors(l, c):
    return [
        (l - 1, c - 1),
        (l - 1, c),
        (l - 1, c + 1),
        (l, c - 1),
        (l, c + 1),
        (l + 1, c - 1),
        (l + 1, c),
        (l + 1, c + 1),
    ]


def adjacent_symbols(schematic, l, c):
    return [
        x
        for x in map(lambda lc: symbol_coord(schematic, lc[0], lc[1]), neighbors(l, c))
        if x is not None
    ]


def register_num(num_adjacents, num, adjacents):
    if num == "":
        return (num_adjacents, "", set())

    if not adjacents:
        return (num_adjacents, "", set())

    num_adjacents.append((int(num), adjacents))

    return (num_adjacents, "", set())


num_adjacents = []
num = ""
adjacents = set()

for l in range(0, lines):
    num_adjacents, num, adjacents = register_num(num_adjacents, num, adjacents)
    for c in range(0, columns):
        ch = schematic.get((l, c))
        if ch.isdigit():
            num += ch
            adjacents |= set(adjacent_symbols(schematic, l, c))
        else:
            num_adjacents, num, adjacents = register_num(num_adjacents, num, adjacents)


part1 = sum(map(lambda x: x[0], num_adjacents))
print(f"part1: {part1}")


gears_nums = dict()
for num, adjacents in num_adjacents:
    for a in adjacents:
        if schematic.get(a) == "*":
            x = gears_nums.get(a, [])
            x.append(num)
            gears_nums.update({a: x})


part2 = 0
for values in gears_nums.values():
    if len(values) == 2:
        part2 += values[0] * values[1]

print(f"part2: {part2}")
