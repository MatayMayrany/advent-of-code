#! /usr/bin/env python
from collections import defaultdict


def build_map_of_directory_sizes(lines):
    sizes = defaultdict(int)
    path = []
    for line in lines:
        parts = line.split(' ')
        if parts[1] == 'cd':  # ignore ls
            if parts[2] == '..':
                path.pop()
            else:
                path.append(parts[2])
        elif parts[1] == 'ls':
            continue
        elif parts[0] == 'dir':
            continue
        else:
            size = int(parts[0])
            for i in range(1, len(path) + 1):
                sizes['/'.join(path[:i])] += size
    return sizes


def main():
    with open('day-7-2022/input-1.txt') as rd:
        items = [line.strip() for line in rd.readlines()]
        sizes = build_map_of_directory_sizes(items)
        target_memory = 70000000 - 30000000
        size_to_free = sizes['/'] - target_memory
        min_directory_size = 0
        sum = 0
        for key, value in sizes.items():
            if value <= 100000:
                sum += value
            if value >= size_to_free:
                if min_directory_size == 0:
                    min_directory_size = value
                else:
                    min_directory_size = value if value < min_directory_size else min_directory_size
        print(sum)
        print(min_directory_size)


if __name__ == "__main__":
    main()
