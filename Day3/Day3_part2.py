# Day3_part2.py
# Lance Pettay
# AdventOfCode2022

priorities = {chr(i): i-96 for i in range(97, 123)} | {chr(i): i-38 for i in range(65,91)}

with open('Day3/input.txt', 'r') as puzzle_input:
    rucksacks = puzzle_input.read().split('\n')

group_size = 3
groups = [rucksacks[i:i+group_size] for i in range(0, len(rucksacks), 3)]

badges = []
for group in groups:
    for item in group[0]:
        if all(item in sack for sack in group):
            badges.append(item)
            break

sum_priorities = sum(priorities[item] for item in badges)
print(sum_priorities)
