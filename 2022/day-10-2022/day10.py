#! /usr/bin/env python
def calculate_total(interesting_cycles):
    sum = 0
    for key, value in interesting_cycles.items():
        sum += value * key
    return sum


def part1(commands):
    interesting_cycles = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
    X = 1
    cycles_finished = 0
    for command in commands:
        parts = command.split(' ')
        if parts[0] == 'noop':
            cycles_finished += 1

        elif parts[0] == 'addx':
            cycles_finished += 1
            if cycles_finished + 1 in interesting_cycles:
                interesting_cycles[cycles_finished + 1] = X
            cycles_finished += 1
            X += int(parts[1])

        if cycles_finished + 1 in interesting_cycles:
            interesting_cycles[cycles_finished + 1] = X
    return interesting_cycles


def update_grid(grid, cycles_finished, sprite):
    cycle_row = int(cycles_finished / 40)
    cycle_position = cycles_finished % 40
    if cycle_row == len(grid):
        grid.append([])
    if cycle_position in sprite:
        grid[cycle_row].append('#')
    else:
        grid[cycle_row].append('.')


def part2(commands):
    sprite = [0, 1, 2]
    cycles_finished = 0
    grid = [[]]
    X = 1
    for command in commands:
        update_grid(grid, cycles_finished, sprite)

        parts = command.split(' ')
        if parts[0] == 'noop':
            cycles_finished += 1

        elif parts[0] == 'addx':
            cycles_finished += 1
            update_grid(grid, cycles_finished, sprite)
            cycles_finished += 1
            X += int(parts[1])
            sprite = [X - 1, X, X + 1]

    return grid


def main():
    with open('day-10-2022/input-1.txt') as rd:
        commands = [line.strip() for line in rd.readlines()]
        interesting_cycles = part1(commands)
        answer_part_1 = calculate_total(interesting_cycles)
        answer_part_2 = part2(commands)
        for row in answer_part_2:
            print(row)


if __name__ == "__main__":
    main()
