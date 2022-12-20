#! /usr/bin/env python
import json
from functools import cmp_to_key


def get_pairs(items):
    pairs = []
    temp = []
    for item in items:
        if item == '\n':
            pairs.append(temp)
            temp = []
        else:
            packet = json.loads(item.strip())
            temp.append(packet)
    pairs.append(temp)
    return pairs


def pair_is_in_right_order(pair):
    left = pair[0]
    right = pair[1]
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        elif right < left:
            return False
        else:
            return None
    elif isinstance(left, int):  # left int right list
        new_pair = [[left], right]
        return pair_is_in_right_order(new_pair)
    elif isinstance(right, int):  # right int left list
        new_pair = [left, [right]]
        return pair_is_in_right_order(new_pair)
    else:
        for i in range(max(len(left), len(right))):
            if len(left) - 1 < i:
                return True
            if len(right) - 1 < i:
                return False
            new_pair = [left[i], right[i]]
            right_order = pair_is_in_right_order(new_pair)
            if right_order is not None:
                return right_order
    return None


def part1(pairs):
    right_order = 0
    indices = []
    for i, pair in enumerate(pairs):
        right = pair_is_in_right_order(pair)
        if right:
            right_order += 1
            indices.append(i + 1)

    sum = 0
    for index in indices:
        sum += index
    return sum


def part2(packets):
    packets.sort(key=cmp_to_key(compare))
    answer = 1
    for i, packet in enumerate(packets):
        if str(packet) == '[[2]]' or str(packet) == '[[6]]':
            answer = answer * (i + 1)
    return answer


def compare(item1, item2):
    if pair_is_in_right_order([item1, item2]):
        return -1
    elif not pair_is_in_right_order([item1, item2]):
        return 1
    else:
        return 0


def get_all_packets(items):
    packets = []
    for item in items:
        if item != '\n':
            packet = json.loads(item.strip())
            packets.append(packet)
    return packets


def main():
    with open('day-13-2022/input-1.txt') as rd:
        items = [line for line in rd.readlines()]

        # 1
        pairs = get_pairs(items)
        answer_1 = part1(pairs)

        # 2
        packets = get_all_packets(items)
        answer_2 = part2(packets)
        for packet in packets:
            print(packet)
        print(answer_1)
        print(answer_2)


if __name__ == "__main__":
    main()
