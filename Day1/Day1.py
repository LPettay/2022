# Day1.py
# Lance Pettay
# AdventOfCode2022

with open('Day1/input.txt', 'r') as puzzle_input:
    inventory = puzzle_input.read().strip('\n')

elves = inventory.split('\n'*2)

elf_calories = []
for elf in elves:
    total_calories = sum(int(cals) for cals in elf.split('\n'))
    elf_calories.append(total_calories)

most_calories = max(elf_calories)
print(most_calories)
