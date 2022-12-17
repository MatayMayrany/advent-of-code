#! /usr/bin/env python
monkey_map = {}
divisible_by_all = 1


def build_monkey_map(lines):
    global divisible_by_all
    monkey_parts = []
    for line in lines:
        monkey_parts.append(line)
        if len(monkey_parts) == 6:
            id = int(monkey_parts[0].split(' ')[1][0])
            items = [int(x) for x in monkey_parts[1].split(':')[1].strip().split(',')]
            # Operation: new = old * 19
            operation_sign, operation_value = monkey_parts[2].split(' ')[4], monkey_parts[2].split(' ')[5]
            divisible_value, true_monkey_id, false_monkey_id = \
                int(monkey_parts[3].split(' ')[3]), \
                int(monkey_parts[4].split(' ')[5]), \
                int(monkey_parts[5].split(' ')[5])
            monkey = Monkey(id, items, operation_sign, operation_value, divisible_value, true_monkey_id,
                            false_monkey_id)
            divisible_by_all = divisible_by_all * divisible_value
            monkey_map[id] = monkey
            monkey_parts.clear()


def main():
    with open('day-11-2022/input-1.txt') as rd:
        lines = [line.strip() for line in rd.readlines() if line != '\n']
        build_monkey_map(lines)
    # part 1
    for round in range(0, 10000):
        for monkey_id in range(0, len(monkey_map)):
            monkey_map[monkey_id].start_turn()

    inspected = []
    for id, monkey in monkey_map.items():
        inspected.append(monkey.inspected_items)
    max_1 = max(inspected)
    inspected.remove(max_1)
    max_2 = max(inspected)
    print(max_1 * max_2)


class Monkey:
    def __init__(self, id, items, operation_sign, operation_value, divisible_value, true_monkey_id, false_monkey_id):
        self.id = id
        self.items = items
        self.operation_sign = operation_sign
        self.operation_value = operation_value
        self.divisible_value = divisible_value
        self.true_monkey_id = true_monkey_id
        self.false_monkey_id = false_monkey_id
        self.inspected_items = 0

    def start_turn(self):
        for item in self.items:
            self.inspected_items += 1
            if self.operation_sign == '*':
                new_worry = item * item if self.operation_value == 'old' else item * int(self.operation_value)
            else:
                new_worry = item + item if self.operation_value == 'old' else item + int(self.operation_value)

            new_worry = new_worry % divisible_by_all  # bored monkey
            if new_worry % self.divisible_value == 0:
                monkey_map[self.true_monkey_id].add_item(new_worry)
            else:
                monkey_map[self.false_monkey_id].add_item(new_worry)
        self.items.clear()

    def add_item(self, item):
        self.items.append(item)

    def to_string(self):
        print("id: ", self.id, "items: ", self.items)

    def print_inspected(self):
        print("inspected: ", self.inspected_items)


if __name__ == "__main__":
    main()
