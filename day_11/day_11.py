import numpy as np


# Read data.
with open("data.txt") as f:
    data = np.array([list(i) for i in f.read().split()])

# Find coords of all galaxies.
coords = list(zip(*np.where(data == "#")))

# Calculate distance between galaxies.
def calc_dist(c1, c2, data: np.ndarray, empty_dist: int) -> int:
    y1, x1 = c1  # Flipped b/c y = rows.
    y2, x2 = c2

    # Find vertical dist.
    vert_dist = 0
    for n_row in range(min(y1, y2) + 1, max(y1, y2) + 1):
        if not np.any(data[n_row] == "#"):
            vert_dist += empty_dist
        else:
            vert_dist += 1

    # Find horizontal dist.
    horiz_dist = 0
    for n_col in range(min(x1, x2) + 1, max(x1, x2) + 1):
        if not np.any(data[:, n_col] == "#"):
            horiz_dist += empty_dist
        else:
            horiz_dist += 1

    return vert_dist + horiz_dist

# Find dists to each other galaxy.
total_dists = 0
for (i, c_i) in enumerate(coords[:-1]):
    for (j, c_j) in enumerate(coords[i + 1:]):
        dist = calc_dist(c_i, c_j, data, int(1e6))
        total_dists += dist

print(total_dists)
