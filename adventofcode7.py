import numpy as np
from tqdm import tqdm

def construct_fuel_cost_list(max_position: int) -> list[int]:
    """
    Construct list where index = x holds cost for x unit moves
    """
    fuel_cost = [0]
    for i in range(1, max_position):
        fuel_cost.append(fuel_cost[i-1] + i)

    return fuel_cost

def calculate_fuel(distance_array: np.array, cost_array: np.array):
    """
    For each distance retrieve the corresponding fuel cost and return sum
    """
    fuel_array = [cost_array[abs(i)] for i in distance_array] 
    
    return sum(fuel_array)

raw = open('inputs/day07.txt').read()
initial_positions = np.array([int(n) for n in raw.split(",")])
max_position = np.amax(initial_positions)
fuel_consumption = []
fuel_consumption2 = [] 
fuel_cost_list = construct_fuel_cost_list(max_position)

for i in tqdm(range(1, max_position)):
    distance = initial_positions - i
    fuel_consumption.append(sum(abs(distance)))
    fuel_consumption2.append(calculate_fuel(distance, fuel_cost_list))

print("Assignment 1: ", np.amin(fuel_consumption))
print("Assignment 2: ", np.amin(fuel_consumption2))