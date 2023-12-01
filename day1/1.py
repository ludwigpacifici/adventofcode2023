#!/usr/bin/python3

from pathlib import Path


input = Path("input.txt").read_text()


def part1(l):
    first = 0
    for c in l:
        if c.isdigit():
            first = int(c)
            break
    last = 0
    for c in list(reversed(l)):
        if c.isdigit():
            last = int(c)
            break
    return (first, last)


def part2(l):
    first = 0
    for i in range(0, len(l)):
        if l[i].isdigit():
            first = int(l[i])
            break
        elif l[i:].startswith("one"):
            first = 1
            break
        elif l[i:].startswith("two"):
            first = 2
            break
        elif l[i:].startswith("three"):
            first = 3
            break
        elif l[i:].startswith("four"):
            first = 4
            break
        elif l[i:].startswith("five"):
            first = 5
            break
        elif l[i:].startswith("six"):
            first = 6
            break
        elif l[i:].startswith("seven"):
            first = 7
            break
        elif l[i:].startswith("eight"):
            first = 8
            break
        elif l[i:].startswith("nine"):
            first = 9
            break

    last = 0
    for i in reversed(range(0, len(l))):
        if l[i].isdigit():
            last = int(l[i])
            break
        elif l[: i + 1][::-1].startswith("eno"):
            last = 1
            break
        elif l[: i + 1][::-1].startswith("owt"):
            last = 2
            break
        elif l[: i + 1][::-1].startswith("eerht"):
            last = 3
            break
        elif l[: i + 1][::-1].startswith("ruof"):
            last = 4
            break
        elif l[: i + 1][::-1].startswith("evif"):
            last = 5
            break
        elif l[: i + 1][::-1].startswith("xis"):
            last = 6
            break
        elif l[: i + 1][::-1].startswith("neves"):
            last = 7
            break
        elif l[: i + 1][::-1].startswith("thgie"):
            last = 8
            break
        elif l[: i + 1][::-1].startswith("enin"):
            last = 9
            break

    return (first, last)


def run(f):
    lfs = map(lambda l: f(l), input.splitlines())

    sum = 0
    for lf in list(lfs):
        n = lf[0] * 10 + lf[-1]
        sum += n
    return sum


print(f"part1: {run(part1)}")
print(f"part2: {run(part2)}")
