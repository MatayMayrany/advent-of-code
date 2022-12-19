#! /usr/bin/env python
import numpy as np
import string

letter_to_height = {}


def is_valid_cell(child_row, child_col, parent_height, grid, visited):
    exists = (0 <= child_row < len(grid)) & (0 <= child_col < len(grid[0]))
    if not exists:
        return False
    if visited[child_row][child_col]:
        return False
    if letter_to_height[grid[child_row][child_col]] > parent_height + 1:
        return False
    return True


def bfs(grid, S):
    # visited grid
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # apply BFS on matrix starting from source
    queue = [S]
    visited[S.row][S.col] = True
    while len(queue) != 0:
        current = queue.pop(0)
        if grid[current.row][current.col] == 'E':
            return current.dist

        # check possible children
        row_up, col_up = current.row - 1, current.col
        row_down, col_down = current.row + 1, current.col
        row_left, col_left = current.row, current.col - 1
        row_right, col_right = current.row, current.col + 1
        next_dist = current.dist + 1

        if is_valid_cell(row_up, col_up, current.height, grid, visited):  # up
            child_up = Node(row_up, col_up, letter_to_height[grid[row_up][col_up]], next_dist)
            queue.append(child_up)
            visited[row_up][col_up] = True

        if is_valid_cell(row_down, col_down, current.height, grid, visited):  # down
            child_down = Node(row_down, col_down, letter_to_height[grid[row_down][col_down]], next_dist)
            queue.append(child_down)
            visited[row_down][col_down] = True

        if is_valid_cell(row_left, col_left, current.height, grid, visited):  # left
            child_left = Node(row_left, col_left, letter_to_height[grid[row_left][col_left]], next_dist)
            queue.append(child_left)
            visited[row_left][col_left] = True

        if is_valid_cell(row_right, col_right, current.height, grid, visited):  # up
            child_right = Node(row_right, col_right, letter_to_height[grid[row_right][col_right]], next_dist)
            queue.append(child_right)
            visited[row_right][col_right] = True

    return -1


class Node:
    def __init__(self, row, col, height, dist):
        self.row = row
        self.col = col
        self.height = height
        self.dist = dist

    def __repr__(self):
        return f"Node({self.row}, {self.col}, {self.dist})"


def build_priority_map():
    i = 1
    for letter in string.ascii_letters:
        if letter == 'E':
            letter_to_height[letter] = letter_to_height['z']
        else:
            letter_to_height[letter] = i
            i += 1


def find_start(grid):
    S = Node(0, 0, 0, 0)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                S.row = row
                S.col = col
                S.height = letter_to_height['a']
                break
    return S


def get_all_elements_with_lowest_elevation(grid):
    possible_starts = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S' or grid[row][col] == 'a':
                possible_start = Node(row, col, 1, 0)
                possible_starts.append(possible_start)
    return possible_starts


def main():
    build_priority_map()
    with open('day-12-2022/input-1.txt') as rd:
        grid = [line.strip() for line in rd.readlines() if line != '\n']

        # Part 1
        S = find_start(grid)
        dist = bfs(grid, S)
        print(dist)

        # Part 2
        possible_starts = get_all_elements_with_lowest_elevation(grid)
        min_dist = float('inf')
        for start in possible_starts:
            dist_from_start = bfs(grid, start)
            if -1 < dist_from_start < min_dist:
                min_dist = dist_from_start
        print(min_dist)


if __name__ == "__main__":
    main()
