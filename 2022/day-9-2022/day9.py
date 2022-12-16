#! /usr/bin/env python
import numpy as np

visited = {'0,0'}
larger_example = ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']


def move_tail(head, tail, last_tail):
    x_difference = head[0] - tail[0]
    y_difference = head[1] - tail[1]
    if x_difference > 1:
        tail[0] += 1
        if y_difference > 0:
            tail[1] += 1
        elif y_difference < 0:
            tail[1] -= 1
    elif x_difference < -1:
        tail[0] -= 1
        if y_difference > 0:
            tail[1] += 1
        elif y_difference < 0:
            tail[1] -= 1
    elif y_difference > 1:
        tail[1] += 1
        if x_difference > 0:
            tail[0] += 1
        elif x_difference < 0:
            tail[0] -= 1
    elif y_difference < -1:
        tail[1] -= 1
        if x_difference > 0:
            tail[0] += 1
        elif x_difference < 0:
            tail[0] -= 1
    if last_tail:
        tail_string = ','.join(str(x) for x in tail)
        visited.add(tail_string)


def part1(steps, head, tail, increment, vertical):
    for i in range(0, steps):
        # move head once
        if vertical:
            head[1] += increment
        else:
            head[0] += increment
        # move tail if it needs and increment once
        move_tail(head, tail, True)


def part2(steps, head, tails, increment, vertical):
    for i in range(0, steps):
        # move head once
        if vertical:
            head[1] += increment
        else:
            head[0] += increment
        # move tail if it needs and increment once
        current_head = head
        for j, tail in enumerate(tails):
            if j == len(tails) - 1:
                move_tail(current_head, tail, True)
            else:
                move_tail(current_head, tail, False)
                current_head = tail


def main():
    with open('day-9-2022/input-1.txt') as rd:
        commands = [line.strip() for line in rd.readlines()]
        head = [0, 0]
        # part 1
        tail = [0, 0]
        for command in commands:
            direction, steps = command.split(' ')
            vertical = True if direction == 'U' or direction == 'D' else False
            increment = 1 if direction == 'U' or direction == 'R' else -1
            part1(int(steps), head, tail, increment, vertical)
        print(len(visited))
        visited.clear()
        # part 2
        head = [0, 0]
        tails = [
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0],
            [0, 0]
        ]
        visited.add('0,0')
        for command in commands:
            direction, steps = command.split(' ')
            vertical = True if direction == 'U' or direction == 'D' else False
            increment = 1 if direction == 'U' or direction == 'R' else -1
            part2(int(steps), head, tails, increment, vertical)
        print(len(visited))


if __name__ == "__main__":
    main()
