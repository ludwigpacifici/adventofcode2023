#!/usr/bin/python3

from functools import reduce
import math


input = open("input.txt").read()


def parse_turn(t):
    rgb = [0] * 3
    for x in map(lambda d: d.split(" "), t.split(", ")):
        v = int(x[0])
        if x[1] == "red":
            rgb[0] = v
        elif x[1] == "green":
            rgb[1] = v
        elif x[1] == "blue":
            rgb[2] = v
    return rgb


def parse_line(l):
    s = l.split(":")
    game = int(s[0].split(" ")[1].strip(":"))
    turns = s[1].strip().split("; ")
    turns = list(map(parse_turn, turns))
    return (game, turns)


games = list(map(parse_line, input.splitlines()))


def is_valid(cubes):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14
    return cubes[0] <= MAX_RED and cubes[1] <= MAX_GREEN and cubes[2] <= MAX_BLUE


valid = (g[0] for g in games if all(map(is_valid, g[1])))


part1 = sum(list(valid))
print(f"part1: {part1}")


def max3(turns):
    return reduce(
        lambda a, b: [max(a[0], b[0]), max(a[1], b[1]), max(a[2], b[2])],
        turns,
        [0, 0, 0],
    )


turns = map(lambda g: g[1], games)
max3 = map(max3, turns)
part2 = sum(map(math.prod, max3))
print(f"part2: {part2}")
