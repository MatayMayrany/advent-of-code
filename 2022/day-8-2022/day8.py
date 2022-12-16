#! /usr/bin/env python
import numpy as np


def get_grid_peremeter(items):
    return 2 * (len(items) + len(items[0]) - 2)


def visible_from_direction(tree_height, tree_heights):
    return all(int(height) < int(tree_height) for height in tree_heights)


def tree_is_visible(items, i, j):
    tree_height = items[i][j]
    visible_left = True
    visible_right = True
    visible_up = True
    visible_down = True

    for row in range(0, i):
        if items[row][j] >= tree_height:  # one of heights above is visible
            visible_up = False
    for row in range(i + 1, len(items)):
        if items[row][j] >= tree_height:  # one of heights under is visible
            visible_down = False
            break
    for height in items[i][:j]:  # one of heights to the left is visible
        if height >= tree_height:
            visible_left = False
            break
    for height in items[i][j + 1:]:  # one of heights to the right is visible
        if height >= tree_height:
            visible_right = False
            break

    return visible_left or visible_right or visible_up or visible_down


def get_number_of_visible_trees(items):
    count = 0
    for i in range(1, len(items) - 1):
        for j in range(1, len(items[0]) - 1):
            if tree_is_visible(items, i, j):
                count += 1
    return count + get_grid_peremeter(items)


def get_scenic_score(items, i, j):
    tree_height = items[i][j]
    visible_trees_left = 0
    visible_trees_right = 0
    visible_trees_up = 0
    visible_trees_down = 0
    for row in range(i - 1, -1, -1):
        visible_trees_up += 1
        if items[row][j] >= tree_height:  # one of heights above is visible
            break
    for row in range(i + 1, len(items)):
        visible_trees_down += 1
        if items[row][j] >= tree_height:  # one of heights under is visible
            break
    for height in reversed(items[i][:j]):  # one of heights to the left is visible
        visible_trees_left += 1
        if height >= tree_height:
            break
    for height in items[i][j + 1:]:  # one of heights to the right is visible
        visible_trees_right += 1
        if height >= tree_height:
            break

    return visible_trees_right * visible_trees_left * visible_trees_down * visible_trees_up


def get_highest_scenic_score(items):
    grid = items
    highest_scenic_score = 0
    for i in range(1, len(items)):
        for j in range(1, len(items[0])):
            scenic_score = get_scenic_score(grid, i, j)
            if scenic_score > highest_scenic_score:
                highest_scenic_score = scenic_score
    return highest_scenic_score


def main():
    with open('day-8-2022/input-1.txt') as rd:
        items = np.array([[int(l) for l in line.strip()] for line in rd.readlines()])
        number_of_visible_trees = get_number_of_visible_trees(items)  # part 1
        highest_scenic_score = get_highest_scenic_score(items)  # part 2
        print(number_of_visible_trees)
        print(highest_scenic_score)


if __name__ == "__main__":
    main()
