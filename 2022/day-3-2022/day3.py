#! /usr/bin/env python
import string

letter_to_priority = {}


def build_priority_map():
    i = 1
    for letter in string.ascii_letters:
        letter_to_priority[letter] = i
        i += 1


def get_priority_of_duplicates(item):
    half_length = len(item) // 2
    first_compartment, second_compartment = item[:half_length], item[half_length:]
    bad_elements = set(first_compartment).intersection(set(second_compartment))
    priority = 0
    for element in bad_elements:
        priority += letter_to_priority[element]
    return priority


def get_priority_of_group_badge(group):
    shared_between_2 = set(group[0]).intersection(set(group[1]))
    (shared_between_3,) = set(group[2]).intersection(shared_between_2)
    return letter_to_priority[shared_between_3]


def main():
    build_priority_map()
    with open('day-3-2022/input-1.txt') as rd:
        items = [line.strip() for line in rd.readlines()]
        problem_1_result = 0
        problem_2_result = 0
        group = []
        for item in items:
            problem_1_result += get_priority_of_duplicates(item)
            group.append(item)
            if len(group) == 3:
                problem_2_result += get_priority_of_group_badge(group)
                group.clear()
        print(problem_1_result)
        print(problem_2_result)


if __name__ == "__main__":
    main()
