# Day5_part1.py
# Lance Pettay
# AdventOfCode2022

import re

def read_puzzle_input():
    with open('Day5/input.txt', 'r') as puzzle_input:
        return puzzle_input.read()


def parse_stacks(procedure):
    stacks = procedure.split('\n'*2)[0].split('\n')
    column_numbers = stacks[-1]

    parsed_stacks = {}
    column_indices = {}
    for num in column_numbers.split():
        parsed_stacks[int(num)] = []
        column_indices[column_numbers.index(num)] = num

    for row in stacks[:-1][::-1]:
        for i, char in enumerate(row):
            if i in column_indices.keys() and not char == ' ':
                parsed_stacks[int(column_indices[i])].append(char)

    return parsed_stacks


def initiate_procedure(procedure, stacks):
    procedure = procedure.split('\n'*2)[1].rstrip('\n').split('\n')
    
    for row in procedure:
        move, frm, to = [int(match) for match in re.findall('\d+', row)]

        for i in range(move, 0, -1):
            stacks[to].append(stacks[frm].pop())
            i -= 1

    return stacks
        

def main():
    procedure = read_puzzle_input()
    parsed_stacks = parse_stacks(procedure)
    complete_stacks = initiate_procedure(procedure, parsed_stacks)
    solution = ''.join([complete_stacks[k][-1] for k in complete_stacks.keys()])
    print(solution)

if __name__ == '__main__':
    main()