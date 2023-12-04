#!/usr/bin/python3

input = open("input.txt").read()


def parse_nums(l):
    return set(map(int, (n for n in l.split(" ") if n.isdigit())))


def parse_line(l):
    l = l.split(":")
    rest = l[1].split("|")
    win = parse_nums(rest[0])
    nums = parse_nums(rest[1])
    return (win, nums)


def parse(input):
    return list(map(parse_line, input.splitlines()))


def match_count(game):
    win, nums = game
    return len(win.intersection(nums))


def score(c):
    return 1 << (c - 1) if c > 0 else 0


games = parse(input)
games_match_count = list(map(match_count, games))
part1 = sum(map(score, games_match_count))
print(f"part1: {part1}")


memo = dict()


def p(id):
    if memo.get(id) is not None:
        return
    copies = games_match_count[id]
    if copies == 0:
        memo[id] = 1
    else:
        r = range(id + 1, id + copies + 1)
        [p(i) for i in r]
        memo[id] = 1 + sum(map(lambda n: memo[n], r))


for i in range(0, len(games_match_count)):
    p(i)

part2 = sum(memo.values())
print(f"part2: {part2}")
