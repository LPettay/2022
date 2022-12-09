# Day3.py
# Lance Pettay
# AdventOfCode2022

priorities = {chr(i): i-96 for i in range(97, 123)} | {chr(i): i-38 for i in range(65,91)}

with open('Day3/input.txt', 'r') as puzzle_input:
    rucksacks = puzzle_input.read().split('\n')

improper_items = []
for rucksack in rucksacks:
    assert(not (len(rucksack) % 2)), f"Compartments are not equally sized"
    
    compartment1 = rucksack[:len(rucksack)//2]
    compartment2 = rucksack[len(rucksack)//2:]

    for c in compartment1:
        if c in compartment2:
            improper_items.append(c)
            break

sum_priorities = sum(priorities[item] for item in improper_items)
print(sum_priorities)
