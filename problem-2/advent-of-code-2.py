#! /usr/bin/env python

def main():
    with open('problem-2/input-advent-of-code-2') as rd:
        commands = [x.strip().split() for x in rd.readlines()]
        part1(commands=commands)
        part2(commands)
        
def part1(commands):
    depth = 0
    position = 0
    for command in commands:
        if (command[0] == 'forward'):
            position += int(command[1])
        else:
            depth = depth + int(command[1]) if command[0] == 'down' else depth - int(command[1])
    print("total depth * position", position * depth)

def part2(commands):
    depth = 0
    position = 0
    aim = 0
    for command in commands: 
        if (command[0] == 'forward'):
            position += int(command[1])
            depth += aim * int(command[1])
        else:
            aim = aim + int(command[1]) if command[0] == 'down' else aim - int(command[1])
    print("total depth * position", depth * position)
if __name__ == "__main__":
    main()
