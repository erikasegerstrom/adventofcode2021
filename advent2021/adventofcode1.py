from typing import List

inputs = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def count_n_increase(input: List[int]) -> int:
    """
    Find number of increase instances in list sequentially 
    comparing one element to the next
    """
    delta = [input[n]-input[n-1] for n in range(1,len(input))]
    pos_count = len(list(filter(lambda x: (x > 0), delta)))
    return pos_count

assert count_n_increase(inputs) == 7

def create_sliding_window_list(input: List[int]) -> List[int]:
    """
    Convert a list into a sliding window sequentially 
    summing elements with the following two elements  
    """
    sliding_window_list = [input[n]+input[n-1]+input[n-2] for n in range(2,len(input))]
    return sliding_window_list

assert create_sliding_window_list(inputs) == [607, 618, 618, 617, 647, 716, 769, 792]

with open("inputs/day01.txt") as f:
    inputs = [int(line.strip()) for line in f]
    print("Assignment 1: ", count_n_increase(inputs))
    sliding_window_list = create_sliding_window_list(inputs)
    print("Assignment 2: ", count_n_increase(sliding_window_list))
