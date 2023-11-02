import numpy as np

def find_lowpoints(padded: np.array): # -> list[int], list[int]:
    """
    Find and return lowpoints including indices.
    """
    nr_rows = padded.shape[0]
    nr_cols = padded.shape[1]
        
    low_points = []
    low_points_indices = []
    for i in range(1,nr_rows-1):
        for j in range(1, nr_cols-1):
            elem = padded[i][j]
            up = padded[i][j-1]
            left = padded[i-1][j]
            right = padded[i+1][j]
            down = padded[i][j+1]
            if elem<left and elem<right and elem<up and elem<down:
                low_points.append(elem)
                low_points_indices.append([i,j])
    return low_points, low_points_indices

def find_basinsize(padded: np.array, low_points_indices: list[int]):
    for index in low_points_indices:
        print(index)

with open('inputs/day09.txt') as f:
    inputs = np.array([[int(i) for i in line.strip().split()[0]] for line in f])

padded = np.pad(inputs, 1, 'constant',  constant_values=9)   
low_points, low_points_indices = find_lowpoints(padded)

"""
Part 1
"""
#print("Low points: ", str(low_points))
#print("Low points indices: ", low_points_indices)
risk_level = sum(low_points) + len(low_points)
#print("Risk level: ", str(risk_level))

"""
Part 2
"""
find_basinsize(padded, low_points_indices)
