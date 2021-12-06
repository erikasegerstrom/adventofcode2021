import numpy as np

raw = open('inputs/day05.txt').read()
pairs = [paragraph.split('->') for paragraph in raw.split("\n")]

x1 = []
y1 = []
x2 = []
y2 = []
for pair in pairs:
    x, y = pair[0].split(',')
    x1.append(int(x))
    y1.append(int(y))
    x, y = pair[1].split(',')
    x2.append(int(x))
    y2.append(int(y))


xmax = np.max([np.max(x1), np.max(x2)])
#print(xmax)
ymax = np.max([np.max(y1), np.max(y2)])
#print(ymax)

class VentsMap():
    def __init__(self, x1, x2, y1, y2) -> None:
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.n_rows = np.max([np.max(x1), np.max(x2)])
        self.n_columns = np.max([np.max(y1), np.max(y2)])
        self.map_values = np.zeros(self.n_rows, self.n_columns)

    def print_map(self):
        
        for x in range (self.x1, self.x2):
            for y in range (0, y):
                self.map_values[x][y] += 1

