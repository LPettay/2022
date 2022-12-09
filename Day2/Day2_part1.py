# Day2_part1.py
# Lance Pettay
# AdventOfCode2022

translator = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors'
}

shape_scores = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3, 
}

outcome_scores = {
    'Lost': 0,
    'Draw': 3,
    'Won': 6
}

running_score = 0
with open('Day2/input.txt', 'r') as strategy_guide:
    for round in strategy_guide:
        opponent_move, my_move = (translator[move] for move in round.strip('\n').split(' '))
        
        if my_move == 'Rock':
            if opponent_move == 'Scissors':
                outcome = 'Won'
            elif opponent_move == 'Paper':
                outcome = 'Lost'
            else:
                outcome = 'Draw'
        
        elif my_move == 'Paper':
            if opponent_move == 'Rock':
                outcome = 'Won'
            elif opponent_move == 'Scissors':
                outcome = 'Lost'
            else:
                outcome = 'Draw'
        
        elif my_move == 'Scissors':
            if opponent_move == 'Paper':
                outcome = 'Won'
            elif opponent_move == 'Rock':
                outcome = 'Lost'
            else:
                outcome = 'Draw'

        running_score += (shape_scores[my_move] + outcome_scores[outcome])

print(running_score)
