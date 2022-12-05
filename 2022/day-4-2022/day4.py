#! /usr/bin/env python


def get_min_max_of_range(range):
    return int(range.split('-')[0]), int(range.split('-')[1])


def one_range_fully_contains_other(min1, min2, max1, max2):
    return (min1 <= min2 and max1 >= max2) or (min2 <= min1 and max2 >= max1)


def ranges_overlap(min1, min2, max1, max2):
    return (min1 <= min2 <= max1) or (min2 <= min1 <= max2)


def main():
    with open('day-4-2022/input-1.txt') as rd:
        items = [line.strip() for line in rd.readlines()]
        result_for_problem_1 = 0
        result_for_problem_2 = 0
        for item in items:
            min1, max1 = get_min_max_of_range(item.split(',')[0])
            min2, max2 = get_min_max_of_range(item.split(',')[1])
            if one_range_fully_contains_other(min1, min2, max1, max2):
                result_for_problem_1 += 1
            if ranges_overlap(min1, min2, max1, max2):
                result_for_problem_2 += 1

        print(result_for_problem_1)
        print(result_for_problem_2)


if __name__ == "__main__":
    main()
