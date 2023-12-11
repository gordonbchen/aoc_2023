import numpy as np


# Read data.
with open("data.txt") as f:
    data = np.array([list(i) for i in f.read().split()])

# Expand empty lines.
new_data = []
for row in data:
    if np.all(row == "."):
        new_data.append(row)
    new_data.append(row)

data = np.array(new_data)

new_data = []
for col in data.T:
    if np.all(col == "."):
        new_data.append(col)
    new_data.append(col)

data = np.array(new_data).T

# Find coords of all galaxies.
coords = np.array(list(zip(*np.where(data == "#"))))

# Find dists to each other galaxy.
total_dists = 0
for (i, c_i) in enumerate(coords[:-1]):
    for (j, c_j) in enumerate(coords[i + 1:]):
        total_dists += np.sum(np.abs(c_i - c_j))

print(total_dists)
