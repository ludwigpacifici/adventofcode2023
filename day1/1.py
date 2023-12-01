#!/usr/bin/python3

from pathlib import Path


input = Path("input.txt").read_text()


def part1(l):
    first = int(next(filter(lambda c: c.isdigit(), l)))
    last = int(next(filter(lambda c: c.isdigit(), reversed(l))))
    return (first, last)


def part2(l):
    first = 0
    for i in range(0, len(l)):
        remaining = l[i:]
        if remaining[0].isdigit():
            first = int(remaining[0])
            break
        elif remaining.startswith("one"):
            first = 1
            break
        elif remaining.startswith("two"):
            first = 2
            break
        elif remaining.startswith("three"):
            first = 3
            break
        elif remaining.startswith("four"):
            first = 4
            break
        elif remaining.startswith("five"):
            first = 5
            break
        elif remaining.startswith("six"):
            first = 6
            break
        elif remaining.startswith("seven"):
            first = 7
            break
        elif remaining.startswith("eight"):
            first = 8
            break
        elif remaining.startswith("nine"):
            first = 9
            break

    last = 0
    reversed_l = l[::-1]
    for i in range(0, len(l)):
        remaining = reversed_l[i:]
        if remaining[0].isdigit():
            last = int(remaining[0])
            break
        elif remaining.startswith("eno"):
            last = 1
            break
        elif remaining.startswith("owt"):
            last = 2
            break
        elif remaining.startswith("eerht"):
            last = 3
            break
        elif remaining.startswith("ruof"):
            last = 4
            break
        elif remaining.startswith("evif"):
            last = 5
            break
        elif remaining.startswith("xis"):
            last = 6
            break
        elif remaining.startswith("neves"):
            last = 7
            break
        elif remaining.startswith("thgie"):
            last = 8
            break
        elif remaining.startswith("enin"):
            last = 9
            break

    return (first, last)


def run(fun):
    lines = map(lambda l: fun(l), input.splitlines())
    lines = map(lambda fl: fl[0] * 10 + fl[1], lines)
    return sum(lines)


print(f"part1: {run(part1)}")
print(f"part2: {run(part2)}")
