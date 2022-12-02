#! /usr/bin/env python

def find_max_calories_carried(items):
    maxCalories = 0
    tracker = 0
    for item in items:
        if item == '':
            maxCalories = tracker if tracker > maxCalories else maxCalories
            tracker = 0
        else:
            tracker += int(item)
    print('max calories: ', maxCalories)


def find_top_3_calories_carried(items):
    maxCalories = []
    tracker = 0
    for item in items:
        if item == '':
            maxCalories.append(tracker)
            tracker = 0
        else:
            tracker += int(item)
    maxCalories.sort()
    print('max calories: ', sum(maxCalories[-3:]))


def main():
    with open('day-1-2022/input-1.txt') as rd:
        items = [line.strip() for line in rd.readlines()]
        find_max_calories_carried(items)
        find_top_3_calories_carried(items)


if __name__ == "__main__":
    main()
