#! /usr/bin/env python

def get_count_till_all_unique(item, unique_count):
    result = 0
    uniques = []
    for char in item:
        index = len(uniques)
        for unique in reversed(uniques):
            if unique == char:
                del uniques[0:index]
            else:
                index -= 1
        uniques.append(char)
        result += 1
        if len(uniques) == unique_count:
            break
    return result


def main():
    with open('day-6-2022/input-1.txt') as rd:
        items = [line for line in rd.readlines()]
        result_for_problem_one = get_count_till_all_unique(items[0], 4)
        result_for_problem_two = get_count_till_all_unique(items[0], 14)
        print(result_for_problem_one)
        print(result_for_problem_two)


if __name__ == "__main__":
    main()
