#! /usr/bin/env python

def main():
    with open('problem-3/input-advent-of-code-3.txt') as rd:
        signals = [x.strip() for x in rd.readlines()]
        solution_1 = part1(signals)
        print("Solution 1", solution_1)
        solution_2 = part2(signals)
        print("Solution 2", solution_2)


        
        
def part1(signals):
    gamma = ""
    epsilon = ""
    for i in range(0, len(signals[0])):
            count_0 = 0
            count_1 = 0
            for signal in signals:
                if signal[i] == '0':
                    count_0 += 1
                elif signal[i] == '1':
                    count_1 += 1
            gamma = gamma + ('1' if count_1 >= count_0 else '0')
            epsilon = epsilon + ('1' if count_1 < count_0 else '0')
            
    return int(gamma, 2) * int(epsilon, 2) 
    

def part2(signals):
    temp_signals = signals
    o2_result = ""
    co2_result = ""
    for i in range(0, len(signals[0])):
        most_common_bit_at_current_index = most_common_bit(temp_signals, i)
        temp_signals = filter(lambda signal: signal[i] == most_common_bit_at_current_index, temp_signals)
        if (len(temp_signals) == 1):
            o2_result = temp_signals[0]
            break

    temp_signals = signals
    for i in range(0, len(signals[0])):
        least_common_bit_at_current_index = least_common_bit(temp_signals, i)
        temp_signals = filter(lambda signal: signal[i] == least_common_bit_at_current_index, temp_signals)
        if (len(temp_signals) == 1):
            co2_result = temp_signals[0]
            break
    
    return(int(o2_result, 2) * int(co2_result, 2))

def most_common_bit(signals, index):
    count_0 = 0
    count_1 = 0
    for signal in signals:
        if signal[index] == '0':
            count_0 += 1
        elif signal[index] == '1':
            count_1 += 1
    return '1' if count_1 >= count_0 else '0'

def least_common_bit(signals, index):
    count_0 = 0
    count_1 = 0
    for signal in signals:
        if signal[index] == '0':
            count_0 += 1
        elif signal[index] == '1':
            count_1 += 1
    return '1' if count_1 < count_0 else '0'
    

if __name__ == "__main__":
    main()
