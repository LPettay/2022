# Day4_part1.py
# Lance Pettay
# AdventOfCode2022

with open('Day4\input.txt', 'r') as puzzle_input:
    assignments = puzzle_input.read().rstrip('\n').split('\n')

overlap_counter = 0
for pair in assignments:
    elf1_sections, elf2_sections = ([int(s) for s in section.split('-')] for section in pair.split(','))
    print('Hold')
    if all(sections in range(elf1_sections[0], elf1_sections[1]+1) for sections in range(elf2_sections[0], elf2_sections[1]+1)):
        overlap_counter += 1
    elif all(sections in range(elf2_sections[0], elf2_sections[1]+1) for sections in range(elf1_sections[0], elf1_sections[1]+1)):
        overlap_counter += 1

print(overlap_counter)
