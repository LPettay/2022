# Day2.py
# Lance Pettay
# AdventOfCode2022

translator = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win'
}

shape_scores = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3, 
}

outcome_scores = {
    'Lose': 0,
    'Draw': 3,
    'Win': 6
}

running_score = 0
with open('Day2/input.txt', 'r') as strategy_guide:
    for round in strategy_guide:
        opponent_move, my_outcome = (translator[move] for move in round.strip('\n').split(' '))
        
        if my_outcome == 'Win':
            if opponent_move == 'Scissors':
                move = 'Rock'
            elif opponent_move == 'Paper':
                move = 'Scissors'
            else:
                move = 'Paper'
        
        elif my_outcome == 'Lose':
            if opponent_move == 'Rock':
                move = 'Scissors'
            elif opponent_move == 'Scissors':
                move = 'Paper'
            else:
                move = 'Rock'
        
        elif my_outcome == 'Draw':
            move = opponent_move

        running_score += (shape_scores[move] + outcome_scores[my_outcome])

print(running_score)
