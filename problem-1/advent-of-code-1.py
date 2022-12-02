#! /usr/bin/env python

def main():
    with open('problem-1/input-advent-of-code-1.txt') as rd:
        ranges = [x.strip() for x in rd.readlines()]
        #convert to ints
        ranges = [int(item) for item in ranges]
        # count number of increased entries with original input
        noisy_count = count_increased_entries(ranges)
        print("noisy count", noisy_count)
        # count number of increased entries with reduced noise
        new_ranges = sum_3_entries(ranges=ranges)
        less_noisy_count = count_increased_entries(new_ranges)
        print("less noisy count", less_noisy_count)    



def sum_3_entries(ranges):
    new_ranges = []
    for i in range(0, len(ranges)):
        new_ranges.append(sum(ranges[i:i + 3]))
    return new_ranges

def count_increased_entries(ranges):
    prev_range = ranges[0]
    counter = 0
    index = 0
    for current_range in ranges[1:]:
        if (current_range > prev_range):
            counter += 1
        index += 1
        prev_range = ranges[index] 
    return counter

if __name__ == "__main__":
    main()
