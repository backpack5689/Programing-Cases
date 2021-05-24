from itertools import combinations

dwarves = []
for i in range(9):
    dwarves.insert(i, int(input()))

for attempt in combinations(dwarves, 7):
    if sum(attempt) == 100:
        for dwarf in attempt:
            print(dwarf)
        break
