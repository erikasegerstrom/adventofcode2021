from typing import List
from numpy.core.fromnumeric import size
from tqdm import tqdm
import numpy as np

class School():
    def __init__(self, list_initial_lanternfish: List[int]) -> None:
        self.nr_per_state = [0]*9
        for lantern in list_initial_lanternfish:
            self.nr_per_state[lantern] += 1
        
    def update_lanterns(self) -> None:
        n_add = self.nr_per_state[0]
        for i in range(1, len(self.nr_per_state)):
            self.nr_per_state[i-1] = self.nr_per_state[i]
        self.nr_per_state[6] += n_add
        self.nr_per_state[8] = n_add

    def propagate(self, days = int) -> int:
        for day in tqdm(range(0, days)):
            self.update_lanterns()
        return sum(self.nr_per_state)

if __name__ == "__main__":
    raw = open('inputs/day06.txt').read()
    initial_lanternfish = [int(n) for n in raw.split(",")]
    school = School(initial_lanternfish)
    days = 256
    result = school.propagate(days)
    print(result)