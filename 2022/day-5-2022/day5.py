#! /usr/bin/env python

def get_number_of_stacks(items):
    number_of_stacks = 0
    found_digits = False
    for item in items:
        if found_digits:
            break
        for char in item:
            if char.isdigit():
                found_digits = True
                number_of_stacks = int(char) if int(char) > number_of_stacks else number_of_stacks
    return number_of_stacks


def build_stacks(items, number_of_stacks):
    stacks = []
    for i in range(0, number_of_stacks - 1):
        item = items[i]
        index = 0
        for x in range(4, len(item) + 1, 4):
            if len(stacks) < number_of_stacks:
                stacks.append([])
            box = item[x - 4:x]
            if box.strip():
                stacks[index].append(box[1])
            index += 1
    return stacks


def execute_command_1(stacks, command):
    elements = [int(s) for s in command.split() if s.isdigit()]
    stack_to_move_from = stacks[elements[1] - 1]
    stack_to_move_to = stacks[elements[2] - 1]
    for i in range(elements[0]):
        element_to_move = stack_to_move_from[0]
        stack_to_move_to.insert(0, element_to_move)
        stack_to_move_from.remove(element_to_move)
    return stacks


def execute_command_2(stacks, command):
    elements = [int(s) for s in command.split() if s.isdigit()]
    stack_to_move_from = stacks[elements[1] - 1]
    stack_to_move_to = stacks[elements[2] - 1]
    elements_to_move = stack_to_move_from[:elements[0]]
    stack_to_move_to[0:0] = elements_to_move
    for element in elements_to_move:
        stack_to_move_from.remove(element)
    return stacks


def print_result(stacks):
    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)


def main():
    with open('day-5-2022/input-1.txt') as rd:
        items = [line for line in rd.readlines()]
        number_of_stacks = get_number_of_stacks(items)
        stacks = build_stacks(items, number_of_stacks)
        for command in (items[number_of_stacks:]):
            if command.strip():
                # stacks = execute_command_1(stacks, command)
                stacks = execute_command_2(stacks, command)

        print(stacks)
        print_result(stacks)


if __name__ == "__main__":
    main()
