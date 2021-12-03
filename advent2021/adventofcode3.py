from typing import Tuple


input = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"]


def binary_to_int(binary: int) -> int:
    """
    Convert binary number to integer
    """
    converted_int = 0
    base = 1
    while(binary):
        remainder = binary % 10
        converted_int += remainder * base
        base = base * 2
        binary = int(binary/10)
    return converted_int

assert binary_to_int(10101001) == 169


def find_most_and_least_common_binary(input: list[str]) -> Tuple[str, str]:
    """
    Find most and least common binary per index in list of binarys
    """
    binary_length = len(input[0])
    n_binary = len(input)
    most_common = ""
    least_common = ""
    for i in range(0, binary_length):
        sum = 0
        for binary in input:
            sum += int(binary[i])
        if sum/n_binary == 0.5:
            most_common = (most_common + str(1))
            least_common = (least_common + str(0))
        else:            
            most_common = (most_common + str(round(sum/n_binary)))
            least_common = (least_common + str(abs(round(sum/n_binary)-1)))

    return most_common, least_common

assert find_most_and_least_common_binary(input) == ("10110", "01001")

def find_oxygen_generator_rating(input: list[str]) -> list[str]:
    residual_list = input
    i = 0
    while (len(residual_list) > 1):
        most_common, least_common = find_most_and_least_common_binary(residual_list)
        residual_list = list(filter(lambda binary: binary[i] == most_common[i], residual_list))
        i += 1
    return residual_list

assert find_oxygen_generator_rating(input) == ["10111"]

def find_CO2_scrubber_rating(input: list[str]) -> list[str]:
    residual_list = input
    i = 0
    while (len(residual_list) > 1):
        most_common, least_common = find_most_and_least_common_binary(residual_list)
        residual_list = list(filter(lambda binary: binary[i] == least_common[i], residual_list))
        i += 1
        
    return residual_list

assert find_CO2_scrubber_rating(input) == ["01010"]
    
with open("inputs/day03.txt") as f:
    inputs = [line.strip() for line in f]
    most_common, least_common = find_most_and_least_common_binary(inputs)
    most_common_int = binary_to_int(int(most_common))
    least_common_int = binary_to_int(int(least_common))
    product = most_common_int * least_common_int
    print("Assignment 1: ", product)

    oxygen_rating = find_oxygen_generator_rating(inputs)
    oxygen_rating_int = binary_to_int(int(oxygen_rating[0]))
    CO2_scrubber_rating = find_CO2_scrubber_rating(inputs)
    CO2_scrubber_rating_int = binary_to_int(int(CO2_scrubber_rating[0]))
    product = oxygen_rating_int * CO2_scrubber_rating_int
    print("Assignment 2: ", product)
"""    
oxygen_rating = find_oxygen_generator_rating(input)
oxygen_rating_int = binary_to_int(int(oxygen_rating[0]))
CO2_scrubber_rating = find_CO2_scrubber_rating(input)
CO2_scrubber_rating_int = binary_to_int(int(CO2_scrubber_rating[0]))
product = oxygen_rating_int * CO2_scrubber_rating_int
print("Oxygen rating: ", oxygen_rating, oxygen_rating_int)
print("CO2 scrubber rating: ", CO2_scrubber_rating, CO2_scrubber_rating_int)
print("Assignment 2: ", product)"""