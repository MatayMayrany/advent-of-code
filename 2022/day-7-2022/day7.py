#! /usr/bin/env python
def build_map_of_directory_sizes(lines):
    directory_sizes = {}
    directory_parents = {}
    current_directory = ''
    current_size = 0
    for line in lines:
        parts = line.split(' ')
        if line[0] == '$':  # ignore ls
            if parts[1] == 'cd':
                if current_directory and current_directory not in directory_sizes:
                    directory_sizes[current_directory] = current_size
                    current_size = 0
                directory = parts[2]
                current_directory = directory_parents[current_directory] if directory == '..' else directory
        else:
            if parts[0] == 'dir':
                directory_parents[parts[1]] = current_directory
            else:
                current_size += int(parts[0])

    directory_sizes[current_directory] = current_size
    for directory, parent in directory_parents.items():
        directory_sizes[parent] += directory_sizes[directory]

    return directory_sizes


def main():
    with open('day-7-2022/input-1.txt') as rd:
        items = [line for line in rd.readlines()]

        directory_sizes = build_map_of_directory_sizes(items)
        over = 0
        under = 0
        sum = 0
        for key, value in directory_sizes.items():
            if value <= 100000:
                under += 1
                sum += value
            else:
                over += 1
        print(sum, over, under)


if __name__ == "__main__":
    main()
