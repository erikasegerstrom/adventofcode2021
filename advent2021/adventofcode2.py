from typing import List

inputs = [["forward", "5"], 
    ["down", "5"],
    ["forward", "8"],
    ["up", "3"],
    ["down", "8"],
    ["forward", "2"]]

def find_coordinates_and_multiply(inputs: List) -> int:
    horizontal = 0
    depth = 0
    for input in inputs: 
        direction, units = input
        if direction == "forward":
            horizontal += int(units)
        elif direction == "down":
            depth += int(units)
        elif direction == "up":
            depth -= int(units)
    return(horizontal * depth)

assert find_coordinates_and_multiply(inputs) == 150

def find_coordinates_and_multiply2(inputs: List) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    for input in inputs: 
        direction, units = input
        if direction == "forward":
            horizontal += int(units)
            depth += (aim * int(units))
        elif direction == "down":
            aim += int(units)
        elif direction == "up":
            aim -= int(units)
    return(horizontal * depth)

assert find_coordinates_and_multiply2(inputs) == 900

with open("inputs/day02.txt") as f:
    inputs = [line.strip().split() for line in f]
    product = find_coordinates_and_multiply(inputs)
    product2 = find_coordinates_and_multiply2(inputs)
    print(product)
    print(product2)