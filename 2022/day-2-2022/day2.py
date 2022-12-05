#! /usr/bin/env python

letter_to_move = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}

letter_to_result = {
    'X': 'Lose',
    'Y': 'Draw',
    'Z': 'Win',
}

move_to_score = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3
}


def player_wins(my_move, opponent_move):
    if (my_move == 'Paper' and opponent_move == 'Rock') \
            or (my_move == 'Rock' and opponent_move == 'Scissors') \
            or (my_move == 'Scissors' and opponent_move == 'Paper'):
        return True


def get_losing_move(opponent_move):
    if opponent_move == 'Rock':
        return 'Scissors'
    elif opponent_move == 'Paper':
        return 'Rock'
    else:
        return 'Paper'


def get_winning_move(opponent_move):
    if opponent_move == 'Rock':
        return 'Paper'
    elif opponent_move == 'Paper':
        return 'Scissors'
    else:
        return 'Rock'


def get_my_move(wanted_result, opponent_move):
    if wanted_result == 'Draw':
        return opponent_move
    if wanted_result == 'Lose':
        return get_losing_move(opponent_move)
    else:
        return get_winning_move(opponent_move)


def find_total_score(items):
    total_score = 0
    for item in items:
        moves = item.split(' ')
        opponent_move = letter_to_move.get(moves[0])
        wanted_result = letter_to_result.get(moves[1])

        my_move = get_my_move(wanted_result, opponent_move)

        # score from move
        total_score += move_to_score.get(my_move)

        # score from result
        if my_move == opponent_move:
            total_score += 3  # draw
        else:
            total_score += 6 if player_wins(my_move, opponent_move) else 0
    return total_score


def main():
    with open('day-2-2022/input-1.txt') as rd:
        items = [line.strip() for line in rd.readlines()]
        total_score = find_total_score(items)
        print(total_score)


if __name__ == "__main__":
    main()
